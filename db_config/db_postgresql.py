from typing import Union
import asyncpg
from asyncpg.pool import Pool
from asyncpg import Connection
from data.config import *


class DataBase:
    def __init__(self):
        self.pool: Union[Pool, None]

    async def conf(self):
        self.pool = await asyncpg.create_pool(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            database=DB_NAME
        )

    async def execute(self, sql, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False,
                      executemany: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(sql, *args)
                elif fetchval:
                    result = await connection.fetchval(sql, *args)
                elif fetchrow:
                    result = await connection.fetchrow(sql, *args)
                elif execute:
                    result = await connection.execute(sql, *args)
                elif executemany:
                    result = await connection.executemany(sql, *args)
            return result

    async def create_table_user(self):
        sql = """
                CREATE TABLE IF NOT EXISTS Users(
                    id BIGINT NOT NULL UNIQUE,
                    full_name VARCHAR(120),
                    phone_number VARCHAR(15)
                )      
"""
        await self.execute(sql, execute=True)

    async def create_user(self, chat_id):
        sql = """
                INSERT INTO Users(id)
                VALUES ($1)
                ON CONFLICT (id) DO NOTHING;    
"""
        await self.execute(sql, chat_id, execute=True)

    async def update_user(self, full_name, phone_number, chat_id):
        sql = """
                UPDATE Users SET full_name=$1, phone_number=$2 WHERE id=$3
"""
        await self.execute(sql, full_name, phone_number, chat_id, execute=True)

    async def user_info(self, chat_id):
        sql = """
                SELECT full_name FROM Users WHERE id=$1        
"""
        return await self.execute(sql, chat_id, fetchval=True)

    async def create_table_category(self):
        sql = """
                CREATE TABLE IF NOT EXISTS Categories(
                    id SERIAL PRIMARY KEY,
                    category_code TEXT NOT NULL,
                    category_name TEXT NOT NULL
                )          
"""
        await self.execute(sql, execute=True)

    async def create_table_subcategory(self):
        sql = """
                        CREATE TABLE IF NOT EXISTS SubCategories(
                            id SERIAL PRIMARY KEY,
                            subcategory_code TEXT NOT NULL,
                            subcategory_name TEXT NOT NULL,
                            category_id INTEGER NOT NULL,
                            FOREIGN KEY(category_id) REFERENCES Categories(id) ON DELETE CASCADE
                        )          
        """
        await self.execute(sql, execute=True)

    async def create_table_product(self):
        sql = """
                CREATE TABLE IF NOT EXISTS Products(
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL, 
                    photo TEXT NOT NULL,
                    description TEXT,
                    subcategory_id INTEGER,
                    price TEXT,
                    FOREIGN KEY(subcategory_id) REFERENCES SubCategories(id) ON DELETE CASCADE
                )
"""
        await self.execute(sql, execute=True)

    async def create_table_order(self):
        sql = """
                    CREATE TABLE IF NOT EXISTS Orders(
                        id SERIAL PRIMARY KEY,
                        customer_name TEXT NOT NULL,
                        date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )          
    """
        await self.execute(sql, execute=True)

    async def create_table_order_item(self):
        sql = """
                    CREATE TABLE IF NOT EXISTS OrderItem(
                        id SERIAL PRIMARY KEY,
                        product_name TEXT,
                        product_quantity INTEGER,
                        product_price BIGINT,
                        product_total_price BIGINT,
                        order_id INTEGER,
                        FOREIGN KEY(order_id) REFERENCES Orders(id) ON DELETE CASCADE
                    )          
    """
        await self.execute(sql, execute=True)

    async def create_order(self, customer_name):
        sql = """
                INSERT INTO Orders(customer_name)
                VALUES($1) returning *    
        """
        return await self.execute(sql, customer_name, fetchrow=True)

    async def create_order_item(self, data_order_item):
        sql = """
                INSERT INTO OrderItem(product_name, product_quantity, product_price, product_total_price, order_id)
                VALUES($1, $2, $3, $4, $5)       
    """
        await self.execute(sql, data_order_item, executemany=True)

    async def insert_category(self, category_list):
        sql = """
                INSERT INTO Categories(category_code, category_name)
                VALUES($1, $2)    
"""
        await self.execute(sql, category_list, executemany=True)

    async def insert_subcategory(self, subcategory_list):
        sql = """
                INSERT INTO SubCategories(subcategory_code, subcategory_name, category_id)
                VALUES($1, $2, $3)    
"""
        await self.execute(sql, subcategory_list, executemany=True)

    async def insert_product(self, product_list):
        sql = """
                INSERT INTO Products(title, photo, description,  subcategory_id, price)
                VALUES ($1, $2, $3, $4, $5)    
"""
        await self.execute(sql, product_list, executemany=True)

    async def categories(self):
        sql = "SELECT category_name, category_code FROM Categories"

        return await self.execute(sql, fetch=True)

    async def get_subcategories(self, category_code):
        sql = """
                SELECT subcategory_name, subcategory_code 
                FROM SubCategories 
                WHERE category_id = (SELECT id FROM Categories WHERE category_code = $1)  
"""
        return await self.execute(sql, category_code, fetch=True)

    async def get_products(self, subcategory_code):
        sql = """
                SELECT title, id 
                FROM Products
                WHERE subcategory_id = (SELECT id FROM SubCategories WHERE subcategory_code = $1)  
"""
        return await self.execute(sql, subcategory_code, fetch=True)

    async def back_subcategories(self, subcategory_code):
        sql = """
                    SELECT subcategory_name, subcategory_code 
                    FROM SubCategories 
                    WHERE category_id = (SELECT category_id FROM SubCategories WHERE subcategory_code = $1)  
    """
        return await self.execute(sql, subcategory_code, fetch=True)

    async def get_product_by_id(self, product_id):
        sql = "SELECT * FROM Products WHERE id=$1"

        return await self.execute(sql, product_id, fetchrow=True)

    async def back_product_list(self, subcategory_id):
        sql = """
                SELECT title, id
                FROM Products
                WHERE subcategory_id = $1        
"""
        return await self.execute(sql, subcategory_id, fetch=True)

    async def get_price_by_id(self, title):
        sql = "SELECT price, id FROM Products WHERE title=$1"

        return await self.execute(sql, title, fetch=True)

    async def category_name(self, category_code):
        sql = """
                SELECT category_name 
                FROM Categories WHERE category_code = $1        
"""
        return await self.execute(sql, category_code, fetchval=True)

    async def subcategory_name(self, subcategory_code):
        sql = """
                SELECT subcategory_name 
                FROM SubCategories WHERE subcategory_code = $1        
"""
        return await self.execute(sql, subcategory_code, fetchval=True)
