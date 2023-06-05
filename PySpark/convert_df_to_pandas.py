from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.appName("Convert DF to Pandas").getOrCreate()

# prepare pyspark dataframe
data = [("James", "", "Smith", "36636", "M", 60000),
        ("Michael", "Rose", "", "40288", "M", 70000),
        ("Robert", "", "Williams", "42114", "", 400000),
        ("Maria", "Anne", "Jones", "39192", "F", 500000),
        ("Jen", "Mary", "Brown", "", "F", 0)]

schema = StructType([
    StructField("first_name", StringType(), True),
    StructField("middle_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("DOB", StringType(), True),
    StructField("Gender", StringType(), True),
    StructField("Salary", IntegerType(), True)
])

df1 = spark.createDataFrame(data, schema)
df1.show(truncate=False)

# convert to pandas

p1 = df1.toPandas()
print(p1)

# Nested structure elements
dataStruct = [(("James", "", "Smith"), "36636", "M", "3000"),
              (("Michael", "Rose", ""), "40288", "M", "4000"),
              (("Robert", "", "Williams"), "42114", "M", "4000"),
              (("Maria", "Anne", "Jones"), "39192", "F", "4000"),
              (("Jen", "Mary", "Brown"), "", "F", "-1")
              ]

schemaStruct = StructType([
    StructField('name', StructType([
        StructField('firstname', StringType(), True),
        StructField('middlename', StringType(), True),
        StructField('lastname', StringType(), True)
    ])),
    StructField('dob', StringType(), True),
    StructField('gender', StringType(), True),
    StructField('salary', StringType(), True)
])
df = spark.createDataFrame(data=dataStruct, schema=schemaStruct)
df.printSchema()

pandasDF2 = df.toPandas()
print(pandasDF2)
