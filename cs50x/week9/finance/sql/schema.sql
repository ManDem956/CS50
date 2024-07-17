DROP INDEX IF EXISTS username;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS transaction_type;
DROP TABLE IF EXISTS user_transaction;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    cash NUMERIC NOT NULL DEFAULT 10000.00
);
-- CREATE TABLE sqlite_sequence(name,seq);
CREATE UNIQUE INDEX username ON users (username);
CREATE TABLE transaction_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK (TYPE IN ('credit', 'debit'))
);
INSERT INTO transaction_type (name, type)
VALUES("BUY", 'credit'),
    ("SELL", 'debit'),
    ("TOPUP", 'debit');
CREATE TABLE user_transaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    transation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transation_type_id INTEGER NOT NULL,
    symbol TEXT DEFAULT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    amount REAL NOT NULL GENERATED ALWAYS AS (quantity * price),
    FOREIGN KEY(user_id) REFERENCES users(id) FOREIGN KEY(transation_type_id) REFERENCES transaction_type(id)
);
CREATE INDEX trn_symbol ON user_transaction (symbol)