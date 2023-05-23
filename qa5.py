from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://ru.wikipedia.org/wiki/Список_государств")
soup = BeautifulSoup(driver.page_source, 'html.parser')
sl = {
     
}
domen = "https://ru.wikipedia.org"
for i in soup.find(class_ = "wikitable").find_all('a'): 
    
    io = i.get('href')
    if "/wiki/" in io :
        sl[i.text] = domen + io
print(sl)
