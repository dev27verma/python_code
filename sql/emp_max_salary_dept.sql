-- employee having max salary for each dept
 input employee                             output employee
    dept emp_id salary                      dept emp_id salary  high
    cmp   123    2500                       cmp   123    2500   2500
    eco   456    500                        eco   456    500    4500
    hist  786    6700                       hist  786    6700   6700
    comp  564    1400                       comp  564    1400   2500
    hist  987    3450                       hist  987    3450   6700

SELECT
    dept,
    emp_id,
    salary,
    MAX(salary) OVER (PARTITION BY dept) AS high
FROM employee;