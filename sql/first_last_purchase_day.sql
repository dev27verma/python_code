| product | customer | purchase_date | purchase_time |
| ------- | -------- | ------------- | ------------- |
| 100     | abc      | 2024-10-10    | 10:00:00      |
| 100     | abc      | 2024-10-10    | 12:00:00      |
| 100     | abc      | 2024-10-10    | 15:00:00      |
| 100     | bcd      | 2024-10-10    | 11:00:00      |
| 100     | bcd      | 2024-10-10    | 14:00:00      |
| 100     | bcd      | 2024-10-10    | 16:00:00      |
-- 1. For each customer and product, find: -- First purchase time of the day -- Last purchase time of the day
SELECT
    product, customer, purchase_date,
    MIN(purchase_time) AS first_purchase_time,
    MAX(purchase_time) AS last_purchase_time
FROM purchases
GROUP BY product, customer, purchase_date;