| emp_id | emp_name | manager_id |
| ------ | -------- | ---------- |
| 1      | A        | NULL       |
| 2      | B        | 1          |
| 3      | C        | 1          |
| 4      | D        | 1          |
| 5      | E        | 1          |
| 6      | F        | 1          |
| 7      | G        | 1          |
| 8      | H        | 2          |
| 9      | I        | 2          |
| 10     | J        | 3          |

-- Write an SQL query to find managers having more than 5 subordinates.
SELECT manager_id
FROM employee
WHERE manager_id IS NOT NULL
GROUP BY manager_id
HAVING COUNT(*) > 5;
