'''
Input = '{"dept_id":101,"e_id":[10101,10102,10103]} {"dept_id":102,"e_id":[10201,10202]}'

output:
101 | 10101
101 | 10102
101 | 10103
102 | 10201
102 | 10202
'''
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, ArrayType
from pyspark.sql.functions import explode

# Create Spark Session
spark = SparkSession.builder.appName("DeptEmployeeExample").getOrCreate()

# Sample input data (as given)
data = [
    '{"dept_id":101,"e_id":[10101,10102,10103]}',
    '{"dept_id":102,"e_id":[10201,10202]}'
]

# Define schema using StructType
schema = StructType([
    StructField("dept_id", IntegerType(), True),
    StructField("e_id", ArrayType(IntegerType()), True)
])

# Create DataFrame from JSON strings using schema
df = spark.read.schema(schema).json(spark.sparkContext.parallelize(data))

print("Original DataFrame:")
df.show(truncate=False)

# Explode the array column
final_df = df.select("dept_id", explode("e_id").alias("e_id"))

print("Final Output:")
final_df.show()