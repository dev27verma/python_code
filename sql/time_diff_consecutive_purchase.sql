| product | customer | purchase_date | purchase_time |
| ------- | -------- | ------------- | ------------- |
| 100     | abc      | 2024-10-10    | 10:00:00      |
| 100     | abc      | 2024-10-10    | 12:00:00      |
| 100     | abc      | 2024-10-10    | 15:00:00      |
| 100     | bcd      | 2024-10-10    | 11:00:00      |
| 100     | bcd      | 2024-10-10    | 14:00:00      |
| 100     | bcd      | 2024-10-10    | 16:00:00      |
-- 4. Calculate the time difference between consecutive purchases for each customer.
SELECT
    product, customer, purchase_date,purchase_time,
    LAG(purchase_time) OVER (PARTITION BY product, customer, purchase_date ORDER BY purchase_time) AS previous_purchase_time,
    purchase_time - LAG(purchase_time) OVER (PARTITION BY product, customer, purchase_date ORDER BY purchase_time) AS time_difference
FROM purchases;