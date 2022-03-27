from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

#setup settings
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['appium:platformVersion'] = '11.0'
desired_caps['appium:deviceName'] = 'Pixel 4 XL API 30'
desired_caps['appium:automationName'] = 'UiAutomator2'
desired_caps['appium:appPackage'] = 'com.saucelabs.mydemoapp.rn'
desired_caps['appium:appActivity'] = 'MainActivity'

#set driver
localApiumUrl = 'http://127.0.0.1:4723/wd/hub'
driver = webdriver.Remote(localApiumUrl, desired_caps)

driver.implicitly_wait(30)

#tests
driver.find_element(AppiumBy.XPATH, '//*[@content-desc="container header"]').is_displayed()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'container header').is_displayed()

productHeader = driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="container header"]')\
    .find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView').get_attribute('text')

print(productHeader)

#quit from app after all tests
driver.quit()