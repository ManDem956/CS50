PRAGMA foreign_keys = ON;

DROP INDEX IF EXISTS username;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS transaction_type;
DROP TABLE IF EXISTS user_transaction;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    cash NUMERIC NOT NULL DEFAULT 10000.00 CHECK (cash >= 0.00)
);
-- CREATE TABLE sqlite_sequence(name,seq);
CREATE UNIQUE INDEX username ON users (username);
CREATE TRIGGER new_user
AFTER
INSERT ON users BEGIN
INSERT INTO user_transaction (user_id, transation_type_id, quantity, price)
VALUES(
        (
            SELECT last_insert_rowid()
        ),
        (
            SELECT id
            FROM transaction_type
            WHERE name = 'TOPUP'
        ),
        1,
        (
            SELECT cash
            FROM users
            WHERE id = (
                    SELECT last_insert_rowid()
                )
        )
    );
END;
CREATE TABLE transaction_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    TYPE TEXT NOT NULL CHECK (TYPE IN ('credit', 'debit'))
);
INSERT INTO transaction_type (name, TYPE)
VALUES("BUY", 'credit'),
    ("SELL", 'debit'),
    ("TOPUP", 'debit');
CREATE TABLE user_transaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    transation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transation_type_id INTEGER NOT NULL,
    symbol TEXT DEFAULT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    price REAL NOT NULL,
    amount REAL NOT NULL GENERATED ALWAYS AS (quantity * price),
    FOREIGN KEY(user_id) REFERENCES users(id) FOREIGN KEY(transation_type_id) REFERENCES transaction_type(id)
);
CREATE INDEX trn_symbol ON user_transaction (symbol);
CREATE TRIGGER validate_shares_count BEFORE
INSERT ON user_transaction BEGIN
SELECT CASE
        WHEN new.quantity > (
            SELECT sum(quantity) quantity
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
            HAVING symbol NOT NULL and symbol = new.symbol
        )
        AND new.transation_type_id IN (
            SELECT id
            FROM transaction_type
            WHERE TYPE = 'debit'
        ) THEN RAISE (ABORT, 'Not enough shares to sell.')
    END;
END;
CREATE TRIGGER validate_user_balance BEFORE
INSERT ON user_transaction BEGIN
SELECT CASE
        WHEN new.amount > (
            SELECT cash
            FROM users
            WHERE users.id = new.user_id
        )
        AND new.transation_type_id IN (
            SELECT id
            FROM transaction_type
            WHERE TYPE = 'credit'
        ) THEN RAISE (ABORT, 'Insufficient funds.')
    END;
END;
CREATE TRIGGER update_user_balance
AFTER
INSERT ON user_transaction BEGIN
UPDATE users
SET cash = bal.balance
FROM (
        SELECT user_id,
            sum(amount) balance
        FROM(
                SELECT ut.user_id,
                    tt.type,
                    CASE
                        tt.type
                        WHEN 'credit' THEN ut.amount * -1
                        ELSE ut.amount
                    END amount
                FROM user_transaction ut
                    JOIN transaction_type tt ON tt.id = ut.transation_type_id
                ORDER BY ut.user_id,
                    tt.type
            )
        GROUP BY user_id
    ) bal
WHERE bal.user_id = users.id;
END;