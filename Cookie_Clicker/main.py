from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="/Users/berkebolukkaya/Desktop/drivers/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")



WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//div[@class='langSelectButton title' and text()='English']"))
)
language = driver.find_element(By.XPATH,"//div[@class='langSelectButton title' and text()='English']")
language.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)
print("COOKIE FOUND")


cookie = driver.find_element(By.ID, "bigCookie")
time.sleep(3)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))

    for i in range(4):
        product_price = driver.find_element(By.ID, "productPrice" + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, "product" + str(i))
            product.click()
            break