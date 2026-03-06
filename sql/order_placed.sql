        orders                                                  Output
| order_id                 | customer_id | order_date |   | customer_id      |
| ------------------------ | ----------- | ---------- |  | ---------------- |
| 1                        | C101        | 2023-02-10 |   | C101             |
| 2                        | C102        | 2023-05-12 |   | C103             |
| 3                        | C101        | 2024-01-15 |   |                  |
| 4                        | C103        | 2023-07-20 |   |                  |
| 5                        | C103        | 2024-03-05 |   |                  |
| 6                        | C104        | 2024-06-18 |   |                  |


--Orders table with columns order_id, customer_id, and order_date, Write a query to find customers who have placed orders in both 2023 and 2024.

SELECT customer_id
FROM orders
GROUP BY customer_id
HAVING
    COUNT(CASE WHEN EXTRACT(YEAR FROM order_date) = 2023 THEN 1 END) > 0
AND COUNT(CASE WHEN EXTRACT(YEAR FROM order_date) = 2024 THEN 1 END) > 0;