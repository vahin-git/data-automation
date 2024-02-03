# data entry-automation

This Python script utilizes the Selenium library to automate interactions with a web application. Let's break down the code and provide an explanation:

1. **Importing Libraries:**
   ```python
   from selenium import webdriver
   import time
   from selenium.webdriver.common.keys import Keys
   from selenium.webdriver.common.by import By
   import pandas as pd
   ```

   - The script imports necessary libraries: `webdriver` for browser automation, `time` for introducing delays, `Keys` for keyboard actions, `By` for specifying the method used to locate elements, and `pandas` for handling data from Excel.

2. **Setting up WebDriver:**
   ```python
   print("sample test case started")
   driver = webdriver.Chrome()
   driver.maximize_window()
   ```
   - The script prints a message and initializes a Chrome WebDriver, maximizing the browser window.

3. **Reading Data from Excel:**
   ```python
   df = pd.read_excel("Book1.xlsx")
   data = []

   for key, value in df.iterrows():
       temp = []
       for every in value:
           temp.append(every)
       data.append(temp)
   ```

   - The script reads data from an Excel file ("Book1.xlsx") using pandas, iterates through the rows, and appends the values to a list called `data`.

4. **Logging into a Website:**
   ```python
   driver.get("https://projects.syzygillc.com/entries/new")
   time.sleep(3)

   username_field = driver.find_element(By.ID, 'username')
   password_field = driver.find_element(By.ID, 'password')

   username = 'aj-work3256-4'
   password = 'Work@3256'

   username_field.send_keys(username)
   password_field.send_keys(password)
   login_button = driver.find_element(By.TAG_NAME, "button")
   login_button.click()
   time.sleep(2)
   ```
   - The script navigates to a website, locates login fields by ID, enters credentials, and clicks the login button.

5. **Entering Data into Form:**
   ```python
   for j in range(len(data)):
       for i in range(5, 16):
           driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/div/form/div/div[2]/div/div[4]/div/div[{i}]/div/input").send_keys(data[j][i - 5])
       time.sleep(2)
       driver.save_screenshot(f'screenshot_{j}.png')
       time.sleep(3)
       driver.find_element(By.XPATH, f"/html/body/div[3]/div/div/div[2]/div/form/div/div[2]/div/div[4]/div/div[16]/div/div/button").click()
       time.sleep(10)
   ```

   - The script iterates through each row of data, enters values into specific form fields, takes a screenshot, and clicks a submit button. There are also delays to allow for page loading.

6. **Closing the Browser:**
   ```python
   time.sleep(5)
   input("hiiii")
   # driver.close()
   # print("sample test case successfully completed")
   ```

   - The script introduces a delay and takes user input to keep the browser open. The last two lines are commented out but would close the browser and print a completion message.

To use this script, you need to have ChromeDriver installed and adjust paths accordingly. The Excel file structure and the HTML structure of the website being automated should match the script's expectations.
