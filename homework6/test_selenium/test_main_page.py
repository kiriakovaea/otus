from homework6.pages.MainPage import MainPage


class TestMainPage:
    def test_main_page(self, browser):
        main_page = MainPage(browser)
        main_page.find_search_input()
        main_page.find_search_button()
        main_page.find_main_image()
        empty_cart_text = main_page.get_empty_shopping_cart_text()
        assert empty_cart_text.text == 'Your shopping cart is empty!'

    def test_change_currency(self, browser):
        main_page = MainPage(browser)
        main_page.click_element(MainPage.CURRENCY_CHECKBOX)
        main_page.click_element(MainPage.EUR_CURRENCY)
        first_element_currency = main_page.find_element_by_locator(MainPage.FIRST_ELEMENT_PRICE).text
        assert '€' in first_element_currency
        main_page.click_element(MainPage.CURRENCY_CHECKBOX)
        main_page.click_element(MainPage.USD_CURRENCY)
        first_element_currency = main_page.find_element_by_locator(MainPage.FIRST_ELEMENT_PRICE).text
        assert '$' in first_element_currency
