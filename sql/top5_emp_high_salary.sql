| emp_id | salary |
| ------ | ------ |
| 1      | 100    |
| 2      | 200    |
| 3      | 300    |
| 4      | 250    |
| 5      | 150    |
| 6      | 400    |
| 7      | 350    |

-- Write an SQL query to retrieve the top 5 employees who have the highest salaries from the table.

SELECT emp_id, salary
FROM employee
ORDER BY salary DESC
LIMIT 5;