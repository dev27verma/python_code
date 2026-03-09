--- column is having 1 2 5 6 8 9
--- find the missing number



-- Creates a temporary result set called numbers
-- Simply selects the column num from your actual table
WITH numbers AS (
  SELECT num FROM your_table
),
-- BigQuery, GENERATE_ARRAY() is used to create a complete numeric sequence between two values in this case 1-10.
-- SELECT MIN(num) FROM numbers --> find starting range limit
-- SELECT MAX(num) FROM numbers --> find ending range limit
-- UNNEST() converts the array into rows 1 2 3 4 5 6 7 8 9 10
full_range AS (
  SELECT num
  FROM UNNEST(GENERATE_ARRAY(
      (SELECT MIN(num) FROM numbers),
      (SELECT MAX(num) FROM numbers)
  )) AS num
)
-- We remove numbers that already exist in the original table.
SELECT num AS missing_number
FROM full_range
WHERE num NOT IN (SELECT num FROM numbers)
ORDER BY num;


--“First I find the min and max values,
-- generate the full numeric sequence using GENERATE_ARRAY,
-- then subtract the existing values using anti-join logic.
-- The remaining rows are the missing numbers.”