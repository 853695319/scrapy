from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == "__main__":
    options = Options()
    options.headless = True
    driver = Firefox(executable_path=r"l:\code\scrapy\Selenium\geckodriver.exe", options=options)
    wait = WebDriverWait(driver, timeout=10)
    driver.get('https://www.baidu.com')
    wait.until(expected.visibility_of_element_located((By.ID, 'kw'))).send_keys('headless firefox' + Keys.ENTER)
    driver.save_screenshot("headless_firefox.png")
    # wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#3>h3>a'))).click()
    print(driver.current_url)
    driver.quit()
