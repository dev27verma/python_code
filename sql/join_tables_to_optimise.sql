|       Customers                                                                       Products Table                                      Sale table
| CustomerID | CustomerName | City      | State       |     |ProductID| ProductName | Category    | Price  |    |SaleID | SaleDate   | Quantity | CustomerID | ProductID |
| -----------| ------------ | --------- | ----------- |     |---------| ----------- | ----------- | -------|    |------ | ---------- | -------- | ---------- | --------- |
| 1          | Rahul        | Delhi     | Delhi       |     | 101      | Laptop      | Electronics | 80000 |    | 1      | 2023-01-10 | 2        | 1          | 101       |
| 2          | Priya        | Mumbai    | Maharashtra |     | 102      | Mobile      | Electronics | 30000 |    | 2      | 2023-03-15 | 1        | 2          | 102       |
| 3          | Amit         | Bangalore | Karnataka   |     | 103      | Chair       | Furniture   | 5000  |    | 3      | 2023-06-20 | 3        | 3          | 103       |
| 4          | Sneha        | Chennai   | Tamil Nadu  |     | 104      | Table       | Furniture   | 7000  |    | 4      | 2023-09-05 | 2        | 1          | 104       |
|            |              |           |             |     |          |             |             |       |    | 5      | 2022-12-25 | 1        | 4          | 102       |

-- write sql query to get the details from Sales, Customers, and Products tables
-- using the appropriate keys and return only the records where the SaleDate is between '2023-01-01' and '2023-12-31'

SELECT
    s.SaleID, s.SaleDate, s.Quantity, s.CustomerID, c.CustomerName, c.City, c.State, p.ProductName, p.Category, p.Price
FROM
    Sales s -- Start with the main table you want to retrieve data from
JOIN
    Customers c ON s.CustomerID = c.CustomerID -- Join with Customers using the shared key
JOIN
    Products p ON s.ProductID = p.ProductID -- Join with Products using the shared key
WHERE
    s.SaleDate BETWEEN '2023-01-01' AND '2023-12-31'; -- Example filter for a specific date range