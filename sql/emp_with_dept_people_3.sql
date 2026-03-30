| emp_id | emp_name | dept_id |
| ------ | -------- | ------- |
| 1      | A        | 10      |
| 2      | B        | 10      |
| 3      | C        | 20      |
| 4      | D        | 20      |
| 5      | E        | 20      |
| 6      | F        | 30      |
| 7      | G        | 40      |
| 8      | H        | 40      |
| 9      | I        | 50      |

-- Write an SQL query to find employees who belong to departments having less than 3 employees.
SELECT emp_id, emp_name, dept_id
FROM employee
WHERE dept_id IN (
                    SELECT dept_id
                        FROM employee
                        GROUP BY dept_id
                        HAVING COUNT(*) < 3
                  );
