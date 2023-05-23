from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
page = driver.page_source
o = 0

array = ["http://io.pythonanywhere.com/form/?next=%2Fapp%2F", "https://ya.ru/"]
for i in array:
    with open(f"QA/page{o}.html", "w" , encoding='utf-8') as tabs:
        o += 1
        driver.get(i)
        a = driver.page_source 
        tabs.write(a)
driver.quit() 