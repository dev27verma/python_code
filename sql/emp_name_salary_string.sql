| emp_id | emp_name | salary |
| ------ | -------- | ------ |
| 1      | A        | 10000  |
| 2      | B        | 20000  |
| 3      | C        | 30000  |
| 4      | D        | 25000  |
| 5      | E        | 15000  |

-- Write an SQL query to retrieve employee name and salary as a single string.
SELECT CONCAT(emp_name, ' - ', salary) AS emp_details
FROM employee;
