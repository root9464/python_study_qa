from bs4 import BeautifulSoup

html_doc = """
<html><head><title>История моей жизниy</title></head>
<body>
<p class="title"><b>История моей жизни</b></p>

<p class="story">У меня есть три сестры:
<a href="http://example.com/vera" class="sister" id="link1">Вера</a>,
<a href="http://example.com/nadjda" class="sister" id="link2">Надежда</a> and
<a href="http://example.com/lubov" class="sister" id="link3">Любовь</a>;
И все у них хорошо</p>

<p class="story">...</p>
"""
dt = {
   
}


soup = BeautifulSoup(html_doc, 'html.parser')
for i in soup.find_all('a'): 
    io = i.get('href')
    dt[i.text] = io

print(dt)

















