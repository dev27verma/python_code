--You need to find the top 3 highest sales transactions per customer in the past month. How would you approach this in BigQuery?
--Use Window Functions: Use the ROW_NUMBER() function over a partitioned set to rank transactions per customer.

WITH ranked_transactions AS (
  SELECT
    customer_id,
    transaction_id,
    amount,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rank
  FROM transactions
  WHERE transaction_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 MONTH)
)
SELECT
  customer_id,
  transaction_id,
  amount
FROM ranked_transactions
WHERE rank <= 3;