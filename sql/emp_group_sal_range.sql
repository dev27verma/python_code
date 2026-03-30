| emp_id | emp_name | salary |
| ------ | -------- | ------ |
| 1      | A        | 10000  |
| 2      | B        | 20000  |
| 3      | C        | 30000  |
| 4      | D        | 45000  |
| 5      | E        | 60000  |
| 6      | F        | 75000  |
| 7      | G        | 90000  |
| 8      | H        | 120000 |

-- Write an SQL query to group employees by salary range.
SELECT
    CASE
        WHEN salary < 20000 THEN 'Below 20K'
        WHEN salary BETWEEN 20000 AND 50000 THEN '20K-50K'
        WHEN salary BETWEEN 50001 AND 80000 THEN '50K-80K'
        ELSE '80K+'
    END AS salary_range, COUNT(*) AS emp_count
FROM employee
GROUP BY salary_range;
