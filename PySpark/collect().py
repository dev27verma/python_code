from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

dept = [("Finance",10), ("Marketing",20), ("Sales",30), ("IT",40)]
deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(dept, deptColumns)
deptDF.show(truncate=False)

# collect all data
dataCollect = deptDF.collect()
print(dataCollect)

# collect only dept_name data
dataCollect2 = deptDF.select("dept_name").collect()
print(dataCollect2)

for row in dataCollect:
    print(row['dept_name'] + "," +str(row['dept_id']))