--Orders table with columns order_id, customer_id, and order_date, Write a query to find customers who have placed orders in both 2023 and 2024.

SELECT customer_id
FROM orders
WHERE EXTRACT(YEAR FROM order_date) IN (2023, 2024)
GROUP BY customer_id
HAVING COUNT(DISTINCT EXTRACT(YEAR FROM order_date)) = 2;