select ut.user_id, ut.transation_time, tt.name, tt.TYPE, ut.symbol, ut.quantity, ut.price, ut.amount from user_transaction ut 
join transaction_type tt on tt.id = ut.transation_type_id
where user_id=1;