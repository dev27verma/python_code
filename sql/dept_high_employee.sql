| emp_id | emp_name | dept_id |
| ------ | -------- | ------- |
| 1      | A        | 10      |
| 2      | B        | 20      |
| 3      | C        | 10      |
| 4      | D        | 30      |
| 5      | E        | 10      |
| 6      | F        | 20      |

-- Write an SQL query to find the department with the highest number of employees.
SELECT dept_id
FROM employee
GROUP BY dept_id
ORDER BY COUNT(*) DESC
LIMIT 1;
