from homework6.pages.ProductCartPage import ProductCartPage


class TestProductCartPage:
    def test_product_cart_page(self, browser):
        product_cart_page = ProductCartPage(browser)
        product_cart_page.find_element_by_locator(ProductCartPage.MAIN_PHOTO)
        product_cart_page.find_element_by_locator(ProductCartPage.LIKE_BUTTON)
        product_cart_page.find_element_by_locator(ProductCartPage.DESCRIPTION)
        product_cart_page.find_element_by_locator(ProductCartPage.DESCRIPTION)
        specification = product_cart_page.find_element_by_locator(ProductCartPage.SPECIFICATION)
        product_cart_page._simple_click_element(specification)
        processor_info = product_cart_page.waiting_element_visible(ProductCartPage.PROCESSOR_INFO)
        assert processor_info.text == 'Clockspeed 100mhz'
        product_cart_page.find_element_by_locator(ProductCartPage.ADD_TO_CART_BUTTON)
        reviewers = product_cart_page.find_element_by_locator(ProductCartPage.REVIEWERS)
        product_cart_page._simple_click_element(reviewers)
        continue_button = product_cart_page.find_element_by_locator(ProductCartPage.CONTINUE_BUTTON)
        product_cart_page._simple_click_element(continue_button)
        warning_info = product_cart_page.waiting_element_visible(ProductCartPage.WARNING_INFO)
        assert warning_info.text == 'Warning: Please select a review rating!'

