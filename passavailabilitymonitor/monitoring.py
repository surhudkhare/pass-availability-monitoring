from passavailabilitymonitor.utils import get_date_string
from passavailabilitymonitor import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import time
load_dotenv()

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")  # Disable notifications
chrome_options.add_argument("--disable-popup-blocking")  # Disable pop-up blocking


def check_availability(trail, target_date):
    try:
        park_name=config.TRAILS[trail]['PARK_NAME']
        trail_name=config.TRAILS[trail]['TRAIL_NAME']
        desired_date_string=get_date_string(target_date)
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(config.BCPARKS_URL)
        wait = WebDriverWait(driver, 20)

        park_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[contains(@aria-label, '{park_name}')]"))
        )
        park_button.click()


        date_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//app-date-picker/fieldset"))
        )
        date_dropdown.click()

        date_selector = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='gridcell' and @aria-label='{desired_date_string}']"))
        )
        date_selector.click()

        time.sleep(3)

        dropdown_element = wait.until(EC.element_to_be_clickable((By.ID, 'passType')))
        dropdown_element.click()

        trail_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//option[contains(text(), '{trail_name}')]")))
        trail_option.click()

        blank_area = driver.find_element(By.TAG_NAME, 'body')
        blank_area.click()

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card')))

        # Find all card elements
        cards = driver.find_elements(By.CSS_SELECTOR, '.card-input')

        # Iterate over each card element and extract AM/PM or "ALL DAY" and availability
        availability = False
        for card in cards:
            if 'card-enabled' in card.get_attribute('class'):
                availability = True
        return availability
    finally:
        driver.quit()


if __name__ == "__main__":
    cheakamus_avail = check_availability(trail="CHEAKAMUS", target_date="2024-07-25")
    print(cheakamus_avail)