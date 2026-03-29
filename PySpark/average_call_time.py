'''You are working in a large telecom company. You receive customer usage logs that contain daily data.
Dataset: usage_logs (1.2 billion records)
id="ukdncu" customer_id (string) usage_mb (double) call_minutes (double) sms_count (int) event_date (date) circle (string) -- region
1. For each customer, compute a 30-day rolling average of: * usage_mb * call_minutes * sms_count
2. Rolling window must be based on event_date. 3. Data is huge → must be optimized.
4. Final output should contain: ```id="itklb7" customer_id  event_date avg_usage_30d avg_call_minutes_30d avg_sms_30d '''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, round
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("RollingAverage30Days").getOrCreate()

data = [("C1",500.0,30.0,10,"2024-03-01","North"), ("C1",700.0,40.0,15,"2024-03-05","North"),
("C1",600.0,35.0,12,"2024-03-20","North"), ("C1",800.0,50.0,20,"2024-04-01","North"),
("C2",300.0,20.0,5,"2024-03-02","South"), ("C2",400.0,25.0,8,"2024-03-10","South")]

df = spark.createDataFrame(data, ["customer_id","usage_mb","call_minutes","sms_count","event_date","circle"])

w = Window.partitionBy("customer_id").orderBy(col("event_date").cast("timestamp").cast("long")).rangeBetween(-30*86400, 0)

result_df = (df.withColumn("avg_usage_30d", round(avg("usage_mb").over(w), 2)).withColumn("avg_call_minutes_30d", round(avg("call_minutes").over(w), 2))
             .withColumn("avg_sms_30d", round(avg("sms_count").over(w), 2)).select("customer_id","event_date","avg_usage_30d","avg_call_minutes_30d","avg_sms_30d"))

result_df.show()