order_table
| order_id | customer_id | order_amount |
| -------- | ----------- | ------------ |
| O1001    | C101        | 3200         |
| O1002    | C101        | 9500         |
| O1003    | C101        | 4700         |
| O1004    | C102        | 4500         |
| O1005    | C102        | 15000        |
| O1006    | C102        | 8200         |
| O1007    | C103        | 7200         |
| O1008    | C104        | 3000         |
| O1009    | C104        | 12000        |
| O1010    | C105        | 4100         |
| O1011    | C105        | 8800         |
| O1012    | C106        | 2200         |
| O1013    | C106        | 6400         |
| O1014    | C107        | 5000         |
| O1015    | C107        | 20000        |
--Orders table with columns order_id, customer_id, order_amount, write a query to find the highest and lowest order amount for each customer.

WITH CustomerOrderSummary AS (
    SELECT
        customer_id,
        MAX(order_amount) AS max_order_amount,
        MIN(order_amount) AS min_order_amount
    FROM
        order_table
    GROUP BY
        customer_id
)
SELECT * FROM CustomerOrderSummary;