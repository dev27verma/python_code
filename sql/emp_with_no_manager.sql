| emp_id | emp_name | manager_id |
| ------ | -------- | ---------- |
| 1      | A        | NULL       |
| 2      | B        | 1          |
| 3      | C        | 1          |
| 4      | D        | 2          |
| 5      | E        | NULL       |

-- Write an SQL query to find all employees who do not have a manager.
SELECT emp_id, emp_name
FROM employee
WHERE manager_id IS NULL;