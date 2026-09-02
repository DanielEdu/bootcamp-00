# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# Lectura del CSV desde S3
s3_path = "s3://lakehouse-datawizard/landing/dim_clientes_s06.csv"

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("sep", ",") \
    .csv(s3_path)

df.display()