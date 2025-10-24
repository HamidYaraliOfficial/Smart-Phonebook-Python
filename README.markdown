# Smart Phonebook - README

## English

### Overview
Smart Phonebook is a modern, user-friendly application designed for managing contacts efficiently. Built using **PyQt6** and **SQLite**, it offers a robust solution for personal and business contact organization. The application supports multiple languages (English, Persian, Chinese, and Russian) and features customizable themes inspired by Windows 11, including Default, Light, Dark, Red, and Blue themes. It provides an intuitive interface with right-to-left and left-to-right text alignment based on the selected language.

### Features
- **Contact Management**: Add, edit, and delete contacts with details such as name, phone, email, address, group, birthday, and notes.
- **Advanced Search**: Search contacts by name, phone, or email with real-time filtering.
- **Group Organization**: Create and manage contact groups for better organization.
- **CSV Export**: Export all contacts to a CSV file for easy sharing or backup.
- **Birthday Reminders**: Receive system tray notifications for upcoming birthdays within the next 7 days.
- **Multilingual Support**: Switch between English, Persian, Chinese, and Russian languages seamlessly.
- **Customizable Themes**: Choose from Windows Default, Light, Dark, Red, or Blue themes for a personalized experience.
- **System Tray Integration**: Minimize the application to the system tray for quick access.

### Requirements
- **Python**: Version 3.9 or higher
- **PyQt6**: For the graphical user interface
- **qdarkstyle**: For Light and Dark theme support
- **SQLite**: Included with Python for database management

### Installation
1. Ensure Python 3.9+ is installed on your system.
2. Install the required packages:
   ```bash
   pip install PyQt6 qdarkstyle
   ```
3. Download the `smart_phonebook.py` file from the repository.
4. Run the application:
   ```bash
   python smart_phonebook.py
   ```

### Usage
1. **Launch the Application**: Run the script to open the main window.
2. **Add a Contact**: Use the toolbar or menu to open the "Add Contact" dialog and enter contact details.
3. **Edit/Delete Contacts**: Select a contact from the table and use the toolbar options to edit or delete.
4. **Search Contacts**: Type in the search bar to filter contacts by name, phone, or email.
5. **Manage Groups**: Navigate to the "Groups" tab to create or delete groups.
6. **Export Contacts**: Use the "Export to CSV" option to save contacts to a file.
7. **Change Language/Theme**: Go to the "Settings" tab to select your preferred language and theme.
8. **Birthday Notifications**: Check the "Birthdays" tab or system tray for upcoming birthday reminders.

### Notes
- The application creates a `phonebook.db` SQLite database file in the same directory as the script.
- Ensure you have write permissions in the directory to create and modify the database.
- The system tray icon requires an `icon.png` file in the same directory for proper display. If not present, the tray icon may not show correctly.
- The application minimizes to the system tray when closed, and can be restored via the tray menu.

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## فارسی

### بررسی اجمالی
دفترچه تلفن هوشمند یک برنامه مدرن و کاربرپسند است که برای مدیریت مخاطبین به صورت کارآمد طراحی شده است. این برنامه با استفاده از **PyQt6** و **SQLite** ساخته شده و راه‌حلی قوی برای سازماندهی مخاطبین شخصی و تجاری ارائه می‌دهد. این برنامه از چندین زبان (انگلیسی، فارسی، چینی و روسی) پشتیبانی می‌کند و دارای تم‌های قابل تنظیم الهام گرفته از ویندوز 11، شامل تم‌های پیش‌فرض، روشن، تیره، قرمز و آبی است. رابط کاربری آن با توجه به زبان انتخابی، از چیدمان راست‌به‌چپ و چپ‌به‌راست پشتیبانی می‌کند.

### ویژگی‌ها
- **مدیریت مخاطبین**: افزودن، ویرایش و حذف مخاطبین با جزئیاتی مانند نام، تلفن، ایمیل، آدرس، گروه، تاریخ تولد و یادداشت‌ها.
- **جستجوی پیشرفته**: جستجوی مخاطبین بر اساس نام، تلفن یا ایمیل با فیلتر کردن در لحظه.
- **سازماندهی گروه‌ها**: ایجاد و مدیریت گروه‌های مخاطبین برای سازماندهی بهتر.
- **خروجی به CSV**: صدور تمام مخاطبین به فایل CSV برای اشتراک‌گذاری یا پشتیبان‌گیری آسان.
- **یادآور تولد**: دریافت اعلان‌های سینی سیستم برای تولدهای آینده در 7 روز بعدی.
- **پشتیبانی چندزبانه**: تغییر بین زبان‌های انگلیسی، فارسی، چینی و روسی به صورت یکپارچه.
- **تم‌های قابل تنظیم**: انتخاب از میان تم‌های پیش‌فرض ویندوز، روشن، تیره، قرمز یا آبی برای تجربه‌ای شخصی‌سازی‌شده.
- **یکپارچگی با سینی سیستم**: کمینه کردن برنامه به سینی سیستم برای دسترسی سریع.

### پیش‌نیازها
- **پایتون**: نسخه 3.9 یا بالاتر
- **PyQt6**: برای رابط کاربری گرافیکی
- **qdarkstyle**: برای پشتیبانی از تم‌های روشن و تیره
- **SQLite**: همراه با پایتون برای مدیریت پایگاه داده ارائه می‌شود

