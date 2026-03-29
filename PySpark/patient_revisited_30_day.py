'''You are working in a healthcare analytics company. You receive patient visit records daily.

Schema: patient_id (string) visit_date (date) diagnosis (string) hospital_id (string) bill_amount (double)

Business Requirement: 1. For each patient, calculate the difference in days between consecutive visits. 2. Identify patients who revisited within 30 days.
3. The dataset is very large (500M+ records). 4. Solution must be scalable and optimized.'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lag, datediff
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("PatientRevisitAnalysis").getOrCreate()

data = [("P1","2024-03-01","Flu","H1",500.0), ("P1","2024-03-20","Cold","H1",300.0), ("P1","2024-05-01","Checkup","H2",700.0),
("P2","2024-03-05","Infection","H2",800.0), ("P2","2024-04-10","Followup","H2",400.0), ("P3","2024-03-10","Surgery","H3",5000.0), ("P3","2024-03-25","Review","H3",600.0)]

df = spark.createDataFrame(data, ["patient_id","visit_date","diagnosis","hospital_id","bill_amount"])

# Window for each patient ordered by visit_date
w = Window.partitionBy("patient_id").orderBy("visit_date")

# Calculate previous visit and difference
df_diff = df.withColumn("prev_visit_date", lag("visit_date").over(w)).withColumn("days_diff", datediff(col("visit_date"), col("prev_visit_date")))

# Filter patients revisiting within 30 days
result_df = df_diff.filter(col("days_diff") <= 30)

result_df.show()