--You have a dataset in BigQuery where some fields contain NULL values. How would you handle these NULL values in your queries?
--Handling NULLs in Aggregations: Use functions like IFNULL() or COALESCE() to replace NULLs with a default value.

SELECT COALESCE(sales_amount, 0) AS total_sales
FROM orders;

--# Method 2
SELECT *
FROM users
WHERE email IS NOT NULL;

--Method 3
--Filtering NULLs: To exclude NULL values from query results, use a WHERE clause.
--Counting NULL and Non-NULL Values: Use conditional expressions to count both NULL and non-NULL occurrences.

SELECT COUNTIF(email IS NULL) AS null_count, COUNTIF(email IS NOT NULL) AS not_null_count
FROM users;