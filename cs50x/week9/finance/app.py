import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
# from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)


# def lookup(symbol):
#     return {"price": 1.00, "symbol": symbol}


SQL_INSERT_USER = "insert into users (username, hash) values(?,?)"
SQL_GET_USER_CASH = "select cash from users where id = ?"

SQL_INSERT_TRANSACTION = "insert into user_transaction (user_id, transation_type_id, symbol, quantity, price)\
    VALUES(?,\
        (select id from transaction_type where name = ?),\
        ?,?,?)"

SQL_GET_STOCKS = """
SELECT user_id,
    symbol,
    sum(quantity) quantity
FROM(
        SELECT ut.user_id,
            ut.symbol,
            tt.type,
            CASE
                tt.type
                WHEN 'debit' THEN ut.quantity * -1
                ELSE ut.quantity
            END quantity
        FROM user_transaction ut
            JOIN transaction_type tt ON tt.id = ut.transation_type_id
        ORDER BY ut.user_id,
            tt.type
    )
GROUP BY user_id,
    symbol
HAVING symbol NOT NULL and sum(quantity) > 0 and user_id = ?"""

SQL_USER_HISTORY = """SELECT DATETIME(ut.transation_time, 'localtime') time, tt.name,
    ut.symbol,
    ut.quantity,
    ut.price,
    ut.amount
FROM user_transaction ut
    JOIN transaction_type tt ON tt.id = ut.transation_type_id
WHERE ut.user_id = ?
ORDER BY transation_time ASC
"""

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    try:
        result = db.execute(SQL_GET_STOCKS, session["user_id"])
        cash = db.execute(SQL_GET_USER_CASH, session["user_id"])[0]["cash"]
    except (RuntimeError, ValueError) as e:
        do_report(str(e))

    for res in result:
        lookup_result = do_lookup(res["symbol"])
        res["price"] = lookup_result["price"]
        res["amount"] = round(lookup_result["price"] * res["quantity"], 2)

    result.append({"symbol": "Cash", "quantity": None, "price": None, "amount": cash})
    return render_template("index.html", result=result, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        try:
            if int(shares) <= 0:
                raise ValueError(f"Incorrect number of shares {shares=}")
            result = do_lookup(symbol)
            db.execute(SQL_INSERT_TRANSACTION, session["user_id"],
                       "BUY", result["symbol"], shares, result["price"])
        except ValueError as e:
            return do_report(str(e), "warning")
        else:
            return redirect("/")

    return render_template("buy.html", quotes=session.get("quotes"))


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    result = db.execute(SQL_USER_HISTORY, session["user_id"])
    return render_template("history.html", history=result)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get(
                "username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        try:
            do_lookup(request.form.get("symbol"))
        except ValueError as e:
            return do_report(str(e), "warning")

    return render_template("quote.html", quotes=session.get("quotes"))


@app.route("/register/", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        try:
            create_user(
                request.form.get("username"),
                request.form.get("password"),
                request.form.get("confirmation"),
            )
        except ValueError as e:
            return do_report(str(e), "warning")
        else:
            return redirect("/login")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        try:
            if int(shares) <= 0:
                raise ValueError(f"Incorrect number of shares {shares=}")
            result = do_lookup(symbol)
            db.execute(SQL_INSERT_TRANSACTION, session["user_id"],
                       "SELL", result["symbol"], shares, result["price"])
        except ValueError as e:
            return do_report(str(e), "warning")
        else:
            return redirect("/")

    try:
        result = db.execute(SQL_GET_STOCKS, session["user_id"])
    except ValueError as e:
        do_report(str(e))
    else:
        return render_template("sell.html", quotes=session.get("quotes"), stocks=result)


def create_user(username: str, password: str, confirm: str) -> None:

    if not username or not password:
        raise ValueError("Invalid username or password`")

    password = generate_password_hash(password)

    if not check_password_hash(password, confirm):
        raise ValueError("Passwords do not match")

    try:
        db.execute(SQL_INSERT_USER, username, password)
    except (RuntimeError, ValueError) as e:
        msg = str(e)
        if msg.startswith('UNIQUE'):
            msg = "User already esists"
        raise ValueError(msg)


def do_lookup(symbol):
    if not session.get("quotes"):
        session["quotes"] = {}

    result = lookup(symbol)

    if result is not None:
        session["quotes"][result["symbol"]] = result["price"]
    else:
        raise ValueError(f"Symbol `{symbol=}` does not exist.")

    return result


def do_report(msg: str, category: str, r_302: str = None, status: int = 400):
    app.logger.warning(msg)
    flash(msg, category=category)
    if r_302:
        return redirect(r_302)
    return apology(msg)
