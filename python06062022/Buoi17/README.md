#1/ Dựng lại database MySQL

- Mở web: localhost/phpmyadmin (máy ở trung tâm đã có gói XAMPP)
- Tạo mới database:
  - Chọn Tab "Database"
  - Nhập database name, vd "pythonnn" và chọn collation: "utf8_unicode_ci"
- Chọn database "pythonnn"
- Chọn Import --> Choose File *.sql --> bấm GO

# 2/ Restore môi trường ảo từ file requirements.txt

* Vào thư mục project (vd Buoi17)
* Mở command line
* Gõ ```python -m venv venv```
* Active môi trường ảo:
  * ```.\venv\Scripts\activate```
* Dựng lại các package cho môi trường
  * ```pip install -r requirements.txt```

