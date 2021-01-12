from seleniumbase import BaseCase

class MyTestCase(BaseCase):

    def test_demo_submission(self):
        self.open("https://Dufuna-CodeCamp.github.io")

        self.assert_title("Taries Empire")

        #self.click_link_text("Product Page")    #test navigation links
        self.type("#quantityNumber", "5")

        self.assert_text("187.50", "#shippingCost")
        self.assert_text("1437.50", "#totalCost")

        self.click("#buyNow")

        # check that button is disabled if no quantity is specified or quantity is less than 1

        self.type("#quantityNumber", "0")
        self.assert_false(self.is_enabled("#buyNow"))

        # check input fields
        self.type("#newsletter", "ire@mail")
        self.find_element_by_id("requiredField").submit()
        self.failure = self.get_attribute('textContent', '.errorMessage')
        self.assertEquals(self.failure, "Please enter a valid mail")
        
        self.click_by_link_text("Contact Us")
        self.assert_exact_text("Please contact us via these numbers", "h3")

        # Type or update text input fields
        self.type("#fullName", "Arinola Badejo")
        self.type("#email", "remi")
        self.type("#order_id", "56")
        self.find_element_by_id("validateForm").submit()

        self.assert_true(self.is_element_visible(".error-block"))

        # Navigate to Register page
        self.click_link_text("Register")

        self.type("#firstName", "Arinola")
        self.type("#lastName", "Badejo")
        self.type("#phoneNumber", "09087676789")
        self.type("#email", "rinola@mail.com")
        self.type("#password", "Customer1")
        self.type("#confirmPassword", "Customer")
        self.click("#terms-conditions")
        self.find_element_by_id("submit_form").submit()

        self.assert_true(self.is_element_visible(".error-block"))

        self.assert_no_404_errors()

        self.assert_no_js_errors()