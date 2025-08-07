# import sys
# import sqlite3
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
#     QTableWidget, QTableWidgetItem, QLabel, QMessageBox
# )

# DB_NAME = "products.db"

# class ProductManager(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("전자제품 관리")
#         self.resize(500, 400)
#         self.conn = sqlite3.connect(DB_NAME)  # SQLite DB 연결
#         self.create_table()                   # 테이블 생성
#         self.init_ui()                        # UI 초기화
#         self.load_data()                      # 데이터 로드

#     def create_table(self):
#         """MyProducts 테이블이 없으면 생성"""
#         cursor = self.conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS MyProducts (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 price REAL NOT NULL
#             )
#         """)
#         self.conn.commit()

#     def init_ui(self):
#         """UI 구성 및 이벤트 연결"""
#         layout = QVBoxLayout()

#         # 입력창 레이아웃
#         form_layout = QHBoxLayout()
#         self.name_input = QLineEdit()
#         self.name_input.setPlaceholderText("제품명")
#         self.price_input = QLineEdit()
#         self.price_input.setPlaceholderText("가격")
#         form_layout.addWidget(QLabel("제품명:"))
#         form_layout.addWidget(self.name_input)
#         form_layout.addWidget(QLabel("가격:"))
#         form_layout.addWidget(self.price_input)
#         layout.addLayout(form_layout)

#         # 버튼 레이아웃
#         btn_layout = QHBoxLayout()
#         self.add_btn = QPushButton("입력")
#         self.update_btn = QPushButton("수정")
#         self.delete_btn = QPushButton("삭제")
#         self.search_btn = QPushButton("검색")
#         btn_layout.addWidget(self.add_btn)
#         btn_layout.addWidget(self.update_btn)
#         btn_layout.addWidget(self.delete_btn)
#         btn_layout.addWidget(self.search_btn)
#         layout.addLayout(btn_layout)

#         # 테이블(리스트) 생성
#         self.table = QTableWidget()
#         self.table.setColumnCount(3)
#         self.table.setHorizontalHeaderLabels(["ID", "제품명", "가격"])
#         self.table.setSelectionBehavior(self.table.SelectRows)
#         layout.addWidget(self.table)

#         self.setLayout(layout)

#         # 버튼 및 테이블 이벤트 연결
#         self.add_btn.clicked.connect(self.add_product)
#         self.update_btn.clicked.connect(self.update_product)
#         self.delete_btn.clicked.connect(self.delete_product)
#         self.search_btn.clicked.connect(self.search_product)
#         self.table.cellClicked.connect(self.table_clicked)

#     def load_data(self, products=None):
#         """테이블에 데이터 표시"""
#         if products is None:
#             cursor = self.conn.cursor()
#             cursor.execute("SELECT * FROM MyProducts")
#             products = cursor.fetchall()
#         self.table.setRowCount(0)
#         for row_data in products:
#             row = self.table.rowCount()
#             self.table.insertRow(row)
#             for col, item in enumerate(row_data):
#                 self.table.setItem(row, col, QTableWidgetItem(str(item)))

#     def add_product(self):
#         """제품 추가"""
#         name = self.name_input.text().strip()
#         price = self.price_input.text().strip()
#         if not name or not price:
#             QMessageBox.warning(self, "입력 오류", "제품명과 가격을 입력하세요.")
#             return
#         try:
#             price_val = float(price)
#         except ValueError:
#             QMessageBox.warning(self, "입력 오류", "가격은 숫자여야 합니다.")
#             return
#         cursor = self.conn.cursor()
#         cursor.execute("INSERT INTO MyProducts (name, price) VALUES (?, ?)", (name, price_val))
#         self.conn.commit()
#         self.load_data()
#         self.name_input.clear()
#         self.price_input.clear()

