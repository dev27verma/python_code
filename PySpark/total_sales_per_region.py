'''You are working in a retail analytics company. You have a very large sales dataset (1TB).

Schema: order_id (string) product_id (string) category (string) amount (double) order_date (date) region (string)

Business Requirement: 1. Find total sales per region. 2. One region ("West") has 70% of the data → causing severe data skew.
3. The job is running very slow due to skew during aggregation. 4. Optimize the solution to handle skew properly.'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, rand, concat, lit, floor, split

spark = SparkSession.builder.appName("HandleDataSkew").getOrCreate()

data = [("O1","P1","Electronics",500.0,"2024-03-01","West"), ("O2","P2","Clothing",200.0,"2024-03-01","West"), ("O3","P3","Electronics",800.0,"2024-03-02","West"),
("O4","P4","Furniture",300.0,"2024-03-02","East"), ("O5","P5","Clothing",150.0,"2024-03-03","West"), ("O6","P6","Electronics",1200.0,"2024-03-03","West"),
("O7","P7","Furniture",400.0,"2024-03-03","South"), ("O8","P8","Clothing",250.0,"2024-03-04","West"), ("O9","P9","Electronics",900.0,"2024-03-04","West"),
("O10","P10","Furniture",600.0,"2024-03-04","North")]

df = spark.createDataFrame(data, ["order_id","product_id","category","amount","order_date","region"])

df_salted = df.withColumn("salt", floor(rand()*5)).withColumn("region_salt", concat(col("region"), lit("_"), col("salt")))

partial_agg = df_salted.groupBy("region_salt").agg(sum("amount").alias("partial_total"))

final_df = partial_agg.withColumn("region", split(col("region_salt"), "_")[0]).groupBy("region").agg(sum("partial_total").alias("total_sales"))

final_df.show()