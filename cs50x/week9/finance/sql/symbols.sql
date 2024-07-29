
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
HAVING symbol NOT NULL and sum(quantity) > 0
-- and user_id = ?