#     def update_product(self):
#         """선택한 제품 정보 수정"""
#         selected = self.table.currentRow()
#         if selected < 0:
#             QMessageBox.warning(self, "선택 오류", "수정할 제품을 선택하세요.")
#             return
#         id_item = self.table.item(selected, 0)
#         if not id_item:
#             return
#         prod_id = int(id_item.text())
#         name = self.name_input.text().strip()
#         price = self.price_input.text().strip()
#         if not name or not price:
#             QMessageBox.warning(self, "입력 오류", "제품명과 가격을 입력하세요.")
#             return
#         try:
#             price_val = float(price)
#         except ValueError:
#             QMessageBox.warning(self, "입력 오류", "가격은 숫자여야 합니다.")
#             return
#         cursor = self.conn.cursor()
#         cursor.execute("UPDATE MyProducts SET name=?, price=? WHERE id=?", (name, price_val, prod_id))
#         self.conn.commit()
#         self.load_data()

#     def delete_product(self):
#         """선택한 제품 삭제"""
#         selected = self.table.currentRow()
#         if selected < 0:
#             QMessageBox.warning(self, "선택 오류", "삭제할 제품을 선택하세요.")
#             return
#         id_item = self.table.item(selected, 0)
#         if not id_item:
#             return
#         prod_id = int(id_item.text())
#         cursor = self.conn.cursor()
#         cursor.execute("DELETE FROM MyProducts WHERE id=?", (prod_id,))
#         self.conn.commit()
#         self.load_data()
#         self.name_input.clear()
#         self.price_input.clear()

#     def search_product(self):
#         """제품명으로 검색"""
#         name = self.name_input.text().strip()
#         cursor = self.conn.cursor()
#         if name:
#             cursor.execute("SELECT * FROM MyProducts WHERE name LIKE ?", ('%' + name + '%',))
#         else:
#             cursor.execute("SELECT * FROM MyProducts")
#         products = cursor.fetchall()
#         self.load_data(products)

#     def table_clicked(self, row, col):
#         """테이블에서 행 선택 시 입력창에 값 표시"""
#         id_item = self.table.item(row, 0)
#         name_item = self.table.item(row, 1)
#         price_item = self.table.item(row, 2)
#         if name_item and price_item:
#             self.name_input.setText(name_item.text())
#             self.price_input.setText(price_item.text())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = ProductManager()
#     win.show()
#     sys.exit(app.exec_())


import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QLabel, QMessageBox
)
from PyQt5.QtGui import QFont

DB_NAME = "products.db"

class ProductManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("전자제품 관리")
        self.resize(520, 420)
        self.conn = sqlite3.connect(DB_NAME)  # SQLite DB 연결
        self.create_table()                   # 테이블 생성
        self.init_ui()                        # UI 초기화
        self.load_data()                      # 데이터 로드

    def create_table(self):
        """MyProducts 테이블이 없으면 생성"""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MyProducts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)
        self.conn.commit()

    def init_ui(self):
        """UI 구성 및 스타일 적용"""
        layout = QVBoxLayout()

        # 제목 라벨
        title = QLabel("전자제품 관리 프로그램")
        title.setFont(QFont("맑은 고딕", 16, QFont.Bold))
        title.setStyleSheet("color: #2d5be3; margin-bottom: 10px;")
        layout.addWidget(title)

        # 입력창 레이아웃
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("제품명")
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("가격")
        self.name_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #2d5be3;
                border-radius: 5px;
                padding: 4px;
                background: #f0f6ff;
            }
        """)
        self.price_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #2d5be3;
                border-radius: 5px;
                padding: 4px;
                background: #f0f6ff;
            }
        """)
        form_layout.addWidget(QLabel("제품명:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("가격:"))
        form_layout.addWidget(self.price_input)
        layout.addLayout(form_layout)

        # 버튼 레이아웃
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("입력")
        self.update_btn = QPushButton("수정")
        self.delete_btn = QPushButton("삭제")
        self.search_btn = QPushButton("검색")
        # 버튼 스타일 적용
        btn_style = """
            QPushButton {
                background-color: #2d5be3;
                color: white;
                border-radius: 6px;
                padding: 6px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1c3fa0;
            }
        """
        self.add_btn.setStyleSheet(btn_style)
        self.update_btn.setStyleSheet(btn_style)
        self.delete_btn.setStyleSheet(btn_style)
        self.search_btn.setStyleSheet(btn_style)
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(self.search_btn)
        layout.addLayout(btn_layout)

        # 테이블(리스트) 생성 및 스타일 적용
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "제품명", "가격"])
        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setStyleSheet("""
            QTableWidget {
                background: #f8fbff;
                border: 1px solid #b3c6e7;
                font-size: 13px;
            }
            QHeaderView::section {
                background-color: #e3ecfc;
                color: #2d5be3;
                font-weight: bold;
                border: 1px solid #b3c6e7;
            }
            QTableWidget::item:selected {
                background: #d0e2ff;
                color: #1c3fa0;
            }
        """)
        layout.addWidget(self.table)

        self.setLayout(layout)

        # 버튼 및 테이블 이벤트 연결
        self.add_btn.clicked.connect(self.add_product)
        self.update_btn.clicked.connect(self.update_product)
        self.delete_btn.clicked.connect(self.delete_product)
        self.search_btn.clicked.connect(self.search_product)
        self.table.cellClicked.connect(self.table_clicked)

    def load_data(self, products=None):
        """테이블에 데이터 표시"""
        if products is None:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM MyProducts")
            products = cursor.fetchall()
        self.table.setRowCount(0)
        for row_data in products:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for col, item in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(item)))

    def add_product(self):
        """제품 추가"""
        name = self.name_input.text().strip()
        price = self.price_input.text().strip()
        if not name or not price:
            QMessageBox.warning(self, "입력 오류", "제품명과 가격을 입력하세요.")
            return
        try:
            price_val = float(price)
        except ValueError:
            QMessageBox.warning(self, "입력 오류", "가격은 숫자여야 합니다.")
            return
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO MyProducts (name, price) VALUES (?, ?)", (name, price_val))
        self.conn.commit()
        self.load_data()
        self.name_input.clear()
        self.price_input.clear()

    def update_product(self):
        """선택한 제품 정보 수정"""
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "선택 오류", "수정할 제품을 선택하세요.")
            return
        id_item = self.table.item(selected, 0)
        if not id_item:
            return
        prod_id = int(id_item.text())
        name = self.name_input.text().strip()
        price = self.price_input.text().strip()
        if not name or not price:
            QMessageBox.warning(self, "입력 오류", "제품명과 가격을 입력하세요.")
            return
        try:
            price_val = float(price)
        except ValueError:
            QMessageBox.warning(self, "입력 오류", "가격은 숫자여야 합니다.")
            return
        cursor = self.conn.cursor()
        cursor.execute("UPDATE MyProducts SET name=?, price=? WHERE id=?", (name, price_val, prod_id))
        self.conn.commit()
        self.load_data()

    def delete_product(self):
        """선택한 제품 삭제"""
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "선택 오류", "삭제할 제품을 선택하세요.")
            return
        id_item = self.table.item(selected, 0)
        if not id_item:
            return
        prod_id = int(id_item.text())
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM MyProducts WHERE id=?", (prod_id,))
        self.conn.commit()
        self.load_data()
        self.name_input.clear()
        self.price_input.clear()

    def search_product(self):
        """제품명으로 검색"""
        name = self.name_input.text().strip()
        cursor = self.conn.cursor()
        if name:
            cursor.execute("SELECT * FROM MyProducts WHERE name LIKE ?", ('%' + name + '%',))
        else:
            cursor.execute("SELECT * FROM MyProducts")
        products = cursor.fetchall()
        self.load_data(products)

    def table_clicked(self, row, col):
        """테이블에서 행 선택 시 입력창에 값 표시"""
        id_item = self.table.item(row, 0)
        name_item = self.table.item(row, 1)
        price_item = self.table.item(row, 2)
        if name_item and price_item:
            self.name_input.setText(name_item.text())
            self.price_input.setText(price_item.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ProductManager()
    win.show()
    sys.exit(app.exec_())