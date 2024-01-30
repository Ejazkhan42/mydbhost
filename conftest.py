from Helper.packages.requirments import setup_driver as driver
import pytest

@pytest.fixture()
def test_driver(request):
    driver_instance = driver(0)
    driver_instance.maximize_window()
    def fin():
        # Save screenshot on test failure
        if hasattr(request.node, 'rep_call') and request.node.rep_call is not None and request.node.rep_call.failed:
            screenshot_path = f"screenshot_{request.node.name}.png"
            driver_instance.save_screenshot(screenshot_path)

    request.addfinalizer(fin)

    yield driver_instance
    driver_instance.quit()
