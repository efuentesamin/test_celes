from fastapi import APIRouter
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


spark = SparkSession.builder \
    .appName("Playing-With-Celes-Data") \
    .getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("WARN")

df = spark.read.parquet('./data')

router = APIRouter()


@router.get('/by_employee/{employee_id}')
def sales_by_employee(
    employee_id: str,
    init_date: str = '2023-10-03',
    end_date: str = '2023-11-30',
    page: int = 1, size: int = 10
):
    offset = size * (page - 1)
    dates = (init_date, end_date)
    results = df.select('KeySale', 'KeyDate', 'Amount') \
        .filter((col('KeyEmployee') == employee_id) & (col('KeyDate').between(*dates))) \
        .orderBy(desc('KeyDate')) \
        .offset(offset).limit(size)
    return [{
        'sale_id': row[0],
        'date': row[1],
        'amount': row[2],
    } for row in results.collect()]


@router.get('/by_product/{product_id}')
def sales_by_product(
    product_id: str,
    init_date: str = '2023-10-03',
    end_date: str = '2023-11-30',
    page: int = 1, size: int = 10
):
    offset = size * (page - 1)
    dates = (init_date, end_date)
    results = df.select('KeySale', 'KeyDate', 'Amount') \
        .filter((col('KeyProduct') == product_id) & (col('KeyDate').between(*dates))) \
        .orderBy(desc('KeyDate')) \
        .offset(offset).limit(size)
    return [{
        'sale_id': row[0],
        'date': row[1],
        'amount': row[2],
    } for row in results.collect()]


@router.get('/by_store/{store_id}')
def sales_by_store(
    store_id: str,
    init_date: str = '2023-10-03',
    end_date: str = '2023-11-30',
    page: int = 1, size: int = 10
):
    offset = size * (page - 1)
    dates = (init_date, end_date)
    results = df.select('KeySale', 'KeyDate', 'Amount') \
        .filter((col('KeyProduct') == store_id) & (col('KeyDate').between(*dates))) \
        .orderBy(desc('KeyDate')) \
        .offset(offset).limit(size)
    return [{
        'sale_id': row[0],
        'date': row[1],
        'amount': row[2],
    } for row in results.collect()]


@router.get('/aggregated_by_store')
def sales_aggregated_by_store(page: int = 1, size: int = 20):
    offset = size * (page - 1)
    results = df.groupBy('KeyStore', 'Stores.StoreName') \
        .agg(sum('Amount').alias('TotalAmount'), avg('Amount').alias('AvgAmount')) \
        .orderBy(asc('Stores.StoreName')) \
        .offset(offset).limit(size)
    return [{
        'store_id': row[0],
        'store_name': row[1],
        'total': row[2],
        'avg': row[3],
    } for row in results.collect()]


@router.get('/aggregated_by_product')
def sales_aggregated_by_product(page: int = 1, size: int = 20):
    offset = size * (page - 1)
    results = df.groupBy('KeyProduct', 'Products.ProductName') \
        .agg(sum('Amount').alias('TotalAmount'), avg('Amount').alias('AvgAmount')) \
        .orderBy(asc('Products.ProductName')) \
        .offset(offset).limit(size)
    return [{
        'product_id': row[0],
        'product_name': row[1],
        'total': row[2],
        'avg': row[3],
    } for row in results.collect()]


@router.get('/aggregated_by_employee')
def sales_aggregated_by_employee(page: int = 1, size: int = 20):
    offset = size * (page - 1)
    results = df.groupBy('KeyEmployee', 'Employees.EmployeeName') \
        .agg(sum('Amount').alias('TotalAmount'), avg('Amount').alias('AvgAmount')) \
        .orderBy(asc('Employees.EmployeeName')) \
        .offset(offset).limit(size)
    return [{
        'employee_id': row[0],
        'employee_name': row[1],
        'total': row[2],
        'avg': row[3],
    } for row in results.collect()]
