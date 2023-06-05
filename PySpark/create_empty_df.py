from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName("Empty Dataframe").getOrCreate()

# create empty RDD
rdd1 = spark.sparkContext.emptyRDD()
print(rdd1)

# create empty RDD using parallelize
rdd2 = spark.sparkContext.parallelize([])
print(rdd2)

# Create Schema
schema = StructType([
    StructField('first name', StringType(), True),
    StructField('Middle Name', StringType(), True),
    StructField('Last Name', StringType(), True)
])

# Create empty DataFrame from empty RDD
df1 = spark.createDataFrame(rdd1, schema)
df1.printSchema()

# Convert empty RDD to Dataframe
df2 = rdd1.toDF(schema)
df2.printSchema()

# Create empty DataFrame directly.
df3 = spark.createDataFrame([], schema)
df3.printSchema()

# Create empty DatFrame with no schema (no columns)
df4 = spark.createDataFrame([], StructType([]))
df4.printSchema()