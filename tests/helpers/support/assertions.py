def assert_field_error(element):
    if not element.get_attribute('aria-invalid'):
        raise AssertionError("No attribute @aria-invalid")
