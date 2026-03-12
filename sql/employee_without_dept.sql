| **Employees** |              |                | **Departments** |                 | **Output** |              |        |
| ------------- | ------------ | ------         | --------------- | ---------       | ---------- | ------------ | ------ |
| EmployeeID    | EmployeeName | DeptID         | DeptID          | DeptName        | EmployeeID | EmployeeName | DeptID |
| 1             | Alice        | 101            | 101             | HR              |            |              |        |
| 2             | Bob          | 102            | 102             | Marketing       |            |              |        |
| 3             | Charlie      | 101            | 103             | Finance         |            |              |        |
| 4             | David        | 104            |                 |                 | 4          | David        | 104    |
-- sql query to find employee without department
SELECT
e.EmployeeID,
e.EmployeeName,
e.DepartmentID
FROM Employees e
LEFT JOIN Departments d
ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentID IS NULL;