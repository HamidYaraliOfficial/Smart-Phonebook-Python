import sys
import sqlite3
import csv
from datetime import datetime, timedelta
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QComboBox, QLabel,
    QDialog, QFormLayout, QMessageBox, QSystemTrayIcon, QMenu, QToolBar,
    QStyleFactory, QTabWidget, QDateEdit, QCheckBox, QHeaderView, QTextEdit
)
from PyQt6.QtGui import QIcon, QFont, QColor, QPalette, QAction
from PyQt6.QtCore import Qt, QDate, QTimer
from PyQt6.QtCore import QTranslator, QLocale
import qdarkstyle
from qdarkstyle import LightPalette, DarkPalette

# Language dictionaries
LANGUAGES = {
    'English': {
        'app_title': 'Smart Phonebook',
        'add_contact': 'Add Contact',
        'edit_contact': 'Edit Contact',
        'delete_contact': 'Delete Contact',
        'search': 'Search',
        'export_csv': 'Export to CSV',
        'groups': 'Groups',
        'birthdays': 'Birthdays',
        'settings': 'Settings',
        'language': 'Language',
        'theme': 'Theme',
        'default_theme': 'Windows Default',
        'light_theme': 'Light',
        'dark_theme': 'Dark',
        'red_theme': 'Red',
        'blue_theme': 'Blue',
        'name': 'Name',
        'phone': 'Phone',
        'email': 'Email',
        'address': 'Address',
        'group': 'Group',
        'birthday': 'Birthday',
        'notes': 'Notes',
        'save': 'Save',
        'cancel': 'Cancel',
        'no_contacts': 'No contacts found',
        'delete_confirm': 'Are you sure you want to delete this contact?',
        'export_success': 'Contacts exported successfully to {}',
        'export_error': 'Error exporting contacts: {}',
        'birthday_reminder': 'Birthday Reminder: {} has a birthday on {}!',
        'no_birthdays': 'No upcoming birthdays',
        'new_group': 'New Group',
        'group_name': 'Group Name',
        'add_group': 'Add Group',
        'delete_group': 'Delete Group',
        'group_delete_confirm': 'Are you sure you want to delete this group?',
        'contact_added': 'Contact added successfully',
        'contact_updated': 'Contact updated successfully',
        'contact_deleted': 'Contact deleted successfully',
        'group_added': 'Group added successfully',
        'group_deleted': 'Group deleted successfully',
        'search_placeholder': 'Search by name, phone, or email...',
        'all_groups': 'All Groups',
        'notes_placeholder': 'Enter additional notes...',
        'contacts': 'Contacts'
    },
    'فارسی': {
        'app_title': 'دفترچه تلفن هوشمند',
        'add_contact': 'افزودن مخاطب',
        'edit_contact': 'ویرایش مخاطب',
        'delete_contact': 'حذف مخاطب',
        'search': 'جستجو',
        'export_csv': 'خروجی به CSV',
        'groups': 'گروه‌ها',
        'birthdays': 'تولدها',
        'settings': 'تنظیمات',
        'language': 'زبان',
        'theme': 'تم',
        'default_theme': 'پیش‌فرض ویندوز',
        'light_theme': 'روشن',
        'dark_theme': 'تیره',
        'red_theme': 'قرمز',
        'blue_theme': 'آبی',
        'name': 'نام',
        'phone': 'تلفن',
        'email': 'ایمیل',
        'address': 'آدرس',
        'group': 'گروه',
        'birthday': 'تولد',
        'notes': 'یادداشت‌ها',
        'save': 'ذخیره',
        'cancel': 'لغو',
        'no_contacts': 'مخاطبی یافت نشد',
        'delete_confirm': 'آیا مطمئن هستید که می‌خواهید این مخاطب را حذف کنید؟',
        'export_success': 'مخاطبین با موفقیت به {} صادر شدند',
        'export_error': 'خطا در صدور مخاطبین: {}',
        'birthday_reminder': 'یادآور تولد: {} در تاریخ {} تولد دارد!',
        'no_birthdays': 'تولدهای آینده وجود ندارد',
        'new_group': 'گروه جدید',
        'group_name': 'نام گروه',
        'add_group': 'افزودن گروه',
        'delete_group': 'حذف گروه',
        'group_delete_confirm': 'آیا مطمئن هستید که می‌خواهید این گروه را حذف کنید؟',
        'contact_added': 'مخاطب با موفقیت اضافه شد',
        'contact_updated': 'مخاطب با موفقیت به‌روزرسانی شد',
        'contact_deleted': 'مخاطب با موفقیت حذف شد',
        'group_added': 'گروه با موفقیت اضافه شد',
        'group_deleted': 'گروه با موفقیت حذف شد',
        'search_placeholder': 'جستجو بر اساس نام، تلفن یا ایمیل...',
        'all_groups': 'همه گروه‌ها',
        'notes_placeholder': 'یادداشت‌های اضافی را وارد کنید...',
        'contacts': 'مخاطبین'
    },
    '中文': {
        'app_title': '智能电话簿',
        'add_contact': '添加联系人',
        'edit_contact': '编辑联系人',
        'delete_contact': '删除联系人',
        'search': '搜索',
        'export_csv': '导出到CSV',
        'groups': '分组',
        'birthdays': '生日',
        'settings': '设置',
        'language': '语言',
        'theme': '主题outside: 主题',
        'default_theme': 'Windows默认',
        'light_theme': '亮色',
        'dark_theme': '暗色',
        'red_theme': '红色',
        'blue_theme': '蓝色',
        'name': '姓名',
        'phone': '电话',
        'email': '电子邮件',
        'address': '地址',
        'group': '分组',
        'birthday': '生日',
        'notes': '备注',
        'save': '保存',
        'cancel': '取消',
        'no_contacts': '未找到联系人',
        'delete_confirm': '您确定要删除此联系人吗？',
        'export_success': '联系人已成功导出到 {}',
        'export_error': '导出联系人时出错：{}',
        'birthday_reminder': '生日提醒：{} 的生日是 {}！',
        'no_birthdays': '没有即将到来的生日',
        'new_group': '新分组',
        'group_name': '分组名称',
        'add_group': '添加分组',
        'delete_group': '删除分组',
        'group_delete_confirm': '您确定要删除此分组吗？',
        'contact_added': '联系人添加成功',
        'contact_updated': '联系人更新成功',
        'contact_deleted': '联系人删除成功',
        'group_added': '分组添加成功',
        'group_deleted': '分组删除成功',
        'search_placeholder': '按姓名、电话或电子邮件搜索...',
        'all_groups': '所有分组',
        'notes_placeholder': '输入附加备注...',
        'contacts': '联系人'
    },
    'Русский': {
        'app_title': 'Умная телефонная книга',
        'add_contact': 'Добавить контакт',
        'edit_contact': 'Редактировать контакт',
        'delete_contact': 'Удалить контакт',
        'search': 'Поиск',
        'export_csv': 'Экспорт в CSV',
        'groups': 'Группы',
        'birthdays': 'Дни рождения',
        'settings': 'Настройки',
        'language': 'Язык',
        'theme': 'Тема',
        'default_theme': 'По умолчанию Windows',
        'light_theme': 'Светлая',
        'dark_theme': 'Темная',
        'red_theme': 'Красная',
        'blue_theme': 'Синяя',
        'name': 'Имя',
        'phone': 'Телефон',
        'email': 'Электронная почта',
        'address': 'Адрес',
        'group': 'Группа',
        'birthday': 'День рождения',
        'notes': 'Заметки',
        'save': 'Сохранить',
        'cancel': 'Отмена',
        'no_contacts': 'Контакты не найдены',
        'delete_confirm': 'Вы уверены, что хотите удалить этот контакт?',
        'export_success': 'Контакты успешно экспортированы в {}',
        'export_error': 'Ошибка экспорта контактов: {}',
        'birthday_reminder': 'Напоминание о дне рождения: у {} день рождения {}!',
        'no_birthdays': 'Нет предстоящих дней рождения',
        'new_group': 'Новая группа',
        'group_name': 'Название группы',
        'add_group': 'Добавить группу',
        'delete_group': 'Удалить группу',
        'group_delete_confirm': 'Вы уверены, что хотите удалить эту группу?',
        'contact_added': 'Контакт успешно добавлен',
        'contact_updated': 'Контакт успешно обновлен',
        'contact_deleted': 'Контакт успешно удален',
        'group_added': 'Группа успешно добавлена',
        'group_deleted': 'Группа успешно удалена',
        'search_placeholder': 'Поиск по имени, телефону или электронной почте...',
        'all_groups': 'Все группы',
        'notes_placeholder': 'Введите дополнительные заметки...',
        'contacts': 'Контакты'
    }
}

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('phonebook.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                address TEXT,
                group_id INTEGER,
                birthday TEXT,
                notes TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_contact(self, name, phone, email, address, group_id, birthday, notes):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO contacts (name, phone, email, address, group_id, birthday, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, phone, email, address, group_id, birthday, notes))
        self.conn.commit()

    def update_contact(self, id, name, phone, email, address, group_id, birthday, notes):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE contacts SET name=?, phone=?, email=?, address=?, group_id=?, birthday=?, notes=?
            WHERE id=?
        ''', (name, phone, email, address, group_id, birthday, notes, id))
        self.conn.commit()

    def delete_contact(self, id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM contacts WHERE id=?', (id,))
        self.conn.commit()

    def get_all_contacts(self, group_id=None, search_query=None):
        cursor = self.conn.cursor()
        query = 'SELECT * FROM contacts'
        params = []
        conditions = []
        if group_id:
            conditions.append('group_id=?')
            params.append(group_id)
        if search_query:
            conditions.append('(name LIKE ? OR phone LIKE ? OR email LIKE ?)')
            params.extend([f'%{search_query}%', f'%{search_query}%', f'%{search_query}%'])
        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)
        cursor.execute(query, params)
        return cursor.fetchall()

    def add_group(self, name):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO groups (name) VALUES (?)', (name,))
        self.conn.commit()

    def delete_group(self, id):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE contacts SET group_id=NULL WHERE group_id=?', (id,))
        cursor.execute('DELETE FROM groups WHERE id=?', (id,))
        self.conn.commit()

    def get_all_groups(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM groups')
        return cursor.fetchall()

    def get_upcoming_birthdays(self, days=7):
        cursor = self.conn.cursor()
        today = datetime.now()
        end_date = today + timedelta(days=days)
        current_month = today.month
        current_day = today.day
        end_month = end_date.month
        end_day = end_date.day
        cursor.execute('''
            SELECT name, birthday FROM contacts
            WHERE birthday IS NOT NULL
            AND (
                (SUBSTR(birthday, 6, 2) = ? AND SUBSTR(birthday, 9, 2) >= ?)
                OR (SUBSTR(birthday, 6, 2) = ? AND SUBSTR(birthday, 9, 2) <= ?)
            )
        ''', (str(current_month).zfill(2), str(current_day).zfill(2),
              str(end_month).zfill(2), str(end_day).zfill(2)))
        return cursor.fetchall()

class AddContactDialog(QDialog):
    def __init__(self, db, lang, parent=None):
        super().__init__(parent)
        self.db = db
        self.lang = lang
        self.setWindowTitle(LANGUAGES[lang]['add_contact'])
        self.setup_ui()

    def setup_ui(self):
        layout = QFormLayout()
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.email_input = QLineEdit()
        self.address_input = QLineEdit()
        self.group_combo = QComboBox()
        self.group_combo.addItem(LANGUAGES[self.lang]['all_groups'], 0)
        for group in self.db.get_all_groups():
            self.group_combo.addItem(group[1], group[0])
        self.birthday_input = QDateEdit()
        self.birthday_input.setCalendarPopup(True)
        self.birthday_input.setDate(QDate.currentDate())
        self.notes_input = QTextEdit()
        self.notes_input.setPlaceholderText(LANGUAGES[self.lang]['notes_placeholder'])

        layout.addRow(QLabel(LANGUAGES[self.lang]['name']), self.name_input)
        layout.addRow(QLabel(LANGUAGES[self.lang]['phone']), self.phone_input)
        layout.addRow(QLabel(LANGUAGES[self.lang]['email']), self.email_input)
        layout.addRow(QLabel(LANGUAGES[self.lang]['address']), self.address_input)
        layout.addRow(QLabel(LANGUAGES[self.lang]['group']), self.group_combo)
        layout.addRow(QLabel(LANGUAGES[self.lang]['birthday']), self.birthday_input)
        layout.addRow(QLabel(LANGUAGES[self.lang]['notes']), self.notes_input)

        button_layout = QHBoxLayout()
        save_button = QPushButton(LANGUAGES[self.lang]['save'])
        cancel_button = QPushButton(LANGUAGES[self.lang]['cancel'])
        save_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

class AddGroupDialog(QDialog):
    def __init__(self, lang, parent=None):
        super().__init__(parent)
        self.lang = lang
        self.setWindowTitle(LANGUAGES[lang]['new_group'])
        self.setup_ui()

    def setup_ui(self):
        layout = QFormLayout()
        self.group_name = QLineEdit()
        layout.addRow(QLabel(LANGUAGES[self.lang]['group_name']), self.group_name)

        button_layout = QHBoxLayout()
        save_button = QPushButton(LANGUAGES[self.lang]['save'])
        cancel_button = QPushButton(LANGUAGES[self.lang]['cancel'])
        save_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

class SmartPhonebook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.current_lang = 'English'
        self.current_theme = 'default'
        self.setup_ui()
        self.load_contacts()
        self.setup_tray()
        self.setup_birthday_reminder()

    def setup_ui(self):
        self.setWindowTitle(LANGUAGES[self.current_lang]['app_title'])
        self.setGeometry(100, 100, 1000, 600)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        add_action = QAction(LANGUAGES[self.current_lang]['add_contact'], self)
        edit_action = QAction(LANGUAGES[self.current_lang]['edit_contact'], self)
        delete_action = QAction(LANGUAGES[self.current_lang]['delete_contact'], self)
        export_action = QAction(LANGUAGES[self.current_lang]['export_csv'], self)
        add_action.triggered.connect(self.add_contact)
        edit_action.triggered.connect(self.edit_contact)
        delete_action.triggered.connect(self.delete_contact)
        export_action.triggered.connect(self.export_to_csv)
        toolbar.addAction(add_action)
        toolbar.addAction(edit_action)
        toolbar.addAction(delete_action)
        toolbar.addAction(export_action)

        # Main layout
        top_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(LANGUAGES[self.current_lang]['search_placeholder'])
        self.search_input.textChanged.connect(self.load_contacts)
        self.group_combo = QComboBox()
        self.group_combo.addItem(LANGUAGES[self.current_lang]['all_groups'], 0)
        for group in self.db.get_all_groups():
            self.group_combo.addItem(group[1], group[0])
        self.group_combo.currentIndexChanged.connect(self.load_contacts)
        top_layout.addWidget(QLabel(LANGUAGES[self.current_lang]['search']))
        top_layout.addWidget(self.search_input)
        top_layout.addWidget(QLabel(LANGUAGES[self.current_lang]['group']))
        top_layout.addWidget(self.group_combo)

        # Tabs
        tabs = QTabWidget()
        self.contacts_tab = QWidget()
        self.groups_tab = QWidget()
        self.birthdays_tab = QWidget()
        self.settings_tab = QWidget()
        tabs.addTab(self.contacts_tab, LANGUAGES[self.current_lang]['contacts'])
        tabs.addTab(self.groups_tab, LANGUAGES[self.current_lang]['groups'])
        tabs.addTab(self.birthdays_tab, LANGUAGES[self.current_lang]['birthdays'])
        tabs.addTab(self.settings_tab, LANGUAGES[self.current_lang]['settings'])
        main_layout.addLayout(top_layout)
        main_layout.addWidget(tabs)

        # Contacts tab
        contacts_layout = QVBoxLayout(self.contacts_tab)
        self.contacts_table = QTableWidget()
        self.contacts_table.setColumnCount(6)
        self.contacts_table.setHorizontalHeaderLabels([
            LANGUAGES[self.current_lang]['name'],
            LANGUAGES[self.current_lang]['phone'],
            LANGUAGES[self.current_lang]['email'],
            LANGUAGES[self.current_lang]['address'],
            LANGUAGES[self.current_lang]['group'],
            LANGUAGES[self.current_lang]['birthday']
        ])
        header = self.contacts_table.horizontalHeader()
        for i in range(self.contacts_table.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
        contacts_layout.addWidget(self.contacts_table)

        # Groups tab
        groups_layout = QVBoxLayout(self.groups_tab)
        self.groups_table = QTableWidget()
        self.groups_table.setColumnCount(1)
        self.groups_table.setHorizontalHeaderLabels([LANGUAGES[self.current_lang]['group_name']])
        header = self.groups_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        group_buttons = QHBoxLayout()
        add_group_button = QPushButton(LANGUAGES[self.current_lang]['add_group'])
        delete_group_button = QPushButton(LANGUAGES[self.current_lang]['delete_group'])
        add_group_button.clicked.connect(self.add_group)
        delete_group_button.clicked.connect(self.delete_group)
        group_buttons.addWidget(add_group_button)
        group_buttons.addWidget(delete_group_button)
        groups_layout.addWidget(self.groups_table)
        groups_layout.addLayout(group_buttons)

        # Birthdays tab
        birthdays_layout = QVBoxLayout(self.birthdays_tab)
        self.birthdays_label = QLabel()
        birthdays_layout.addWidget(self.birthdays_label)

        # Settings tab
        settings_layout = QFormLayout(self.settings_tab)
        self.language_combo = QComboBox()
        self.language_combo.addItems(['English', 'فارسی', '中文', 'Русский'])
        self.language_combo.setCurrentText(self.current_lang)
        self.language_combo.currentTextChanged.connect(self.change_language)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems([
            LANGUAGES[self.current_lang]['default_theme'],
            LANGUAGES[self.current_lang]['light_theme'],
            LANGUAGES[self.current_lang]['dark_theme'],
            LANGUAGES[self.current_lang]['red_theme'],
            LANGUAGES[self.current_lang]['blue_theme']
        ])
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        settings_layout.addRow(QLabel(LANGUAGES[self.current_lang]['language']), self.language_combo)
        settings_layout.addRow(QLabel(LANGUAGES[self.current_lang]['theme']), self.theme_combo)

        self.apply_theme()
        self.update_text_direction()

    def setup_tray(self):
        self.tray_icon = QSystemTrayIcon(QIcon('icon.png'), self)
        tray_menu = QMenu()
        show_action = tray_menu.addAction('Show')
        quit_action = tray_menu.addAction('Quit')
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(QApplication.quit)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def setup_birthday_reminder(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_birthdays)
        self.timer.start(86400000)  # Check daily
        self.check_birthdays()

    def apply_theme(self):
        app = QApplication.instance()
        if self.current_theme == LANGUAGES[self.current_lang]['default_theme']:
            app.setStyle(QStyleFactory.create('Windows'))
            palette = QPalette()
            app.setPalette(palette)
        elif self.current_theme == LANGUAGES[self.current_lang]['light_theme']:
            app.setStyleSheet(qdarkstyle.load_stylesheet(palette=LightPalette()))
        elif self.current_theme == LANGUAGES[self.current_lang]['dark_theme']:
            app.setStyleSheet(qdarkstyle.load_stylesheet(palette=DarkPalette()))
        elif self.current_theme == LANGUAGES[self.current_lang]['red_theme']:
            app.setStyleSheet("""
                QWidget { background-color: #FFEBEE; color: #D32F2F; }
                QPushButton { background-color: #D32F2F; color: white; border-radius: 5px; }
                QLineEdit, QComboBox, QTextEdit { background-color: white; color: black; }
                QTableWidget { background-color: white; color: black; }
            """)
        elif self.current_theme == LANGUAGES[self.current_lang]['blue_theme']:
            app.setStyleSheet("""
                QWidget { background-color: #E3F2FD; color: #1565C0; }
                QPushButton { background-color: #1565C0; color: white; border-radius: 5px; }
                QLineEdit, QComboBox, QTextEdit { background-color: white; color: black; }
                QTableWidget { background-color: white; color: black; }
            """)

    def update_text_direction(self):
        if self.current_lang == 'فارسی':
            self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        else:
            self.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

    def change_language(self, lang):
        self.current_lang = lang
        self.update_ui_texts()
        self.update_text_direction()
        self.load_contacts()
        self.load_groups()
        self.check_birthdays()

    def change_theme(self, theme):
        self.current_theme = theme
        self.apply_theme()

    def update_ui_texts(self):
        self.setWindowTitle(LANGUAGES[self.current_lang]['app_title'])
        self.contacts_table.setHorizontalHeaderLabels([
            LANGUAGES[self.current_lang]['name'],
            LANGUAGES[self.current_lang]['phone'],
            LANGUAGES[self.current_lang]['email'],
            LANGUAGES[self.current_lang]['address'],
            LANGUAGES[self.current_lang]['group'],
            LANGUAGES[self.current_lang]['birthday']
        ])
        self.groups_table.setHorizontalHeaderLabels([LANGUAGES[self.current_lang]['group_name']])
        self.search_input.setPlaceholderText(LANGUAGES[self.current_lang]['search_placeholder'])
        self.centralWidget().layout().itemAt(0).layout().itemAt(0).widget().setText(LANGUAGES[self.current_lang]['search'])
        self.centralWidget().layout().itemAt(0).layout().itemAt(2).widget().setText(LANGUAGES[self.current_lang]['group'])
        self.centralWidget().layout().itemAt(1).widget().setTabText(0, LANGUAGES[self.current_lang]['contacts'])
        self.centralWidget().layout().itemAt(1).widget().setTabText(1, LANGUAGES[self.current_lang]['groups'])
        self.centralWidget().layout().itemAt(1).widget().setTabText(2, LANGUAGES[self.current_lang]['birthdays'])
        self.centralWidget().layout().itemAt(1).widget().setTabText(3, LANGUAGES[self.current_lang]['settings'])
        self.groups_tab.layout().itemAt(1).layout().itemAt(0).widget().setText(LANGUAGES[self.current_lang]['add_group'])
        self.groups_tab.layout().itemAt(1).layout().itemAt(1).widget().setText(LANGUAGES[self.current_lang]['delete_group'])
        self.settings_tab.layout().itemAt(0).widget().setText(LANGUAGES[self.current_lang]['language'])
        self.settings_tab.layout().itemAt(1).widget().setText(LANGUAGES[self.current_lang]['theme'])

    def load_contacts(self):
        group_id = self.group_combo.currentData()
        search_query = self.search_input.text()
        contacts = self.db.get_all_contacts(group_id, search_query)
        self.contacts_table.setRowCount(len(contacts))
        groups = {g[0]: g[1] for g in self.db.get_all_groups()}
        for row, contact in enumerate(contacts):
            for col, value in enumerate([contact[1], contact[2], contact[3], contact[4], 
                                       groups.get(contact[5], ''), contact[6]]):
                item = QTableWidgetItem(str(value) if value else '')
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                self.contacts_table.setItem(row, col, item)
        if not contacts:
            self.contacts_table.setRowCount(1)
            item = QTableWidgetItem(LANGUAGES[self.current_lang]['no_contacts'])
            item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.contacts_table.setItem(0, 0, item)

    def load_groups(self):
        groups = self.db.get_all_groups()
        self.groups_table.setRowCount(len(groups))
        for row, group in enumerate(groups):
            item = QTableWidgetItem(group[1])
            item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.groups_table.setItem(row, 0, item)
        self.group_combo.clear()
        self.group_combo.addItem(LANGUAGES[self.current_lang]['all_groups'], 0)
        for group in groups:
            self.group_combo.addItem(group[1], group[0])

    def add_contact(self):
        dialog = AddContactDialog(self.db, self.current_lang, self)
        if dialog.exec():
            name = dialog.name_input.text()
            phone = dialog.phone_input.text()
            email = dialog.email_input.text()
            address = dialog.address_input.text()
            group_id = dialog.group_combo.currentData()
            birthday = dialog.birthday_input.date().toString('yyyy-MM-dd')
            notes = dialog.notes_input.toPlainText()
            self.db.add_contact(name, phone, email, address, group_id, birthday, notes)
            self.load_contacts()
            QMessageBox.information(self, 'Success', LANGUAGES[self.current_lang]['contact_added'])

    def edit_contact(self):
        selected = self.contacts_table.selectedItems()
        if not selected:
            return
        row = selected[0].row()
        contact_id = self.db.get_all_contacts(self.group_combo.currentData(), self.search_input.text())[row][0]
        contact = self.db.get_all_contacts()[row]
        dialog = AddContactDialog(self.db, self.current_lang, self)
        dialog.setWindowTitle(LANGUAGES[self.current_lang]['edit_contact'])
        dialog.name_input.setText(contact[1])
        dialog.phone_input.setText(contact[2])
        dialog.email_input.setText(contact[3])
        dialog.address_input.setText(contact[4])
        dialog.group_combo.setCurrentIndex(dialog.group_combo.findData(contact[5] if contact[5] else 0))
        dialog.birthday_input.setDate(QDate.fromString(contact[6], 'yyyy-MM-dd') if contact[6] else QDate.currentDate())
        dialog.notes_input.setText(contact[7])
        if dialog.exec():
            name = dialog.name_input.text()
            phone = dialog.phone_input.text()
            email = dialog.email_input.text()
            address = dialog.address_input.text()
            group_id = dialog.group_combo.currentData()
            birthday = dialog.birthday_input.date().toString('yyyy-MM-dd')
            notes = dialog.notes_input.toPlainText()
            self.db.update_contact(contact_id, name, phone, email, address, group_id, birthday, notes)
            self.load_contacts()
            QMessageBox.information(self, 'Success', LANGUAGES[self.current_lang]['contact_updated'])

    def delete_contact(self):
        selected = self.contacts_table.selectedItems()
        if not selected:
            return
        row = selected[0].row()
        contact_id = self.db.get_all_contacts(self.group_combo.currentData(), self.search_input.text())[row][0]
        if QMessageBox.question(self, 'Confirm', LANGUAGES[self.current_lang]['delete_confirm']) == QMessageBox.StandardButton.Yes:
            self.db.delete_contact(contact_id)
            self.load_contacts()
            QMessageBox.information(self, 'Success', LANGUAGES[self.current_lang]['contact_deleted'])

    def add_group(self):
        dialog = AddGroupDialog(self.current_lang, self)
        if dialog.exec():
            group_name = dialog.group_name.text()
            self.db.add_group(group_name)
            self.load_groups()
            self.load_contacts()
            QMessageBox.information(self, 'Success', LANGUAGES[self.current_lang]['group_added'])

    def delete_group(self):
        selected = self.groups_table.selectedItems()
        if not selected:
            return
        row = selected[0].row()
        group_id = self.db.get_all_groups()[row][0]
        if QMessageBox.question(self, 'Confirm', LANGUAGES[self.current_lang]['group_delete_confirm']) == QMessageBox.StandardButton.Yes:
            self.db.delete_group(group_id)
            self.load_groups()
            self.load_contacts()
            QMessageBox.information(self, 'Success', LANGUAGES[self.current_lang]['group_deleted'])

    def export_to_csv(self):
        try:
            contacts = self.db.get_all_contacts()
            groups = {g[0]: g[1] for g in self.db.get_all_groups()}
            with open('contacts.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Phone', 'Email', 'Address', 'Group', 'Birthday', 'Notes'])
                for contact in contacts:
                    group_name = groups.get(contact[5], '') if contact[5] else ''
                    writer.writerow([contact[1], contact[2], contact[3], contact[4], group_name, contact[6], contact[7]])
            QMessageBox.information(self, 'Success', LANGUAGES[self.current_lang]['export_success'].format('contacts.csv'))
        except Exception as e:
            QMessageBox.critical(self, 'Error', LANGUAGES[self.current_lang]['export_error'].format(str(e)))

    def check_birthdays(self):
        birthdays = self.db.get_upcoming_birthdays()
        if birthdays:
            message = '\n'.join([LANGUAGES[self.current_lang]['birthday_reminder'].format(name, date) for name, date in birthdays])
            self.birthdays_label.setText(message)
            self.tray_icon.showMessage('Birthday Reminder', message, QSystemTrayIcon.MessageIcon.Information)
        else:
            self.birthdays_label.setText(LANGUAGES[self.current_lang]['no_birthdays'])

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage('Smart Phonebook', 'Application minimized to tray', QSystemTrayIcon.MessageIcon.Information)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Windows'))
    window = SmartPhonebook()
    window.show()
    sys.exit(app.exec())