### نصب
1. اطمینان حاصل کنید که پایتون 3.9 یا بالاتر روی سیستم شما نصب است.
2. بسته‌های مورد نیاز را نصب کنید:
   ```bash
   pip install PyQt6 qdarkstyle
   ```
3. فایل `smart_phonebook.py` را از مخزن دانلود کنید.
4. برنامه را اجرا کنید:
   ```bash
   python smart_phonebook.py
   ```

### استفاده
1. **راه‌اندازی برنامه**: اسکریپت را اجرا کنید تا پنجره اصلی باز شود.
2. **افزودن مخاطب**: از نوار ابزار یا منو استفاده کنید تا گفتگوی «افزودن مخاطب» باز شود و جزئیات مخاطب را وارد کنید.
3. **ویرایش/حذف مخاطبین**: یک مخاطب را از جدول انتخاب کنید و از گزینه‌های نوار ابزار برای ویرایش یا حذف استفاده کنید.
4. **جستجوی مخاطبین**: در نوار جستجو تایپ کنید تا مخاطبین بر اساس نام، تلفن یا ایمیل فیلتر شوند.
5. **مدیریت گروه‌ها**: به تب «گروه‌ها» بروید تا گروه‌های جدید ایجاد یا حذف کنید.
6. **صدور مخاطبین**: از گزینه «خروجی به CSV» برای ذخیره مخاطبین در یک فایل استفاده کنید.
7. **تغییر زبان/تم**: به تب «تنظیمات» بروید تا زبان و تم مورد نظر خود را انتخاب کنید.
8. **اعلان‌های تولد**: تب «تولدها» یا سینی سیستم را برای یادآوری تولدهای آینده بررسی کنید.

### نکات
- برنامه یک فایل پایگاه داده SQLite به نام `phonebook.db` در همان دایرکتوری اسکریپت ایجاد می‌کند.
- اطمینان حاصل کنید که در دایرکتوری مجوز نوشتن دارید تا پایگاه داده ایجاد و اصلاح شود.
- آیکون سینی سیستم به یک فایل `icon.png` در همان دایرکتوری نیاز دارد تا به درستی نمایش داده شود. در صورت عدم وجود، آیکون سینی ممکن است به درستی نمایش داده نشود.
- برنامه هنگام بسته شدن به سینی سیستم کمینه می‌شود و می‌تواند از طریق منوی سینی بازیابی شود.

### مجوز
این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات، فایل `LICENSE` را ببینید.

---

## 中文

### 概述
智能电话簿是一款现代、用户友好的应用程序，旨在高效管理联系人。它使用 **PyQt6** 和 **SQLite** 构建，为个人和商业联系人组织提供了强大的解决方案。该应用程序支持多种语言（英语、波斯语、汉语和俄语），并提供受 Windows 11 启发的可定制主题，包括默认、亮色、暗色、红色和蓝色主题。根据所选语言，界面支持从右到左和从左到右的文本对齐。

### 功能
- **联系人管理**：添加、编辑和删除联系人，包含姓名、电话、电子邮件、地址、组、生日和备注等详细信息。
- **高级搜索**：通过姓名、电话或电子邮件实时过滤搜索联系人。
- **分组组织**：创建和管理联系人组以实现更好的组织。
- **CSV 导出**：将所有联系人导出到 CSV 文件，以便于共享或备份。
- **生日提醒**：在系统托盘中接收未来 7 天内生日的通知。
- **多语言支持**：在英语、波斯语、汉语和俄语之间无缝切换。
- **可定制主题**：从 Windows 默认、亮色、暗色、红色或蓝色主题中选择，获得个性化体验。
- **系统托盘集成**：将应用程序最小化到系统托盘以便快速访问。

### 要求
- **Python**：版本 3.9 或更高
- **PyQt6**：用于图形用户界面
- **qdarkstyle**：支持亮色和暗色主题
- **SQLite**：随 Python 提供，用于数据库管理

### 安装
1. 确保系统已安装 Python 3.9 或更高版本。
2. 安装所需包：
   ```bash
   pip install PyQt6 qdarkstyle
   ```
3. 从仓库下载 `smart_phonebook.py` 文件。
4. 运行应用程序：
   ```bash
   python smart_phonebook.py
   ```

### 使用
1. **启动应用程序**：运行脚本以打开主窗口。
2. **添加联系人**：使用工具栏或菜单打开“添加联系人”对话框并输入联系人详细信息。
3. **编辑/删除联系人**：从表格中选择一个联系人，并使用工具栏选项进行编辑或删除。
4. **搜索联系人**：在搜索栏中输入内容以按姓名、电话或电子邮件过滤联系人。
5. **管理分组**：导航到“分组”选项卡以创建或删除分组。
6. **导出联系人**：使用“导出到 CSV”选项将联系人保存到文件。
7. **更改语言/主题**：前往“设置”选项卡选择您喜欢的语言和主题。
8. **生日通知**：检查“生日”选项卡或系统托盘以获取即将到来的生日提醒。

### 注意事项
- 应用程序会在脚本所在目录中创建一个名为 `phonebook.db` 的 SQLite 数据库文件。
- 确保您在该目录中具有写入权限，以便创建和修改数据库。
- 系统托盘图标需要在同一目录中有一个 `icon.png` 文件以正确显示。如果不存在，托盘图标可能无法正确显示。
- 应用程序关闭时会最小化到系统托盘，并可通过托盘菜单恢复。

### 许可证
该项目根据 MIT 许可证发布。有关详细信息，请参阅 `LICENSE` 文件。