| **Employees** |              |                | **Departments** |                 | **Output** |          |
| ------------- | ------------ | ------         | --------------- | ---------       | ---------- | -------- |
| EmployeeID    | EmployeeName | DeptID         | DeptID          | DeptName        | DeptID     | DeptName |
| 1             | Alice        | 101            | 101             | HR              |            |          |
| 2             | Bob          | 102            | 102             | Marketing       |            |          |
| 3             | Charlie      | 101            | 103             | Finance         | 103        | Finance  |
| 4             | David        | 104            | 104             | Developer       |            |          |

-- write sql to find the department without employee
SELECT
d.DepartmentID,
d.DepartmentName
FROM Departments d
LEFT JOIN Employees e
ON d.DepartmentID = e.DepartmentID
WHERE e.EmployeeID IS NULL;