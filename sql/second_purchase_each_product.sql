| product | customer | purchase_date | purchase_time |
| ------- | -------- | ------------- | ------------- |
| 100     | abc      | 2024-10-10    | 10:00:00      |
| 100     | abc      | 2024-10-10    | 12:00:00      |
| 100     | abc      | 2024-10-10    | 15:00:00      |
| 100     | bcd      | 2024-10-10    | 11:00:00      |
| 100     | bcd      | 2024-10-10    | 14:00:00      |
| 100     | bcd      | 2024-10-10    | 16:00:00      |

-- 3. Find the second purchase made by each customer for each product on a given date.
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY product, customer, purchase_date ORDER BY purchase_time) AS rn
    FROM purchases
) t
WHERE rn = 2;