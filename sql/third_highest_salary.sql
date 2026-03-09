-- third highest salary

select * from employees where salary = (select distinct(salary) from employees order by salary desc limit 1 offset 2)

---------------------------------------------
-- if two three employee having same salary and we want distinct salary amount
SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk = 3;