--- find the person who bought product in consecutive month
"""
+-------------+------------+-------+
| customer_id | order_date | price |
+-------------+------------+-------+
| 101         | 2026-01-01 | 500   |
| 101         | 2026-02-01 | 600   |
| 102         | 2026-01-01 | 800   |
| 102         | 2026-03-01 | 900   |
| 103         | 2026-02-01 | 200   |
| 103         | 2026-03-01 | 100   |
+-------------+------------+-------+
"""

SELECT DISTINCT customer_id
FROM (
    SELECT
        customer_id,
        PARSE_DATE('%d-%m-%Y', order_date) AS order_dt,
        LAG(PARSE_DATE('%d-%m-%Y', order_date)) OVER (
            PARTITION BY customer_id
            ORDER BY PARSE_DATE('%d-%m-%Y', order_date)
        ) AS prev_order_dt
    FROM customer
)
WHERE DATE_DIFF(order_dt, prev_order_dt, MONTH) = 1;