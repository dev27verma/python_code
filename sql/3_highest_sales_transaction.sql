sales_transaction
| customer_id | transaction_id | transaction_date | sales_amount |
| ----------- | -------------- | ---------------- | ------------ |
| C101        | T1001          | 2026-02-25       | 9500         |
| C101        | T1008          | 2026-02-18       | 8700         |
| C101        | T1015          | 2026-02-05       | 8200         |
| C101        | T1020          | 2026-01-10       | 6000         |
| C102        | T2003          | 2026-02-22       | 15000        |
| C102        | T2009          | 2026-02-14       | 13200        |
| C103        | T3004          | 2026-02-20       | 7200         |

--You need to find the top 3 highest sales transactions per customer in the past month. How would you approach this in BigQuery?
--Use Window Functions: Use the ROW_NUMBER() function over a partitioned set to rank transactions per customer.

WITH ranked_transactions AS (
  SELECT
    customer_id, transaction_id, amount,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rank
  FROM sales_transaction
  WHERE transaction_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 MONTH)
)
SELECT
  customer_id,
  transaction_id,
  amount
FROM ranked_transactions
WHERE rank <= 3;