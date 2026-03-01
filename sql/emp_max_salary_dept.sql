-- employee having max salary for each dept
-- input table1                             output table1
--    dept emp_id salary                      dept emp_id salary  high
--    cmp   123    2500                       cmp   123    2500   2500
--    eco   456    500                        eco   456    500    4500
--    hist  786    6700                       hist  786    6700   6700
--    comp  564    1400                       comp  564    1400   2500
--    hist  987    3450                       hist  987    3450   6700

SELECT
    e.dept, e.emp_id, e.salary, d.high
FROM employee e
JOIN (
    SELECT
        dept,
        MAX(salary) AS high
    FROM employee
    GROUP BY dept
) d
ON t.dept = d.dept;
---------------------------------
SELECT *
FROM (
    SELECT *,
           RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rnk
    FROM employee
)
WHERE rnk = 1;