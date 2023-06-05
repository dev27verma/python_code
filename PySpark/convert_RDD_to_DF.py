from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName("Convert RDD To DF").getOrCreate()

# create RDD
dept = [("Finance", 10), ("Marketing", 20), ("Sales", 30), ("IT", 40)]
rdd = spark.sparkContext.parallelize(dept)

# convert pyspark RDD to DF
df1 = rdd.toDF()
df1.printSchema()
df1.show(truncate=False)

# with Schema

dept_column = ['dept_name', 'dept_id']
df1 = rdd.toDF(dept_column)
df1.printSchema()
df1.show(truncate=False)

# Using PySpark createDataFrame() function
dept_df = spark.createDataFrame(rdd, dept_column)
dept_df.show()

deptSchema = StructType([
    StructField('dept_name', StringType(), True),
    StructField('dept_id', StringType(), True)
])

deptDF1 = spark.createDataFrame(rdd, schema=deptSchema)
deptDF1.printSchema()
deptDF1.show(truncate=False)
