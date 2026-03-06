| product | customer | purchase_date | purchase_time |
| ------- | -------- | ------------- | ------------- |
| 100     | abc      | 2024-10-10    | 10:00:00      |
| 100     | abc      | 2024-10-10    | 12:00:00      |
| 100     | abc      | 2024-10-10    | 15:00:00      |
| 100     | bcd      | 2024-10-10    | 11:00:00      |
| 100     | bcd      | 2024-10-10    | 14:00:00      |
| 100     | bcd      | 2024-10-10    | 16:00:00      |

-- 1. For each customer and product, find:
        -- First purchase time of the day
        -- Last purchase time of the day
SELECT
    product,
    customer,
    purchase_date,
    MIN(purchase_time) AS first_purchase_time,
    MAX(purchase_time) AS last_purchase_time
FROM purchases
GROUP BY product, customer, purchase_date;
-- 2. Time difference between first and last purchase on the same day.
SELECT
    product,
    customer,
    purchase_date,
    MIN(purchase_time) AS first_purchase_time,
    MAX(purchase_time) AS last_purchase_time,
    MAX(purchase_time) - MIN(purchase_time) AS time_diff
FROM purchases
GROUP BY product, customer, purchase_date;
-- 3. Find the second purchase made by each customer for each product on a given date.
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY product, customer, purchase_date
               ORDER BY purchase_time
           ) AS rn
    FROM purchases
) t
WHERE rn = 2;
-- 4. Calculate the time difference between consecutive purchases for each customer.
SELECT
    product,
    customer,
    purchase_date,
    purchase_time,
    LAG(purchase_time) OVER (
        PARTITION BY product, customer, purchase_date
        ORDER BY purchase_time
    ) AS previous_purchase_time,
    purchase_time - LAG(purchase_time) OVER (
        PARTITION BY product, customer, purchase_date
        ORDER BY purchase_time
    ) AS time_difference
FROM purchases;