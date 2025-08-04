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
    sales
ORDER BY
    product_id, sale_date;