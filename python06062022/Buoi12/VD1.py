# Cài: pip install jinja2
from jinja2 import Template

my_template = '''
Xin chào {{ ho_ten }}.
Welcome to Python Course {{ id }}
'''
template = Template(my_template)
result = template.render(ho_ten="Nhất Nghệ", id=7777)
print(result)