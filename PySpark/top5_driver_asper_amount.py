'''You are working in a ride-sharing company (like Uber/Ola). You receive trip data daily.
Schema: trip_id (string) driver_id (string) city (string) trip_distance (double) fare_amount (double) trip_date (date)
1. Find the top 5 drivers in each city based on total fare_amount. 2. The solution must scale efficiently for hundreds of millions of records.
3. Output should contain: * city * driver_id * total_fare * rank'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, row_number
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("TopDriversPerCity").getOrCreate()

data = [("T1","D1","NY",10.0,500.0,"2024-03-01"), ("T2","D1","NY",15.0,700.0,"2024-03-02"), ("T3","D2","NY",8.0,300.0,"2024-03-01"), ("T4","D3","NY",12.0,900.0,"2024-03-03"),
        ("T5","D2","NY",10.0,400.0,"2024-03-04"), ("T6","D4","LA",20.0,1000.0,"2024-03-01"), ("T7","D5","LA",18.0,800.0,"2024-03-02"), ("T8","D4","LA",15.0,600.0,"2024-03-03"),
        ("T9","D6","LA",25.0,1200.0,"2024-03-04"), ("T10","D7","LA",10.0,300.0,"2024-03-05")]

df = spark.createDataFrame(data, ["trip_id","driver_id","city","trip_distance","fare_amount","trip_date"])

# Step 1: Aggregate total fare per driver per city
df_agg = df.groupBy("city","driver_id").agg(_sum("fare_amount").alias("total_fare"))

# Step 2: Window for ranking
w = Window.partitionBy("city").orderBy(col("total_fare").desc())

# Step 3: Rank and filter top 5
result_df = df_agg.withColumn("rank", row_number().over(w)).filter(col("rank") <= 5)

result_df.show()