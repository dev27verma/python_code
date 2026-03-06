id
--
A
A
B
C
C
C
E

output
id temp
A   1
A   1
C   2
C   2
C   2
B   NULL
E   NULL
-- Write a SQL query to generate a column temp such that:
-- For each group of consecutive identical ids,
-- temp should contain the count of rows in that consecutive group.
-- The same count should be shown for all rows in that group.
SELECT id,
       CASE
           WHEN COUNT(*) OVER (PARTITION BY id) > 1
           THEN COUNT(*) OVER (PARTITION BY id) - 1
           ELSE NULL
       END AS temp
FROM table_id;
