'''
В PySpark приложении датафреймами(pyspark.sql.DataFrame) заданы продукты, категории и их связи. 
Каждому продукту может соответствовать несколько категорий или ни одной. 
А каждой категории может соответствовать несколько продуктов или ни одного. Напишите метод на PySpark, 
который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий.
'''
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit

def get_products_with_categories(products_df: DataFrame, 
                                categories_df: DataFrame, 
                                product_category_links_df: DataFrame) -> DataFrame:
    products_with_categories = (
        products_df.join(
            product_category_links_df, 
            on='product_id', 
            how='left'
        )
        .join(
            categories_df, 
            on='category_id', 
            how='left'
        )
        .select(
            col('product_name'), 
            col('category_name')
        )
    )
    
    products_without_categories = (
        products_df.join(
            product_category_links_df, 
            on='product_id', 
            how='left_anti'
        )
        .select(
            col('product_name'), 
            lit(None).alias('category_name')
        )
    )
    
    result_df = products_with_categories.union(products_without_categories)
    
    return result_df
