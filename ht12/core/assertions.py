from ht12.core.actions import Actions


class Assertions(Actions):

    def __init__(self, driver):
        super().__init__(driver)

    def assert_element_is_visible(self, selector):
        element = self.get_element(selector)
        assert element.is_displayed(), f"Element {selector} is not visible"

    def assert_element_is_selected(self, selector):
        element = self.get_element(selector)
        assert element.is_selected(), f"Element {selector} is not selected"
