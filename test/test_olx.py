from page.home_olx import TestOLXSearch

def test_correct_page(driver):
    home_page = TestOLXSearch(driver)
    home_page.test_olx_search()
