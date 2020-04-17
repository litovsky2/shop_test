 
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base_url")
    fixture = Application(base_url)
    fixture.wd.maximize_window()
    fixture.wd.implicitly_wait(10)
    yield fixture
    fixture.destroy()


def pytest_addoption(parser):
    parser.addoption(
        "--base_url",
        action="store",
        default="http://automationpractice.com/",
        help="base_url",
    )