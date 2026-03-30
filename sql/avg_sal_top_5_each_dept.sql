| emp_id | emp_name | dept_id | salary |
| ------ | -------- | ------- | ------ |
| 1      | A        | 10      | 10000  |
| 2      | B        | 10      | 20000  |
| 3      | C        | 10      | 30000  |
| 4      | D        | 10      | 25000  |
| 5      | E        | 10      | 15000  |
| 6      | F        | 20      | 50000  |
| 7      | G        | 20      | 40000  |
| 8      | H        | 20      | 30000  |
| 9      | I        | 20      | 20000  |
| 10     | J        | 20      | 10000  |

-- Write an SQL query to find the average salary of top 5 highest paid employees in each department.
SELECT dept_id, AVG(salary) AS avg_salary
FROM (
      SELECT emp_id, emp_name, dept_id, salary,
             DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) rnk
      FROM employee
     ) t
WHERE rnk <= 5
GROUP BY dept_id;
