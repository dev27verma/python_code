--- find the person who bought product in consecutive month
  orders_table
| customer_id | order_date | price |                        prev_order_date | month_diff |
| ----------- | ---------- | ----- |                         --------------- | ---------- |
| 101         | 2026-01-01 | 500   |                         NULL            | NULL       |
| 101         | 2026-02-01 | 600   |                         2026-01-01      | 1          |
| 102         | 2026-01-01 | 800   |                         NULL            | NULL       |
| 102         | 2026-03-01 | 900   |                         2026-01-01      | 2          |
| 103         | 2026-02-01 | 200   |                         NULL            | NULL       |
| 103         | 2026-03-01 | 100   |                         2026-02-01      | 1          |


SELECT DISTINCT customer_id
FROM (
    SELECT customer_id,
           DATE_DIFF(order_date,
                     LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date),
                     MONTH) AS month_diff
    FROM orders
) t
WHERE month_diff = 1;





output
| customer_id | order_date | prev_order_date |
| ----------- | ---------- | --------------- |
| 101         | 2026-02-01 | 2026-01-01      |
| 103         | 2026-03-01 | 2026-02-01      |

final output --> because i selected only customer_id
| customer_id |
| ----------- |
| 101         |
| 103         |
