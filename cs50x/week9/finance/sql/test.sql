drop table if exists shares;
CREATE TABLE shares(
    id INTEGER PRIMARY KEY,
    amount INT,
    user_id INT,
    transaction_id INT,
    stock_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (transaction_id) REFERENCES transactions (id),
    FOREIGN KEY (stock_id) REFERENCES stock(id))