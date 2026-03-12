| Employees                                     Departments                             Result
| ------------- | ------------ | ------     | --------------- | --------- |              ---------- | ------------ / ------ | -------------- |
| EmployeeID    | EmployeeName | DeptID     | DeptID          | DeptName  |              EmployeeID | EmployeeName | DeptID | DepartmentName |
| 1             | Alice        | 101        | 101             | HR        |              1          | Alice        | 101   | HR             |
| 2             | Bob          | 102        | 102             | Marketing |              2          | Bob          | 102    | Marketing      |
| 3             | Charlie      | 101        | 101             | HR        |              3          | Charlie      | 101    | HR             |


Given two tables, Employees and Departments, write an SQL query to list all employees with their corresponding department names.



SELECT
e.EmployeeID,
e.EmployeeName,
e.DepartmentID,
d.DepartmentName
FROM Employees e
JOIN Departments d
ON e.DepartmentID = d.DepartmentID;


