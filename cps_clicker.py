from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Check pinned timeline for delayed one(more safe)

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://cpstest.io")

try:
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "clickarea"))
    )
    click_button = driver.find_element(By.ID, "clickarea")

    
    while True:
        try:
            click_button.click()
            
        except Exception as e:
            print(f"An error occurred during clicking: {e}")
            break

except Exception as e:
    print(f"An error occurred while initializing the script: {e}")

finally:
    driver.quit()
