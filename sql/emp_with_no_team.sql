| emp_id | emp_name | manager_id |
| ------ | -------- | ---------- |
| 1      | A        | NULL       |
| 2      | B        | 1          |
| 3      | C        | 1          |
| 4      | D        | 2          |
| 5      | E        | 2          |
| 6      | F        | 3          |
| 7      | G        | 3          |
| 8      | H        | 4          |
| 9      | I        | 4          |
| 10     | J        | 5          |
| 11     | K        | 6          |
| 12     | L        | 7          |
| 13     | M        | 8          |
| 14     | N        | 9          |
| 15     | O        | 10         |

-- Write an SQL query to find employees who do not have any subordinates.
SELECT e.emp_id, e.emp_name
FROM employee e
LEFT JOIN employee s
ON e.emp_id = s.manager_id
WHERE s.emp_id IS NULL;
