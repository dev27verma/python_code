| emp_id | salary |
| ------ | ------ |
| 1      | 100    |
| 2      | 200    |
| 3      | 300    |
| 4      | 250    |
| 5      | 300    |

-- find second highest salary
select max(salary) from employee where salary < (select max(salary) from employee)


-- using window function
SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employee
) t
WHERE rnk = 2;


-- using window function nth highest salary
SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employee
) t
WHERE rnk = n;