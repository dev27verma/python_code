| emp_id | emp_name | dept_id |
| ------ | -------- | ------- |
| 1      | A        | 10      |
| 2      | B        | 20      |
| 3      | C        | 10      |
| 4      | D        | 30      |
| 5      | E        | 10      |
| 6      | F        | 20      |

-- Write an SQL query to find the count of employees in each department.
SELECT dept_id, COUNT(*) AS emp_count
FROM employee
GROUP BY dept_id;
