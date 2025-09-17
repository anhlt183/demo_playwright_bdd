import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.your_information_page import InformationPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage
from pytest_bdd import hooks

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

# Biến global để quản lý vòng đời browser/context cho từng Scenario
# _browser = None
# _context = None
# _playwright = None
# _last_outline_name = None  # Lưu tên Outline đang chạy

# def pytest_bdd_before_scenario(request, feature, scenario):
#     """Chạy trước mỗi Scenario (bao gồm cả Outline)."""
#     global _browser, _context, _playwright, _last_outline_name
#     # Lấy tên outline gốc (không có param row)
#     outline_name = str(scenario).split("[")[0].strip()
#     # Nếu chưa có browser hoặc outline_name thay đổi → mở browser mới
#     if _browser is None or outline_name != _last_outline_name:
#         print(f"[HOOK] Starting browser for Scenario: {scenario}")
#         if _browser:  # Nếu đang có browser cũ thì đóng
#             _context.close()
#             _browser.close()
#             _playwright.stop()
#         _playwright = sync_playwright().start()
#         _browser = _playwright.chromium.launch(headless=False)
#         _context = _browser.new_context()
#         _last_outline_name = outline_name

#     # Gắn context vào request.node để fixture page lấy dùng
#     request.node.context = _context


# def pytest_bdd_after_scenario(request, feature, scenario):
#     """Đóng browser/context khi Scenario kết thúc."""
#     global _browser, _context, _playwright, _last_outline_name
#     # Lấy tên outline gốc
#     outline_name = scenario.name.split("[")[0].strip()
#     # Nếu đây là row cuối cùng của outline → đóng browser
#     scenario_list = list(feature.scenarios.values())  # list ScenarioTemplate/Scenario object
#     current_index = scenario_list.index(scenario)
#     is_last_row = not any(
#         s.name.startswith(outline_name) and s.name != scenario.name
#         for s in scenario_list[current_index + 1 :]
#     )

#     if is_last_row and _browser:
#         print(f"[HOOK] Closing browser for Outline: {outline_name}")
#         _context.close()
#         _browser.close()
#         _playwright.stop()
#         _context = None
#         _browser = None
#         _playwright = None
#         _last_outline_name = None


# @pytest.fixture
# def page(request):
#     """Trả về page mới trong context hiện tại."""
#     context = getattr(request.node, "context", None)
#     if not context:
#         raise RuntimeError("No browser context for current scenario")
#     page = context.new_page()
#     yield page
#     # page.close()


@pytest.fixture
def login_page(page):
    return LoginPage(page)
@pytest.fixture
def home_page(page):
    return HomePage(page)
@pytest.fixture
def product_detail_page(page):
    return ProductDetailPage(page)
@pytest.fixture
def cart_page(page):
    return CartPage(page)
@pytest.fixture
def your_information_page(page):
    return InformationPage(page)
@pytest.fixture
def overview_page(page):
    return OverviewPage(page)
@pytest.fixture
def complete_page(page):
    return CompletePage(page)
