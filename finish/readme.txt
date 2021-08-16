- Sau khi clone repo về máy hãy mở terminal và chạy lệnh:
pip install virtualenv
- Sau đó cd đến thư mục lưu repo lần lượt chạy:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python
from app import db
db.create_all()
exit()
python app.py

