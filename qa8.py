from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://github.com/login'
login = 'root9464'
password = '7q8q1579'
driver.get(url)

def test_fullpage_screenshot():
    #the element with longest height on page
    ele=driver.find_element("xpath", '/html/body')
    total_height = ele.size["height"]+1000
    driver.set_window_size(1920, total_height)      #the trick
    time.sleep(2)
    driver.save_screenshot("screenshot1.png")
    driver.quit()


    
m = driver.find_element(By.NAME, 'login')
z = driver.find_element(By.NAME, 'password')
o = driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[12]')


m.send_keys(login)
z.send_keys(password)
o.click()
time.sleep(2)
if driver.current_url == 'https://github.com/':
    test_fullpage_screenshot()
