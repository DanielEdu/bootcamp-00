# Databricks notebook source
# MAGIC %md
# MAGIC ### DataFrame de productos con schema explícito
# MAGIC Compatible con Databricks Runtime 16.x (Spark 3.5+)

# COMMAND ----------

from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DecimalType,
    BooleanType,
)
from decimal import Decimal

schema_productos = StructType([
    StructField("id_producto", IntegerType(), nullable=False),
    StructField("nombre", StringType(), nullable=False),
    StructField("categoria", StringType(), nullable=True),
    StructField("precio", DecimalType(10, 2), nullable=False),
    StructField("stock", IntegerType(), nullable=True),
    StructField("activo", BooleanType(), nullable=True),
])

data_productos = [
    (1, "Laptop 14''",       "Electrónica",  Decimal("899.99"), 25,  True),
    (2, "Mouse Inalámbrico", "Electrónica",  Decimal("19.90"),  150, True),
    (3, "Silla Ergonómica",  "Oficina",      Decimal("149.50"), 40,  True),
    (4, "Escritorio Ajustable", "Oficina",   Decimal("299.00"), 10,  False),
    (5, "Monitor 27''",      "Electrónica",  Decimal("259.99"), 60,  True),
]

df_productos = spark.createDataFrame(data_productos, schema=schema_productos)

# COMMAND ----------

df_productos.printSchema()

# COMMAND ----------

display(df_productos)
