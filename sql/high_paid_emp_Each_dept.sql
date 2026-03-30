| emp_id | emp_name | dept_id | salary |
| ------ | -------- | ------- | ------ |
| 1      | A        | 10      | 10000  |
| 2      | B        | 10      | 20000  |
| 3      | C        | 10      | 30000  |
| 4      | D        | 10      | 25000  |
| 5      | E        | 20      | 15000  |
| 6      | F        | 20      | 25000  |
| 7      | G        | 20      | 30000  |
| 8      | H        | 30      | 5000   |
| 9      | I        | 30      | 7000   |
| 10     | J        | 30      | 6000   |

-- Write an SQL query to find top 3 highest paid employees in each department.
SELECT emp_id, emp_name, dept_id, salary
FROM (
    SELECT emp_id, emp_name, dept_id, salary,
           DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) rnk
    FROM employee
    ) t
WHERE rnk <= 3;
