        sales_table                                                                     output
| product_id              | sale_date  | sales_amount |   | product_id       | sale_date  | sales_amount | moving_avg_3_month |   |
| ----------------------- | ---------- | ------------ | - | ---------------- | ---------- | ------------ | ------------------ | - |
| 101                     | 2026-01-01 | 100          |   | 101              | 2026-01-01 | 100          | 100.00             |   |
| 101                     | 2026-02-01 | 200          |   | 101              | 2026-02-01 | 200          | 150.00             |   |
| 101                     | 2026-03-01 | 300          |   | 101              | 2026-03-01 | 300          | 200.00             |   |
| 101                     | 2026-04-01 | 400          |   | 101              | 2026-04-01 | 400          | 300.00             |   |
| 102                     | 2026-01-01 | 150          |   | 102              | 2026-01-01 | 150          | 150.00             |   |
| 102                     | 2026-02-01 | 250          |   | 102              | 2026-02-01 | 250          | 200.00             |   |
| 102                     | 2026-03-01 | 350          |   | 102              | 2026-03-01 | 350          | 250.00             |   |


--How do you calculate the moving average of sales over the last three months for each product?
--Write a SQL query using window functions to achieve this and explain how you would ensure accuracy in your calculations.

-- Assuming your table is named "sales" and has columns like "product_id", "sale_date", and "sales_amount"
SELECT
    product_id,
    sale_date,
    sales_amount,
    -- Calculate the 3-month moving average for each product
    AVG(sales_amount) OVER (PARTITION BY product_id ORDER BY sale_date ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_average
FROM
    sales_table
ORDER BY
    product_id, sale_date;