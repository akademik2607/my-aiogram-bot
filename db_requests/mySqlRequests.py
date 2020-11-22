import pymysql
from data import config

def db_request(val_name, parent_val):
    connection = pymysql.connect(host=config.DB_HOST,
                                 user=config.DB_USER,
                                 password=config.DB_PASS,
                                 db=config.DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        connection.commit()

        with connection.cursor() as cursor:
            if val_name == 'category':
                sql = "SELECT `category_name`  FROM `categories`"
                cursor.execute(sql)
                result = cursor.fetchall()
            elif val_name == "sub_category":
                sql = f'''SELECT sub_category_name FROM sub_categories 
                      INNER JOIN categories 
                      ON sub_categories.category_id = categories.id 
                      WHERE categories.category_name = "{parent_val}";'''
                cursor.execute(sql)
                result = cursor.fetchall()
            return result
    finally:
        connection.close()


def get_sql_id(param_name, name_of_table, column_name):
    connection = pymysql.connect(host=config.DB_HOST,
                                 user=config.DB_USER,
                                 password=config.DB_PASS,
                                 db=config.DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        connection.commit()
        with connection.cursor() as cursor:
            # Read a single record
            sql = f"SELECT `id`  FROM `{name_of_table}` WHERE `{column_name}` = '{param_name}';"  # рефактор
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def return_subcategories(id_cat, table_name, req_par, name_par):
    connection = pymysql.connect(host=config.DB_HOST,
                                 user=config.DB_USER,
                                 password=config.DB_PASS,
                                 db=config.DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:

        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = f"SELECT `{req_par}`  FROM `{table_name}` WHERE `{name_par}` = {id_cat}"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

