from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
import pandas as pd


print("sample test case started")  
driver = webdriver.Chrome()  
driver.maximize_window()  

df = pd.read_excel("Book1.xlsx")

# print(df.head())
data = []

# print(df.head())

for key, value in df.iterrows():
    temp = []
    for every in value:
        print(every)
        temp.append(every)
    data.append(temp)


print()
print()
print(len(data))


#navigate to the url  
driver.get("https://projects.syzygillc.com/entries/new")  


time.sleep(3)  

username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')

username = 'aj-work3256-4'
password = 'Work@3256'


username_field.send_keys(username)
password_field.send_keys(password)

time.sleep(3)  

login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()
time.sleep(2)


for j in range(len(data)):
    for i in range(5, 16):
        driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/div/form/div/div[2]/div/div[4]/div/div[{i}]/div/input").send_keys(data[j][i - 5])

    time.sleep(2)
    driver.save_screenshot(f'screenshot_{j}.png')
    time.sleep(3)
    driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/div/form/div/div[2]/div/div[4]/div/div[16]/div/div/button").click()
    time.sleep(10)
        # login_button.click()


time.sleep(5)
input("hiiii")
# driver.close()  
# print("sample test case successfully completed")  
