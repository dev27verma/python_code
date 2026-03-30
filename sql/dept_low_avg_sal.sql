| emp_id | emp_name | dept_id | salary |
| ------ | -------- | ------- | ------ |
| 1      | A        | 10      | 10000  |
| 2      | B        | 20      | 20000  |
| 3      | C        | 10      | 30000  |
| 4      | D        | 30      | 15000  |
| 5      | E        | 10      | 20000  |
| 6      | F        | 20      | 25000  |

-- Write an SQL query to find the department with the lowest average salary.
SELECT dept_id
FROM employee
GROUP BY dept_id
ORDER BY AVG(salary) ASC
LIMIT 1;
