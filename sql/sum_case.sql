-- sql query to find -ve and +ve sum separetely
t1
2
-2
3
-3
4
-4
5
-5

SELECT
  SUM(CASE WHEN t1 >= 0 THEN t1 ELSE 0 END) AS positive_sum,
  SUM(CASE WHEN t1 < 0 THEN t1 ELSE 0 END) AS negative_sum
FROM t1;
-------------------------------------------------
-- sql query: count null
c1 c2 c3
a   10 null
null 20 null
null null null
b null null
c null  abc

output
c1 c2 c3
2  3   4

SELECT
    SUM(CASE WHEN c1 IS NULL THEN 1 ELSE 0 END) AS c1_null_count,
    SUM(CASE WHEN c2 IS NULL THEN 1 ELSE 0 END) AS c2_null_count,
    SUM(CASE WHEN c3 IS NULL THEN 1 ELSE 0 END) AS c3_null_count
FROM your_table_name;