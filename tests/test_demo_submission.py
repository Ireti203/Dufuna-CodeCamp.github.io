from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_demo_submission():

    driver = webdriver.Chrome()

    driver.get("https://Dufuna-CodeCamp.github.io")

    driver.assertEqual("Taries Empire", driver.title)

    driver.find_element_by_id("quantityNumber").send_keys("5")

    driver.assertEqual("187.50", driver.find_element_by_id("shippingCost").text)
    driver.assertEqual("1437.50", driver.find_element_by_id("totalCost").text)

    driver.find_element_by_id("buyNow").click()

    # check that button is disabled if no quantity is specified or quantity is less than 1
    driver.find_element_by_id("quantityNumber").send_keys("0")
    driver.assertFalse(True, driver.is_enabled("#buyNow"))

    # check input fields
    driver.find_element_by_id("newsletter").send_keys("ire@mail")
    driver.find_element_by_id("requiredField").submit()
    failure = driver.find_element_by_class_name('errorMessage').text
    driver.assertEqual(failure, "Please enter a valid mail")
        
    driver.find_element_by_link_text("Contact Us").click()

    # Type or update text input fields
    driver.find_element_by_id("fullName").send_keys("Arinola Badejo")
    driver.find_element_by_id("email").send_keys("remi")
    driver.find_element_by_id("order_id").send_keys("56")
    driver.find_element_by_id("validateForm").submit()

    driver.assertTrue(True, driver.is_element_visible(".error-block"))

    # Navigate to Register page
    driver.find_element_by_link_text("Register").click()

    driver.find_element_by_id("firstName").send_keys("Arinola")
    driver.find_element_by_id("lastName").send_keys("Badejo")
    driver.find_element_by_id("phoneNumber").send_keys("09087676789")
    driver.find_element_by_id("email").send_keys("rinola@mail.com")
    driver.find_element_by_id("password").send_keys("Customer1")
    driver.find_element_by_id("confirmPassword").send_keys("Customer")
    driver.find_element_by_id("terms-conditions").click()
    driver.find_element_by_id("submit_form").submit()

    driver.assertTrue(True, driver.is_element_visible(".error-block"))