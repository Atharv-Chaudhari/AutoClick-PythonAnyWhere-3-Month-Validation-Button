from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule


def fun():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

    driver.get("YOUR_URL_OF PROJECT_WEB_SECTION")

    element = driver.find_element(By.ID, "id_auth-username")
    element.send_keys("YOUR_USERNAME or YOUR_EMAIL")
    element = driver.find_element(By.ID, "id_auth-password")
    element.send_keys("YOUR_PASSWORD")
    element = driver.find_element(By.ID, "id_next").click()
    element = driver.find_element(By.CSS_SELECTOR, "[value='Run until 3 months from today']").click()
    time.sleep(5)
    print("Button Have been Clicked Successfully..!!!")
    driver.close()

schedule.every().monday.do(fun)

while True:
    schedule.run_pending()
    time.sleep(1)
