-- third highest salary

select * from salary where amount = (select distinct(amount) from salary order by amount desc limit 1 offset 2) limit 1

---------------------------------------------
-- if two three employee having same salary and we want distinct salary amount
SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk = 3;