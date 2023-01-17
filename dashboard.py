from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
from PyQt6.uic import loadUiType
import MySQLdb

ui, _ = loadUiType('dashboard.ui')


class MainApp(QWidget, ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.handle_ui_change()
        self.handle_buttons()
        self.show_category()
        self.show_authors()
        self.show_publisher()
        self.show_category_combobox()
        self.show_author_combobox()
        self.setWindowTitle('Raju')
        self.show()

    def handle_ui_change(self):
        self.hide_theme()

    def handle_buttons(self):
        self.pushButton_3.clicked.connect(self.show_theme)
        self.pushButton_21.clicked.connect(self.hide_theme)
        self.pushButton.clicked.connect(self.open_day_to_day_tab)
        self.pushButton_2.clicked.connect(self.open_books_tab)
        self.pushButton_4.clicked.connect(self.open_users_tab)
        self.pushButton_5.clicked.connect(self.open_settings_tab)
        self.pushButton_8.clicked.connect(self.add_new_book)
        self.pushButton_14.clicked.connect(self.add_category)
        self.pushButton_15.clicked.connect(self.add_author)
        self.pushButton_16.clicked.connect(self.add_publisher)


    def show_theme(self):
        self.groupBox_3.show()

    def hide_theme(self):
        self.groupBox_3.hide()

    ##############################
    #########################

    def open_day_to_day_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def open_books_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def open_users_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def open_settings_tab(self):
        self.tabWidget.setCurrentIndex(3)

    ############Books###########

    def add_new_book(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cur = self.db.cursor()

        book_title = self.lineEdit_3.text()
        book_code = self.lineEdit_2.text()
        book_category = self.comboBox_3.CurrentText()
        book_author = self.comboBox_4.CurrentText()
        book_publisher = self.comboBox_5.CurrentText()
        book_price = self.lineEdit_4.Text()

    def search_books(self):
        pass

    def edit_books(self):
        pass

    def delete_books(self):
        pass

    ##############################

    def add_new_user(self):
        pass

    def login(self):
        pass

    def edit_user(self):
        pass

    #################settings###############

    def add_category(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cur = self.db.cursor()
        category_name = self.lineEdit_19.text()
        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''', (category_name,))
        self.db.commit()
        self.lineEdit_19.setText('')
        self.show_category()


    def show_category(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cur = self.db.cursor()
        self.cur.execute('''SELECT category_name FROM category''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)



    def add_author(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cur = self.db.cursor()
        author_name = self.lineEdit_20.text()
        self.cur.execute('''
                    INSERT INTO authors (author_name) VALUES (%s)
                ''', (author_name,))
        self.db.commit()
        self.lineEdit_20.setText('')
        print('Author added')
        self.show_authors()

    def show_authors(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cur = self.db.cursor()
        self.cur.execute('''SELECT author_name FROM authors''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)


    def add_publisher(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cur = self.db.cursor()
        publisher_name = self.lineEdit_21.text()
        self.cur.execute('''
                    INSERT INTO publisher (publisher_name) VALUES (%s)
                ''', (publisher_name,))
        self.db.commit()
        self.show_publisher()

    def show_publisher(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cur = self.db.cursor()
        self.cur.execute('''SELECT publisher_name FROM publisher''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)


##########Show setting datas################
    def show_category_combobox(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cur = self.db.cursor()
        self.cur.execute('''SELECT category_name FROM category''')
        data = self.cur.fetchall()

        for category in data :
            # print(category[0])
            self.comboBox_3.addItem(category[0])
    def show_author_combobox(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="root", db="library")
        self.cur = self.db.cursor()
        self.cur.execute('''SELECT author_name FROM authors''')
        data = self.cur.fetchall()

        for author in data:
            # print(category[0])
            self.comboBox_4.addItem(author[0])
    def show_publisher_combobox(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    # window.show()
    app.exec()


if __name__ == '__main__':
    main()
