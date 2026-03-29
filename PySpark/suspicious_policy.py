'''You are working in a fintech company detecting fraudulent transactions. You receive transaction data daily.
Schema: transaction_id (string) customer_id (string) transaction_time (timestamp) amount (double) location (string) device_id (string)

1. Identify suspicious transactions where: * A customer performs 2 transactions within 5 minutes  * From different locations
2. Dataset size: 600M+ records. 3. Must be scalable and optimized. 4. Output suspicious transaction pairs.'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lag, to_timestamp
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("FraudDetection").getOrCreate()

data = [("T1","C1","2024-03-01 10:00:00",500.0,"NY","D1"), ("T2","C1","2024-03-01 10:03:00",700.0,"LA","D2"),
        ("T3","C1","2024-03-01 11:00:00",300.0,"NY","D1"), ("T4","C2","2024-03-01 09:00:00",1000.0,"SF","D3"), ("T5","C2","2024-03-01 09:04:00",1200.0,"SF","D3")]

df = spark.createDataFrame(data, ["transaction_id","customer_id","transaction_time","amount","location","device_id"])

# FIX: convert to timestamp
df = df.withColumn("transaction_time", to_timestamp(col("transaction_time")))

w = Window.partitionBy("customer_id").orderBy("transaction_time")

df_flag = (df.withColumn("prev_time", lag("transaction_time").over(w)).withColumn("prev_location", lag("location").over(w))
           .withColumn("time_diff", (col("transaction_time").cast("long") - col("prev_time").cast("long"))/60))

result_df = df_flag.filter((col("time_diff") <= 5) & (col("location") != col("prev_location")))

result_df.select("customer_id","transaction_id","prev_time","transaction_time","prev_location","location").show()