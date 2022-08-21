import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web = Chrome()
web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
web.implicitly_wait(5)

web.get('https://www.southwest.com/')

time.sleep(1)

web.find_element(by=By.XPATH, value='//*[@id="LandingAirBookingSearchForm_originationAirportCode"]').send_keys('LAX')
time.sleep(0.3)
web.find_element(by=By.XPATH, value='//*[@id="LandingAirBookingSearchForm_destinationAirportCode"]').send_keys('SFO')
time.sleep(0.3)
web.find_element(by=By.XPATH, value='//*[@id="LandingAirBookingSearchForm_departureDate"]').send_keys(Keys.BACKSPACE,
                                                                                                      Keys.BACKSPACE,
                                                                                                      Keys.BACKSPACE,
                                                                                                      Keys.BACKSPACE,
                                                                                                      Keys.BACKSPACE,
                                                                                                      '9/5')
time.sleep(0.3)
web.find_element(by=By.XPATH, value='//*[@id="LandingAirBookingSearchForm_returnDate"]').send_keys('9/11')
time.sleep(0.3)
el = web.find_element(by=By.XPATH, value='//*[@id="LandingAirBookingSearchForm_submit-button"]')
el.click()

li_list = web.find_elements(by=By.XPATH, value='//*[@id="air-search-results-matrix-0"]/li')

for li in li_list:
    start_time = li.find_element(by=By.XPATH, value='./div[2]/span').text
    end_time = li.find_element(by=By.XPATH, value='./div[3]/span').text
    total_time = li.find_element(by=By.XPATH, value='./div[5]').text
    try:
        bs_cost = li.find_element(by=By.XPATH,
                                  value='./div[6]/div/div[1]/button/span/span/span/span/span').text
        any_cost = li.find_element(by=By.XPATH,
                                   value='./div[6]/div/div[2]/button/span/span/span/span/span').text
        wgap_cost = li.find_element(by=By.XPATH,
                                    value='./div[6]/div/div[3]/button/span/span/span/span/span').text
        wga_cost = li.find_element(by=By.XPATH,
                                   value='./div[6]/div/div[4]/div[4]/button/span/span/span/span/span').text
        print(start_time, end_time, total_time, bs_cost, any_cost, wgap_cost, wga_cost)
    except:
        print(start_time, end_time, total_time)
