# Nhớ cài pip install jinja2
from jinja2 import Template

template = Template('Hello {{ name }}. Phone: {{ phone}}')
result = template.render(name='Nhất Nghệ', phone='02839292174')
print(result)
