| emp_id | emp_name | dept_id |
| ------ | -------- | ------- |
| 1      | A        | 10      |
| 2      | B        | 10      |
| 3      | C        | 20      |
| 4      | D        | 20      |
| 5      | E        | 20      |
| 6      | F        | 30      |
| 7      | G        | 30      |
| 8      | H        | 40      |

-- Write an SQL query to find percentage of employees in each department.
SELECT dept_id, COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS percentage
FROM employee
GROUP BY dept_id;
