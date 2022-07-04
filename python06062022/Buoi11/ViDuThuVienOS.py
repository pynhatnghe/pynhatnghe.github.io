import os
from pathlib import Path

curr_dir = os.getcwd()
print('Thư mục đang đứng', curr_dir)
print(os.listdir(curr_dir))
parent_dir = Path(curr_dir).parent
print(parent_dir)
items = os.listdir(parent_dir)
print(items)
for m_item in items:
    print("m_item", m_item)
    full_path = os.path.join(parent_dir, m_item)
    print(full_path)
    if os.path.isdir(full_path):
        print("Là thư mục")
    elif os.path.isfile(full_path):
        print("Là file")