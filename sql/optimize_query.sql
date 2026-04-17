optimize the query:
      -- need a query to find the relevant order details for the date - 2026-04-09
     -- current query very slow
     -- need to optimize it

query:
       select order_id, user_id, amount from orders o join users u
       on o.user_id = u.user_id where o.order_date=''

-- use the above order table schema


SELECT
    o.order_id,
    o.user_id,
    o.amount
FROM (
    SELECT order_id, user_id, amount
    FROM orders
    WHERE order_date = DATE '2026-04-09'
) o
JOIN users u
  ON o.user_id = u.user_id;