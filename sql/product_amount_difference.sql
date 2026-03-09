            order_table                                                     output
| order_id | customer_id | order_date | order_amount |      | customer_id      | order_id | order_date | order_amount | prev_order_amount | amount_diff |
| ---------| ----------- | ---------- | ------------ | -    | ---------------- | -------- | ---------- | ------------ | ----------------- | ----------- |
| 1        | 101         | 2024-01-01 | 500          |      | 101              | 1        | 2024-01-01 | 500          | NULL              | NULL        |
| 2        | 101         | 2024-01-05 | 700          |      | 101              | 2        | 2024-01-05 | 700          | 500               | 200         |
| 3        | 101         | 2024-01-10 | 650          |      | 101              | 3        | 2024-01-10 | 650          | 700               | -50         |
| 4        | 102         | 2024-01-02 | 300          |      | 102              | 4        | 2024-01-02 | 300          | NULL              | NULL        |
| 5        | 102         | 2024-01-08 | 450          |      | 102              | 5        | 2024-01-08 | 450          | 300               | 150         |


-- write sql to calculate the difference in order amount from the previous order for each customer order
WITH prev_orders AS (
    SELECT *,
        LAG(order_amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_order_amount
    FROM orders
)
SELECT
    customer_id, order_id, order_date, order_amount, prev_order_amount, order_amount - prev_order_amount AS amount_diff
FROM prev_orders
ORDER BY customer_id, order_date;