| emp_id | emp_name | join_date  |
| ------ | -------- | ---------- |
| 1      | A        | 2025-10-10 |
| 2      | B        | 2025-11-05 |
| 3      | C        | 2025-12-01 |
| 4      | D        | 2025-09-20 |
| 5      | E        | 2025-08-15 |
| 6      | F        | 2024-12-10 |
| 7      | G        | 2025-01-25 |
| 8      | H        | 2025-02-14 |
| 9      | I        | 2025-03-30 |
| 10     | J        | 2025-04-18 |
| 11     | K        | 2025-05-22 |
| 12     | L        | 2025-06-11 |
| 13     | M        | 2025-07-09 |
| 14     | N        | 2025-08-01 |
| 15     | O        | 2025-09-28 |

-- Write an SQL query to list all employees hired in the last 6 months.
SELECT emp_id, emp_name, join_date
FROM employee
WHERE join_date >= CURRENT_DATE - INTERVAL '6 months';
