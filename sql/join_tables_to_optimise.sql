--How do you generate a report that combines data from multiple sources, including sales data, customer demographics, and product information stored in different tables?
--Write a SQL query that efficiently joins these tables and explain your approach to ensure optimal performance.

SELECT
    s.SaleID,
    s.SaleDate,
    s.Quantity,
    s.CustomerID,
    c.CustomerName,
    c.City,
    c.State,
    p.ProductName,
    p.Category,
    p.Price
FROM
    Sales s -- Start with the main table you want to retrieve data from
JOIN
    Customers c ON s.CustomerID = c.CustomerID -- Join with Customers using the shared key
JOIN
    Products p ON s.ProductID = p.ProductID -- Join with Products using the shared key
WHERE
    s.SaleDate BETWEEN '2023-01-01' AND '2023-12-31'; -- Example filter for a specific date range