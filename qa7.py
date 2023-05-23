from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'http://tempname09488853983.pythonanywhere.com/form/'
password = 'qwerty7q8q1579'
login = '+79501831100'
driver.get(url)

m = driver.find_element(By.NAME, 'password')
z = driver.find_element(By.NAME, 'number')
o = driver.find_element(By.XPATH, '/html/body/div[2]/div/form[1]/div/input[3]')

z.send_keys(login)
m.send_keys(password)
o.click()
time.sleep(4)
if driver.current_url == 'http://tempname09488853983.pythonanywhere.com/home/':
    print('работает')