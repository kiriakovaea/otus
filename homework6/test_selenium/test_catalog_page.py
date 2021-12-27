from homework6.pages.CatalogPage import CatalogPage


class TestCatalogPage:
    def test_catalog_page(self, browser):
        catalog_page = CatalogPage(browser)
        catalog_page.find_element_by_locator(CatalogPage.LOGO)
        catalog_page.find_element_by_locator(CatalogPage.SHOW_LIMIT_BUTTON)
        catalog_page.find_element_by_locator(CatalogPage.SORTED_BY_BUTTON)
        list_view = catalog_page.find_element_by_locator(CatalogPage.LIST_VIEW_BUTTON)
        catalog_page._simple_click_element(list_view)
        first_list_image = catalog_page.waiting_element_visible(CatalogPage.FIRST_IMAGE)
        catalog_page.check_first_element(first_list_image)
        table_view = catalog_page.find_element_by_locator(CatalogPage.GRID_VIEW_BUTTON)
        catalog_page._simple_click_element(table_view)
        first_table_image = catalog_page.waiting_element_visible(CatalogPage.FIRST_IMAGE)
        catalog_page.check_first_element(first_table_image)
