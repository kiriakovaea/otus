from selenium.webdriver.common.by import By


class CatalogPage:
    LOGO = (By.CLASS_NAME, "img-thumbnail")
    LIST_VIEW_BUTTON = (By.ID, "list-view")
    GRID_VIEW_BUTTON = (By.ID, "grid-view")
    SORTED_BY_BUTTON = (By.ID, 'input-sort')
    SHOW_LIMIT_BUTTON = (By.ID, 'input-limit')
    FIRST_IMAGE = (By.LINK_TEXT, 'Apple Cinema 30"')
