from pyspark.sql import functions as F, SparkSession

# start sparksession
spark = (
    SparkSession.builder
        .appName("clean_code_release")
            .master("local[*]")
                .getOrCreate()
)

# this conf ref: https://sparkbyexamples.com/spark/spark-stop-info-and-debug-logging-console/
spark.sparkContext.setLogLevel("ERROR")

# create sample data
print("[INFO] Sample data\n")

data = [
    {
	    "client.id": "1",
	    "client.name": "Mary"
    },
    {
	    "client.id": "2",
	    "client.name": "Anna"
    }
]

dataframe = spark.createDataFrame(data)
dataframe.show()

# withColumns feature
print("[INFO] Add multiple columns: withColumns (new in release 3.3.0)\n")

new_columns = {
    "client.country": F.lit("USA"),
    "client.job": F.lit("Data Engineer")
}

print("[INFO] new_columns dict:\n", new_columns, "\n")

dataframe = dataframe.withColumns(new_columns)
dataframe.show()

# withColumnsRenamed feature
print("[INFO] Rename multiple columns: withColumnsRenamed (new in release 3.4.0)\n")

columns_renamed = {column: column.replace(".", "_") for column in dataframe.columns}

print("[INFO] columns_renamed dict\n", columns_renamed, "\n")

dataframe = dataframe.withColumnsRenamed(columns_renamed)
dataframe.show()

# isEmpty feature
print("[INFO] Empty dataframe check: dataframe.isEmpty() (new in release 3.3.0)\n")
print("dataframe is empty?\n", dataframe.isEmpty())
