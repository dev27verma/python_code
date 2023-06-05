from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data = [("James", "Smith", "USA", "CA"),
        ("Michael", "Rose", "USA", "NY"),
        ("Robert", "Williams", "USA", "CA"),
        ("Maria", "Jones", "USA", "FL")
        ]

columns = ["first_name", "last_name", "country", "state"]
df = spark.createDataFrame(data=data, schema=columns)
df.show(truncate=False)

df.select("first_name").show()

df.select("first_name", "last_name").show()

# Using Dataframe object name
df.select(df.first_name, df.last_name).show()

# Using col function
df.select(col("first_name"), col("last_name")).show()

data = [(("James", None, "Smith"), "OH", "M"),
        (("Anna", "Rose", ""), "NY", "F"),
        (("Julia", "", "Williams"), "OH", "F"),
        (("Maria", "Anne", "Jones"), "NY", "M"),
        (("Jen", "Mary", "Brown"), "NY", "M"),
        (("Mike", "Mary", "Williams"), "OH", "M")
        ]

schema = StructType([
    StructField('name', StructType([
        StructField('first_name', StringType(), True),
        StructField('middle_name', StringType(), True),
        StructField('last_name', StringType(), True)
    ])),
    StructField('state', StringType(), True),
    StructField('gender', StringType(), True)
])

df2 = spark.createDataFrame(data=data, schema=schema)
df2.printSchema()
df2.show(truncate=False)  # shows all columns

df2.select("name").show(truncate=False)
df2.select("name.first_name", "name.last_name").show(truncate=False)
df2.select("name.*").show(truncate=False)