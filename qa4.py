from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
from collections import defaultdict
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


op = defaultdict(list)


for k in range(1, 2):

    driver.get(f"https://nekdo.ru/page/{k}/")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    io = soup.find_all(class_ = "text")


    for i,b in zip(io ,soup.find_all(class_ = "cat")):
        x = b.find_all(class_ = 'link')
        for h in x:
            op[h.text].append(i.text)
print(op['прочие'])

# with open("json.json", "w", encoding="utf-8") as f:
#     json.dump(op, f, ensure_ascii=False )






















    # for i in io:
    #     op.append(i.text)

