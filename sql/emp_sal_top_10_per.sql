| emp_id | emp_name | salary |
| ------ | -------- | ------ |
| 1      | A        | 10000  |
| 2      | B        | 20000  |
| 3      | C        | 30000  |
| 4      | D        | 40000  |
| 5      | E        | 50000  |
| 6      | F        | 60000  |
| 7      | G        | 70000  |
| 8      | H        | 80000  |
| 9      | I        | 90000  |
| 10     | J        | 100000 |

-- Write an SQL query to find employees whose salary is in the top 10%.
SELECT emp_id, emp_name, salary
FROM (
      SELECT emp_id, emp_name, salary,
           NTILE(10) OVER (ORDER BY salary DESC) AS bucket
      FROM employee
    ) t
WHERE bucket = 1;
