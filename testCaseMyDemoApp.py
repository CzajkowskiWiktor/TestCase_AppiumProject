import unittest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# TESTCASE - CHECK IF PRODUCT IS ADDED TO CART WITH PROPER PRICE
# STEP 1) on main page: check if mainPage is Loaded
# STEP 2) on main page: click on product -> redirect to product page
# STEP 3) on product page: a) check product name b) check product price c) check if add to card button d) check image is displayed
# STEP 4) on product page: click add to cart button -> check if product is added to cart
# STEP 5) on product page: click cart button: navigate to cart page
# STEP 6) on cart page: check if cart page is displayed: a) check header b) check product name
# c) check product price d) check proceed to checkout d) check image is displayed e) check footer
# STEP 7) on cart page: click proceed to checkout
# STEP 8) on login page: check Login Page is loaded
# STEP 9) on login page: type username, type password, click login button
# STEP 10) on checkout page: checkout page is displayed
# STEP 11) on checkout shipping address page: enter data, shipping address, click to payment
# STEP 12) on checkout payment page: enter data, payment method, click to payment
# STEP 13) on checkout review order page: review order
# STEP 14) on checkout complete page: completed order and conitnue shopping

class TestCaseMyDemoApp(unittest.TestCase):

    def setUp(self):
        # setup settings
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['appium:platformVersion'] = '11.0'
        desired_caps['appium:deviceName'] = 'Pixel 4 XL API 30'
        desired_caps['appium:automationName'] = 'UiAutomator2'
        desired_caps['appium:appPackage'] = 'com.saucelabs.mydemoapp.rn'
        desired_caps['appium:appActivity'] = 'MainActivity'
        # set driver
        localApiumUrl = 'http://127.0.0.1:4723/wd/hub'
        self.driver = webdriver.Remote(localApiumUrl, desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_smoke_launchApplication(self):
        self.driver.find_element(AppiumBy.XPATH, '//*[@content-desc="container header"]').is_displayed()
        self.driver.find_element(AppiumBy.XPATH, '//*[@content-desc="container header"]/*[@text="Products"]').is_displayed()

    def test_validateIfUserCanBuyProduct(self):
        # STEP 1
        self.driver.find_element(AppiumBy.XPATH, '//*[@content-desc="container header"]').is_displayed()
        self.driver.find_element(AppiumBy.XPATH,
                                 '//*[@content-desc="container header"]/*[@text="Products"]').is_displayed()
        # STEP 2
        products = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'store item')
        product_title = products[1].find_element(AppiumBy.ACCESSIBILITY_ID, 'store item text').get_attribute('text')
        product_price = products[1].find_element(AppiumBy.ACCESSIBILITY_ID, 'store item price').get_attribute('text')
        print(product_price, product_title)
        products[1].click()

        #STEP 3
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//*[@text="Sauce Labs Bike Light"]')))
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Add To Cart button').is_displayed()
        product_headerElement = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'container header')
        product_headerElement.is_displayed()
        product_headerText = product_headerElement.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text]').get_attribute('text')
        product_priceText = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'product price').get_attribute('text')
        self.assertEqual(product_title, product_headerText, 'Product name is different than expected')
        self.assertEqual(product_price, product_priceText, 'Product price is different than expected')


        #STEP 4
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Add To Cart button').click()
        cartElement = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'cart badge')
        product_cartNumber = cartElement.find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView').get_attribute('text')
        self.assertEqual('1', product_cartNumber)

        #STEP 5
        cartElement.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//*[@text="My Cart"]')))
        proceedToCheckoutButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Proceed To Checkout button')
        proceedToCheckoutButton.is_displayed()

        #STEP 6
        #checking product details in Cart Page
        cart_productLabel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'product label').get_attribute('text')
        cart_productPrice = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'product price').get_attribute('text')
        cart_productAmount = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'counter amount').\
            find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView').get_attribute('text')
        self.assertEqual(product_title, cart_productLabel)
        self.assertEqual(product_price, cart_productPrice)
        self.assertEqual('1', cart_productAmount)
        #checking footer in Cart Page
        cart_checkoutFooter = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'checkout footer')
        childFooterElements = cart_checkoutFooter.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')
        self.assertEqual(childFooterElements[0].get_attribute('text'), 'Total:')
        self.assertEqual(childFooterElements[1].get_attribute('text'), '1 item')
        self.assertEqual(childFooterElements[2].get_attribute('text'), product_price)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'remove item')

        #STEP 7
        proceedToCheckoutButton.click()

        #STEP 8
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//*[@content-desc="container header"]/*[@text="Login"]')))
        loginButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Login button')
        loginButton.is_displayed()
        self.driver.find_element(AppiumBy.XPATH, '//*[@content-desc="container header"]/*[@text="Login"]').is_displayed()

        #STEP 9
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Username input field').send_keys('bob@example.com')
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Password input field').send_keys('10203040')
        loginButton.click()

        #STEP 10
        paymentButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'To Payment button')
        paymentButton.is_displayed()
        self.driver.find_element(AppiumBy.XPATH, '//*[@content-desc="container header"]/*[@text="Checkout"]').is_displayed()
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="Enter a shipping address"]').is_displayed()

        #STEP 11
        inputEditElements = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.EditText')
        inputEditElements[0].send_keys('Bob Winter')
        inputEditElements[1].send_keys('Polanka 12')
        inputEditElements[2].send_keys('mieszkanie 5')
        inputEditElements[3].send_keys('Poznan')
        inputEditElements[4].send_keys('Wielkopolska')
        inputEditElements[5].send_keys('61-131')
        inputEditElements[6].send_keys('Polska')
        self.assertEqual(inputEditElements[0].get_attribute('text'), 'Bob Winter')
        self.assertEqual(inputEditElements[1].get_attribute('text'), 'Polanka 12')
        self.assertEqual(inputEditElements[2].get_attribute('text'), 'mieszkanie 5')
        self.assertEqual(inputEditElements[3].get_attribute('text'), 'Poznan')
        self.assertEqual(inputEditElements[4].get_attribute('text'), 'Wielkopolska')
        self.assertEqual(inputEditElements[5].get_attribute('text'), '61-131')
        self.assertEqual(inputEditElements[6].get_attribute('text'), 'Polska')
        paymentButton.click()
        # version 2 of sending keys to app
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Full Name* input field').send_keys('Bob Winter')
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Address Line 1* input field').send_keys('Polanka 12')
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Address Line 2 input field').send_keys('mieszkanie 5')
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'City* input field').send_keys('Poznan')
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Address Line 1* input field').send_keys('Wielkopolska')
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Address Line 1* input field').send_keys('61-131')
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Address Line 1* input field').send_keys('Polska')

        #STEP 12
        reviewOrderButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Review Order button')
        reviewOrderButton.is_displayed()
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="Enter a payment method"]').is_displayed()
        inputEditCardElements = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.EditText')
        inputEditCardElements[0].send_keys('Bob Winter')
        inputEditCardElements[1].send_keys('4116422061177316')
        inputEditCardElements[2].send_keys('03/25')
        inputEditCardElements[3].send_keys('511')
        self.assertEqual(inputEditCardElements[0].get_attribute('text'), 'Bob Winter')
        self.assertEqual(inputEditCardElements[1].get_attribute('text'), '4116 4220 6117 7316')
        self.assertEqual(inputEditCardElements[2].get_attribute('text'), '03/25')
        self.assertEqual(inputEditCardElements[3].get_attribute('text'), '511')
        reviewOrderButton.click()

        #STEP 13
        placeOrderButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Place Order button')
        placeOrderButton.is_displayed()
        self.driver.find_element(AppiumBy.XPATH,
                                 '//*[@content-desc="container header"]/*[@text="Checkout"]').is_displayed()
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="Review your order"]').is_displayed()
        review_productLabel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'product label').get_attribute('text')
        review_productPrice = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'product price').get_attribute('text')
        self.assertEqual(product_title, review_productLabel)
        self.assertEqual(product_price, review_productPrice)
        # checking footer in Review Page
        review_checkoutFooter = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'checkout footer')
        reviewFooterElements = review_checkoutFooter.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')
        self.assertEqual(reviewFooterElements[0].get_attribute('text'), 'Total:')
        self.assertEqual(reviewFooterElements[1].get_attribute('text'), '1 item')
        self.assertEqual(reviewFooterElements[2].get_attribute('text'), '$15.98')
        placeOrderButton.click()

        #STEP 14
        continueShoppingButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Continue Shopping button')
        continueShoppingButton.is_displayed()
        self.driver.find_element(AppiumBy.XPATH,
                                 '//*[@text="Checkout Complete"]').is_displayed()
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="Your new swag is on its way"]').is_displayed()
        continueShoppingButton.click()


