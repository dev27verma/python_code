-- delete duplicate rows:
DELETE FROM table_name
WHERE id IN (
    SELECT id
    FROM (
        SELECT id,
               ROW_NUMBER() OVER (
                   ORDER BY id
               ) AS rn
        FROM table_name)
    t
    WHERE rn > 1
);

DELETE t1
FROM table_name t1
JOIN table_name t2
  ON t1.id > t2.id;
-------------------------------------------------------
-- SQL query to get duplicate
SELECT column_name, COUNT(column_name) AS duplicate_count
FROM table_name
GROUP BY column_name
HAVING COUNT(column_name) > 1;

-----------------------------------------------------------
-- sql query to find duplicate in two tables with output
table 1
c1 c2
1      a
2      b
2      c

table 2
c1    c2
1        a
2       b
4       d

SELECT t1.c1, t1.c2
FROM table1 t1
INNER JOIN table2 t2 ON t1.c1 = t2.c1 AND t1.c2 = t2.c2
GROUP BY t1.c1, t1.c2
HAVING COUNT(*) > 1;