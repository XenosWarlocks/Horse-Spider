from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, JavascriptException
import time
import random

def human_like_delay(min_time=2, max_time=5):
    time.sleep(random.uniform(min_time, max_time))

def get_google_search_links(query, num_results=10, max_pages=15):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

    driver = webdriver.Chrome(options=options)

    search_url = f"https://www.google.com/search?q={query}&num={num_results}"
    driver.get(search_url)
    human_like_delay()

    all_links = []

    for page in range(max_pages):
        # Scroll down the page to simulate user activity
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        human_like_delay()

        # Extract links from the current page
        links = []
        results = driver.find_elements(By.CSS_SELECTOR, 'div.g a')
        for result in results:
            try:
                # Check if the element is displayed before interacting with it
                if result.is_displayed():
                    # Move the mouse to the element before clicking
                    ActionChains(driver).move_to_element(result).perform()
                    human_like_delay(1, 2)

                    url = result.get_attribute('href')
                    if url and "http" in url:
                        links.append(url)
            except (ElementNotInteractableException, JavascriptException) as e:
                print(f"Skipping element due to error: {e}")
                continue

        all_links.extend(links)

        # Find the "Next" button and click it if it exists
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'pnnext'))
            )
            ActionChains(driver).move_to_element(next_button).click().perform()
            human_like_delay()
        except (TimeoutException, JavascriptException) as e:
            print("No more pages or an error occurred:", e)
            break

    driver.quit()
    return all_links

