c1 c2                output
1   a                c1   c2
1   b                1    a,b
2   c                2    c

SELECT c1, STRING_AGG(c2, ',') AS c2 FROM your_table GROUP BY c1;




-------------------------------------------------------------------------------
tbl emp
id   name   city
1    aa     hyd
1    aa     mum
2    aa     hyd
2    aa     mum

output
id name city
1   aa  hyd, mum
2   aa  hyd, mum

select id, name, string_agg(distinct city, ", " order by city) as city from emp group by id, name;