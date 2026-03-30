| emp_id | emp_name | dept_id | salary |
| ------ | -------- | ------- | ------ |
| 1      | A        | 10      | 10000  |
| 2      | B        | 10      | 20000  |
| 3      | C        | 10      | 30000  |
| 4      | D        | 20      | 15000  |
| 5      | E        | 20      | 25000  |
| 6      | F        | 20      | 25000  |
| 7      | G        | 30      | 5000   |
| 8      | H        | 30      | 7000   |

-- Write an SQL query to find the second highest salary for each department.
SELECT dept_id, salary
    FROM (
        SELECT dept_id, salary,
               DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
        FROM employee
        ) t
WHERE rnk = 2;
