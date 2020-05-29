from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import settings
from base.locators import ComponentLocator, GroupLocator, Locator
from components.navbars import RegistriesNavbar
from pages.base import GuidBasePage, OSFBasePage


class BaseRegistriesPage(OSFBasePage):

    # Components
    navbar = ComponentLocator(RegistriesNavbar)


class RegistriesLandingPage(BaseRegistriesPage):
    url = settings.OSF_HOME + "/registries"

    identity = Locator(
        By.CSS_SELECTOR, "._RegistriesHeader_3zbd8x", settings.LONG_TIMEOUT
    )
    search_button = Locator(By.CSS_SELECTOR, "[data-test-search-button]")


class RegistriesDiscoverPage(BaseRegistriesPage):
    url = settings.OSF_HOME + "/registries/discover"

    identity = Locator(By.CSS_SELECTOR, "[data-test-share-logo]")
    loading_indicator = Locator(By.CSS_SELECTOR, ".ball-scale")

    # Group Locators
    search_results = GroupLocator(
        By.CSS_SELECTOR, "._RegistriesSearchResult__Title_1wvii8"
    )

    def get_first_non_withdrawn_registration(self):
        for result in self.search_results:
            try:
                result.find_element_by_class_name("label-default")
            except NoSuchElementException:
                return result.find_element_by_css_selector(
                    "[data-test-result-title-id]"
                )


class RegistrationDetailPage(GuidBasePage):
    identity = Locator(By.CSS_SELECTOR, "[data-test-registration-title]")
