--- column is having 1,2,5,6,8,9
--- find the missing number



WITH numbers AS (
  SELECT num FROM your_table
),
full_range AS (
  SELECT num
  FROM UNNEST(GENERATE_ARRAY(
      (SELECT MIN(num) FROM numbers),
      (SELECT MAX(num) FROM numbers)
  )) AS num
)
SELECT num AS missing_number
FROM full_range
WHERE num NOT IN (SELECT num FROM numbers)
ORDER BY num;
