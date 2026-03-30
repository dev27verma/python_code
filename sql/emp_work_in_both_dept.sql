| emp_id | emp_name | dept_id |
| ------ | -------- | ------- |
| 1      | A        | 101     |
| 1      | A        | 102     |
| 2      | B        | 101     |
| 3      | C        | 102     |
| 4      | D        | 103     |
| 5      | E        | 101     |
| 5      | E        | 102     |
| 5      | E        | 103     |

-- Write an SQL query to find employees who work in more than one department.
SELECT emp_id, emp_name
FROM employee
GROUP BY emp_id, emp_name
HAVING COUNT(DISTINCT dept_id) > 1;


-- Write an SQL query to find employees who work in both 101 and 102 departments.
SELECT emp_id, emp_name
FROM employee
WHERE dept_id IN (101, 102)
GROUP BY emp_id, emp_name
HAVING COUNT(DISTINCT dept_id) = 2;