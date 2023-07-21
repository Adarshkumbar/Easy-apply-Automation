from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = r"C:\Users\91623\Downloads\Development\chromedriver.exe"
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3413150810&f_AL=true&geoId=102713980&keywords=java%20developer&refresh=true")

sign_in = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

email = driver.find_element(By.XPATH, value="//*[@id='username']")
email.send_keys("u7776145@gmail.com")
time.sleep(5)

password = driver.find_element(By.XPATH, value="//*[@id='password']")
password.send_keys("danunaik@")
time.sleep(5)

submit = driver.find_element(By.XPATH, value="//*[@id='organic-div']/form/div[3]/button")
submit.click()
time.sleep(5)

job_list = driver.find_elements(By.CSS_SELECTOR, value=".jobs-search-results__list-item")
saved_jobs = []

for num in range(2, len(job_list)):
    try:
        job_found = driver.find_element(By.CLASS_NAME, value=f"jobs-search-two-pane__job-card-container--viewport-tracking-{num}")
        job_found.click()
        time.sleep(10)
        save = driver.find_element(By.XPATH, value="//*[@id='main']/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button")

        if save.text == "Save":
            save.click()
            time.sleep(10)
            saved_jobs.append(driver.find_element(By.XPATH, value="//*[@id='main']/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/h3").text)
    except NoSuchElementException:
        print("No Easy Apply Job Found")
        continue

print(saved_jobs)