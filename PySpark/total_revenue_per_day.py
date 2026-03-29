'''
You are working as a Data Engineer in an e-commerce company. You receive daily transaction data in CSV format with the following schema:
transaction_id (string) customer_id (string) product_id (string) quantity (integer) price (double) transaction_date (string)

You are asked to:
1. Load the CSV data into PySpark.
2. Remove duplicate transactions based on `transaction_id`.
3. Filter out records where `quantity <= 0` or `price <= 0`.
4. Create a new column `total_amount = quantity * price`.
5. Find total revenue per day.
6. Store the result in Parquet format partitioned by `transaction_date`.

How would you implement this in PySpark?
'''


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# create data file transaction.csv
data = """transaction_id,customer_id,product_id,quantity,price,transaction_date
T001,C001,P001,2,500.0,2026-03-25
T002,C002,P002,1,1200.5,2026-03-25
T003,C001,P003,3,250.0,2026-03-25
T004,C003,P001,0,500.0,2026-03-26
T005,C004,P004,5,0.0,2026-03-26
T006,C002,P002,2,1200.5,2026-03-26
T007,C005,P005,1,700.0,2026-03-26
T008,C001,P001,2,500.0,2026-03-25
T009,C006,P006,4,150.75,2026-03-27
T010,C007,P007,1,999.99,2026-03-27
T002,C002,P002,1,1200.5,2026-03-25
"""
#write the actual file to location
with open("transactions.csv", "w") as f:
    f.write(data)

# 1. Create Spark Session
spark = SparkSession.builder.appName("total revenue").getOrCreate()

# 2. Load CSV Data
df = spark.read.option("header", "true").option("inferSchema", "true").csv("transactions.csv")

# 3. Remove duplicate transactions based on transaction_id
df_dedup = df.dropDuplicates(["transaction_id"])

# 4. Filter invalid records (quantity <= 0 or price <= 0)
df_filtered = df_dedup.filter((col("quantity") > 0) & (col("price") > 0))

# 5. Create total_amount column
df_transformed = df_filtered.withColumn("total_amount", col("quantity") * col("price"))

# 6. Calculate total revenue per day
df_daily_revenue = df_transformed.groupBy("transaction_date").agg(sum("total_amount").alias("total_revenue"))

df_daily_revenue.show()

# 7. Write output to Parquet partitioned by transaction_date   ----> not working because of permission issue to hadoop
# df_daily_revenue.write.mode("overwrite").partitionBy("transaction_date").parquet("output/")
df_daily_revenue.write.mode("overwrite").csv("output_csv/")
# df_daily_revenue.write.mode("overwrite").json("output_json/")
# df_daily_revenue.toPandas().to_csv("output.csv", index=False)