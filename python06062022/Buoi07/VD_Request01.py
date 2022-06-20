import requests

# Đọc trang nhatnghe.com
nhat_nghe_request = requests.get("http://nhatnghe.com")
print("STATUS:", nhat_nghe_request.status_code)
if nhat_nghe_request.status_code == 200:
    print(nhat_nghe_request.headers)
    print(nhat_nghe_request.text)
