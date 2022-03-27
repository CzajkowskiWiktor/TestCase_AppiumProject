from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['appium:platformVersion'] = '12.0'
desired_caps['appium:deviceName'] = 'Google Pixel 4 XL GoogleAPI Emulator'
desired_caps['appium:app'] = 'storage:filename=Android-MyDemoAppRN.1.1.0.build-226.apk'
desired_caps['appium:appiumVersion'] = '1.22.1'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['sauce:options'] = {}
desired_caps['sauce:options']['appiumVersion'] = '1.22.1'
desired_caps['sauce:options']['username'] = 'oauth-malyczaja12-d3f94'
desired_caps['sauce:options']['accessKey'] = 'bf2d009a-fc4a-42ff-9e04-36495aa8ab0f'
labUrl = 'https://ondemand.eu-central-1.saucelabs.com:443/wd/hub'

driver = webdriver.Remote(labUrl, desired_caps)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH, '//*[@content-desc="container header"]').is_displayed()
driver.quit()