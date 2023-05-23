from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://ru.wikipedia.org/wiki/Список_государств")
soup = BeautifulSoup(driver.page_source, 'html.parser')
sl = {
     
}


io = soup.find(class_ = "wikitable")
io.get('href')
print(io)
