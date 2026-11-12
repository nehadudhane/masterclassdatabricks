# Databricks notebook source
# MAGIC %md
# MAGIC # Databricks Masterclass

# COMMAND ----------

mydata = [(1,'aa',30),(2,'bb',40),(3,'cc',50)]

myschema = "id int, name string, marks int"

df = spark.createDataFrame(mydata,schema=myschema)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

# COMMAND ----------

display(df)

# COMMAND ----------



# spark.conf.set("fs.azure.account.auth.type.datbricksaz.dfs.core.windows.net", "OAuth")
# spark.conf.set("fs.azure.account.oauth.provider.type.datbricksaz.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
# spark.conf.set("fs.azure.account.oauth2.client.id.datbricksaz.dfs.core.windows.net", "a5f0af78-4b2c-4ca1-9170-696c177b1c33")
# spark.conf.set("fs.azure.account.oauth2.client.secret.datbricksaz.dfs.core.windows.net", "REDACTED_FOR_PUBLIC_REPOSITORY")
# spark.conf.set("fs.azure.account.oauth2.client.endpoint.datbricksaz.dfs.core.windows.net", "https://login.windows.net/5df7bfe8-c66e-4465-9a6b-7636fd5c6dd8/oauth2/token")

datalake_path="abfss://destination@datbricksaz.dfs.core.windows.net/"

# COMMAND ----------

dbutils.fs.ls(datalake_path)

# COMMAND ----------

dbutils.widgets.text("file_path","neha")

# COMMAND ----------

dbutils.secrets.list(scope='nehascope')

# COMMAND ----------

dbutils.secrets.get(scope='nehascope',key='app-secret')

# COMMAND ----------

# MAGIC %md
# MAGIC # Data Reading
# MAGIC

# COMMAND ----------

df_sales = spark.read.format('csv')\
            .option('header', True)\
            .option('inferSchema', True)\
            .load('abfss://source@datbricksaz.dfs.core.windows.net/')

# COMMAND ----------

df_sales.display()

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------


 df_sales.withColumn('Item_Type', split(col('Item_Type'), ' ')).display()


# COMMAND ----------

dbutils.widgets.text("name" ,"neha")


# COMMAND ----------

var = dbutils.widgets.get('name')

# COMMAND ----------

var

# COMMAND ----------

df_sales.withColumn('flag' , lit(var)).display()

# COMMAND ----------

df_sales.withColumn('Item_Visibility', col('Item_Visibility').cast(StringType())).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###