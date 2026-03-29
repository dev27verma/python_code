'''You have a PySpark DataFrame `sales_data` with the following schema:

| Column Name | Type |
| -------------- | ------------------- |
| `region` | string |
| `product` | string |
| `sales_amount` | double |
| `sales_date` | string (yyyy-MM-dd) |

Your manager wants you to generate a monthly sales summary report with the following requirements:
1. Convert `sales_date` to proper DateType. 2. Extract `year` and `month`. 3. Calculate total_sales, average_sales, and number_of_orders per `region`, `product`, `year`, and `month`.
4. Output the result sorted by `region`, `year`, and `month`.'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, year, month, sum as _sum, avg, count

spark = SparkSession.builder.appName("Monthly_Sales_Summary").getOrCreate()

data = [("North","Laptop",1200.0,"2024-03-01"), ("North","Laptop",800.0,"2024-03-15"), ("South","Mobile",500.0,"2024-03-10"), ("South","Mobile",700.0,"2024-04-05"),
("North","Laptop",1000.0,"2024-04-10"), ("East","Tablet",300.0,"2024-03-20")]

df = spark.createDataFrame(data, ["region","product","sales_amount","sales_date"])

# Convert date + extract year/month + aggregate + sort
result_df = (df.withColumn("sales_date", to_date(col("sales_date"), "yyyy-MM-dd")).withColumn("year", year(col("sales_date")))
             .withColumn("month", month(col("sales_date"))).groupBy("region","product","year","month").agg(_sum("sales_amount")
             .alias("total_sales"), avg("sales_amount").alias("avg_sales"), count("*").alias("number_of_orders")).orderBy("region","year","month"))

result_df.show()