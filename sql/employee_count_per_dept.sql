| **Employees** |              |                | **Departments** |                 | **Output** |           |          |
| ------------- | ------------ | ------         | --------------- | ---------       | ---------- | --------- | -------- |
| EmployeeID    | EmployeeName | DeptID         | DeptID          | DeptName        | DeptID     | DeptName  | EmpCount |
| 1             | Alice        | 101            | 101             | HR              | 101        | HR        | 2        |
| 2             | Bob          | 102            | 102             | Marketing       | 102        | Marketing | 1        |
| 3             | Charlie      | 101            | 103             | Finance         | 103        | Finance   | 0        |
| 4             | David        | 104            | 104             | Developer       | 104        | Developer | 1        |

-- write sql to count the number of employee per dept
SELECT
d.DepartmentID,
d.DepartmentName,
COUNT(e.EmployeeID) AS employee_count
FROM Departments d
LEFT JOIN Employees e
ON d.DepartmentID = e.DepartmentID
GROUP BY d.DepartmentID, d.DepartmentName;