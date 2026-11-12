# Databricks notebook source
# MAGIC %run "/masterclassdatabricks/Tutorial1"

# COMMAND ----------

# MAGIC %md
# MAGIC # DELTA LAKE

# COMMAND ----------

df_sales.write.format('delta')\
    .mode('append')\
    .option('path','abfss://destination@datbricksaz.dfs.core.windows.net/sales')\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #Managed Table

# COMMAND ----------

# MAGIC %sql
# MAGIC create database salesDB;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC create table salesDB.mantable (
# MAGIC     id int,
# MAGIC     name string,
# MAGIC     marks int
# MAGIC )
# MAGIC USING DELTA

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC insert into salesDB.mantable values
# MAGIC (1,'aa',30),
# MAGIC (2,'bb',40),
# MAGIC (3,'cc',50),
# MAGIC (4,'dd',60)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from salesDB.mantable

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table salesDB.mantable;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDB.mantable

# COMMAND ----------

# MAGIC %md
# MAGIC #External Table
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create table salesdb.exttable(
# MAGIC     id int,
# MAGIC     name string,
# MAGIC     marks int
# MAGIC )
# MAGIC using delta
# MAGIC location 'abfss://destination@datbricksaz.dfs.core.windows.net/salesdb/exxtable'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC insert into salesdb.exttable values
# MAGIC (1,'aa',30),
# MAGIC (2,'bb',40),
# MAGIC (3,'cc',50),
# MAGIC (4,'dd',60)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from salesdb.exttable

# COMMAND ----------

# MAGIC %md
# MAGIC ## DELTA TABLES FUNCTIONALITIES
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into salesdb.exttable values
# MAGIC (5,'aa',30),
# MAGIC (6,'bb',40),
# MAGIC (7,'cc',50),
# MAGIC (8,'dd',60)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM salesdb.exttable

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from salesdb.exttable where id=8

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC describe history salesdb.exttable

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #Timetravel
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC restore table salesdb.exttable to version as of 2

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from salesdb.exttable

# COMMAND ----------

# MAGIC %md
# MAGIC #Delta table optimisation
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC optimize salesdb.exttable

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesdb.exttable

# COMMAND ----------

# MAGIC %md
# MAGIC #Z ORDER BY
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE salesdb.exttable ZORDER BY (id)
# MAGIC     

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesdb.exttable

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC #AUTOLOADER

# COMMAND ----------

# MAGIC %md
# MAGIC ## streaming dataframe
# MAGIC

# COMMAND ----------

df = spark.readStream.format('cloudFiles')\
    .option('cloudFiles.format','parquet')\
    .option('cloudFiles.schemaLocation','abfss://aldestination@datbricksaz.dfs.core.windows.net/checkpoint')\
    .load('abfss://alsource@datbricksaz.dfs.core.windows.net')

# COMMAND ----------

df.writeStream.format('delta')\
    .option('checkpointLocation','abfss://aldestination@datbricksaz.dfs.core.windows.net/checkpoint')\
    .trigger(processingTime='5 seconds')\
    .start('abfss://aldestination@datbricksaz.dfs.core.windows.net/data')


# COMMAND ----------

# MAGIC %sql
# MAGIC show external locations