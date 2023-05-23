from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(ChromeDriverManager().install())

# hub_card_item
url = 'https://platform.kodland.org/ru/courses/'
login = 'echervonnyj'
password = '19409'
driver.get(url)

time.sleep(2)
m = driver.find_element(By.NAME, 'login')
z = driver.find_element(By.NAME, 'password')
o = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/form/button')
set = {}
m.send_keys(login)
z.send_keys(password)
time.sleep(1)
o.click()
time.sleep(2)
start_time = time.time()
h = driver.find_elements(By.CLASS_NAME, 'hub_card_item')

for i in h[1:]:
    x = i.find_element(By.CLASS_NAME, 'hub-card-main__title')
    q = i.find_element(By.CLASS_NAME, 'like-links__btns')
    set[x.text] = q.text.split("\n")
    
# e = driver.find_elements(By.CLASS_NAME, 'like-links__btns')
# for i in h[1:]:
#     u = driver.find_elements(By.CLASS_NAME, 'hub-card-main__title')
# for x,q in zip(u,e):
#     set[x.text] = q.text.split("\n")

print(set)
elapsed_time = time.time() - start_time
print('finished in {} ms'.format(int(elapsed_time * 1_000)))