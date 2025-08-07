import sqlite3
import random

class ProductDB:
    def __init__(self, db_name="products.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def insert_product(self, product_id, name, price):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO products (id, name, price) VALUES (?, ?, ?)",
            (product_id, name, price)
        )
        self.conn.commit()

    def update_product(self, product_id, name=None, price=None):
        cursor = self.conn.cursor()
        if name is not None and price is not None:
            cursor.execute(
                "UPDATE products SET name=?, price=? WHERE id=?",
                (name, price, product_id)
            )
        elif name is not None:
            cursor.execute(
                "UPDATE products SET name=? WHERE id=?",
                (name, product_id)
            )
        elif price is not None:
            cursor.execute(
                "UPDATE products SET price=? WHERE id=?",
                (price, product_id)
            )
        self.conn.commit()

    def delete_product(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM products WHERE id=?",
            (product_id,)
        )
        self.conn.commit()

    def select_product(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE id=?",
            (product_id,)
        )
        return cursor.fetchone()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = ProductDB()
    # 샘플 데이터 100개 삽입
    product_names = [
        "노트북", "스마트폰", "태블릿", "모니터", "키보드", "마우스", "프린터", "스피커", "헤드폰", "웹캠"
    ]
    for i in range(1, 101):
        name = random.choice(product_names) + f"_{i}"
        price = random.randint(50000, 2000000)
        db.insert_product(i, name, price)
    print("샘플 데이터 100개 삽입 완료")
    db.close()
