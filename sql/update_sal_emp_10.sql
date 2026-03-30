| emp_id | emp_name | salary |
| ------ | -------- | ------ |
| 1      | A        | 10000  |
| 2      | B        | 20000  |
| 3      | C        | 30000  |
| 4      | D        | 25000  |
| 5      | E        | 15000  |

-- Write an SQL query to update the salary of all employees by 10%.
UPDATE employee
SET salary = salary * 1.10;
