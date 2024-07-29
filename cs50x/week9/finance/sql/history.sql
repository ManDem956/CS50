SELECT DATETIME(ut.transation_time, 'localtime') time, tt.name,
    ut.symbol,
    ut.quantity,
    ut.price,
    ut.amount
FROM user_transaction ut
    JOIN transaction_type tt ON tt.id = ut.transation_type_id
WHERE ut.user_id = 1
ORDER BY transation_time ASC