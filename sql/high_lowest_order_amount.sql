--Orders table with columns order_id, customer_id, order_amount, write a query to find the highest and lowest order amount for each customer.

WITH CustomerOrderSummary AS (
    SELECT
        customer_id,
        MAX(order_amount) AS max_order_amount,
        MIN(order_amount) AS min_order_amount
    FROM
        orders
    GROUP BY
        customer_id
)
SELECT * FROM CustomerOrderSummary;