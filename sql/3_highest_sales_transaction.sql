sales_transaction
| customer_id | transaction_id | transaction_date | sales_amount |     rnk
| ----------- | -------------- | ---------------- | ------------ |
| C101        | T1001          | 2026-02-25       | 9500         |      1
| C101        | T1008          | 2026-02-18       | 8700         |      2
| C101        | T1015          | 2026-02-05       | 8200         |      3
| C101        | T1020          | 2026-01-10       | 6000         |      4  -> older than 1 month
| C102        | T2003          | 2026-02-22       | 15000        |      1
| C102        | T2009          | 2026-02-14       | 13200        |      2
| C103        | T3004          | 2026-02-20       | 7200         |      1

--You need to find the top 3 highest sales transactions per customer in the past month. How would you approach this in BigQuery?
--Use Window Functions: Use the ROW_NUMBER() function over a partitioned set to rank transactions per customer.

SELECT
    *,
    RANK() OVER (PARTITION BY customer_id ORDER BY sales_amount DESC) AS rnk
FROM sales_transaction
    WHERE DATE_DIFF(CURRENT_DATE(), transaction_date, MONTH) = 1
    QUALIFY rnk <= 3;

output
| customer_id | transaction_id | sales_amount |
| ----------- | -------------- | ------------ |
| C101        | T1001          | 9500         |
| C101        | T1008          | 8700         |
| C101        | T1015          | 8200         |
| C102        | T2003          | 15000        |
| C102        | T2009          | 13200        |
| C103        | T3004          | 7200         |
