 table 1: sales_table                             table 2: product_table
 prod_id order_dt sales_amt                       columns: prod_id  prod_nm
    1    20-08-2024   100                                     1	    cinthol
    4    26-09-2024   150                                     2	     lux
    2    22-08-2024  200                                      3	    Dettol
    4    25-08-2024   450                                     4	    pears
    3    22-08-2024  500
    1    25-08-2024   200
    1    15-08-2025   400
    4    22-09-2025   350

-- write SQL in Bigquery to find top 3 products in terms of total sales amount for each year . Output col should have prod_nm, year and total_sales

WITH yearly_sales AS (
  SELECT
    p.prod_nm, EXTRACT(YEAR FROM s.order_dt) AS year, SUM(s.sales_amt) AS total_sales
  FROM sales_table s JOIN product_table p
    ON s.prod_id = p.prod_id
  GROUP BY prod_nm, year
),
ranked_sales AS (
  SELECT
    *, RANK() OVER (PARTITION BY year ORDER BY total_sales DESC) AS rnk
  FROM yearly_sales
)
SELECT
  prod_nm, year, total_sales
FROM ranked_sales
WHERE rnk <= 3
ORDER BY year, total_sales DESC;