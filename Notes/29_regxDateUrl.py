import re
url = r'https://example.com/2024/12/15/article-title'
y = re.findall('[0-9]+',url)
print(y)