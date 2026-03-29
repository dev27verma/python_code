'''You are working in an e-commerce analytics platform. You receive a product catalog dataset and sales dataset.
1️⃣ products (2M records) product_id (string) product_name (string) category (string) price (double)
2️⃣ sales (900M records) sale_id (string) product_id (string) quantity (integer) sale_date (date)
1. Find total quantity sold per category per day. 2. The sales table is extremely large. 3. Join should be optimized.
4. Output should contain: sale_date category total_quantity'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, broadcast

spark = SparkSession.builder.appName("sales_per_day").getOrCreate()

products_data = [("P1","iPhone","Electronics",800.0), ("P2","Shirt","Clothing",50.0), ("P3","Laptop","Electronics",1200.0), ("P4","Shoes","Footwear",100.0)]

sales_data = [("S1","P1",2,"2024-03-01"), ("S2","P2",5,"2024-03-01"), ("S3","P1",1,"2024-03-02"), ("S4","P3",3,"2024-03-02"), ("S5","P4",4,"2024-03-02")]

products_df = spark.createDataFrame(products_data, ["product_id","product_name","category","price"])
sales_df = spark.createDataFrame(sales_data, ["sale_id","product_id","quantity","sale_date"])

# Select only required columns (column pruning)
products_small = products_df.select("product_id","category")

# Optimized join (broadcast small table)
joined_df = sales_df.join(broadcast(products_small), "product_id")

# Aggregate
result_df = joined_df.groupBy("sale_date","category").agg(_sum("quantity").alias("total_quantity"))

result_df.show()