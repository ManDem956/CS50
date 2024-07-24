-- SELECT tt.type,
-- ,
--     sum(ut.amount) AS credit
-- FROM user_transaction ut
--     JOIN transaction_type tt ON tt.id = ut.transation_type_id
-- WHERE tt.type = 'credit'
--     AND ut.user_id = 2;
.mode table
.headers on
select  username, user_id, sum(amount) balance FROM(
SELECT u.username, ut.user_id,
    tt.type,
    CASE
        tt.type
        WHEN 'credit' THEN ut.amount * -1
        ELSE ut.amount
    END amount
FROM user_transaction ut
    JOIN transaction_type tt ON tt.id = ut.transation_type_id
    join users u on u.id = ut.user_id
ORDER BY ut.user_id,
    tt.type)
group by user_id