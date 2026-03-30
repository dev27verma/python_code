| emp_id | emp_name | manager_id | join_date  |
| ------ | -------- | ---------- | ---------- |
| 1      | A        | NULL       | 2020-01-10 |
| 2      | B        | 1          | 2020-01-15 |
| 3      | C        | 1          | 2021-03-20 |
| 4      | D        | 2          | 2020-01-25 |
| 5      | E        | 2          | 2022-05-10 |
| 6      | F        | 3          | 2021-03-05 |
| 7      | G        | 3          | 2021-04-12 |
| 8      | H        | 4          | 2020-01-30 |
| 9      | I        | 5          | 2022-05-18 |
| 10     | J        | 6          | 2021-03-25 |

-- Write an SQL query to find employees who joined in the same month and year as their manager.
SELECT e.emp_id, e.emp_name
FROM employee e
JOIN employee m
ON e.manager_id = m.emp_id
WHERE
    EXTRACT(YEAR FROM e.join_date) = EXTRACT(YEAR FROM m.join_date)
    AND EXTRACT(MONTH FROM e.join_date) = EXTRACT(MONTH FROM m.join_date);
