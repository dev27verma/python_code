| emp_id | salary |
| ------ | ------ |
| 1      | 100    |
| 2      | 200    |
| 3      | 300    |
| 4      | 250    |
| 5      | 150    |

-- Write an SQL query to find all employees whose salary is greater than the average salary of all employees.
SELECT emp_id, salary
FROM employee
WHERE salary > (SELECT AVG(salary) FROM employee);

-- window function
SELECT emp_id, salary
FROM (
    SELECT emp_id,
           salary,
           AVG(salary) OVER () AS avg_salary
    FROM employee
) t
WHERE salary > avg_salary;
