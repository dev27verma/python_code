| emp_id | emp_name | dept_id | join_date  |
| ------ | -------- | ------- | ---------- |
| 1      | A        | 10      | 2022-01-10 |
| 2      | B        | 10      | 2021-06-15 |
| 3      | C        | 20      | 2025-01-20 |
| 4      | D        | 20      | 2024-03-05 |
| 5      | E        | 30      | 2021-02-01 |
| 6      | F        | 30      | 2020-07-25 |
| 7      | G        | 40      | 2023-09-12 |

-- Write an SQL query to find employees in departments that have not hired anyone in the last 2 years.
SELECT emp_id, emp_name, dept_id
FROM employee
WHERE dept_id IN (
                    SELECT dept_id
                    FROM employee
                    GROUP BY dept_id
                    HAVING MAX(join_date) <= CURRENT_DATE - INTERVAL '2 years'
                 );
