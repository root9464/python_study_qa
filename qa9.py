from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://platform.kodland.org/ru/course_604/'
login = 'echervonnyj'
password = '19409'
driver.get(url)
time.sleep(1)
m = driver.find_element(By.NAME, 'login')
z = driver.find_element(By.NAME, 'password')
o = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/form/button')
array = []
m.send_keys(login)
z.send_keys(password)
time.sleep(1)
o.click()
time.sleep(2)
def submit_task(url):
    
    driver.get(url)
    h = driver.find_element(By.ID, 'sub-button')
    h.click()
    j = driver.find_element(By.ID, 'submit_task_button')
    j.click()
    time.sleep(1)
    #button w100 send-survey
#================================================================

p = driver.find_elements(By.CLASS_NAME, 'lesson-wrapper')
u = int(input('Номер урока:'))
inp = p[u - 1].find_elements(By.CLASS_NAME, 'task-link')
for i in inp:
    array.append(i.get_attribute('href'))
for i in array:
    submit_task(i)
    time.sleep(0.5)