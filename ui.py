from selenium.webdriver.common.by import By

SYNC_BUTTON = By.XPATH,'//*[@id="synchronize-button"]'
LAST_SYNC = By.ID,'last-synchronization'
SELECT_ALL = By.NAME,'btSelectAll'
ALL_ITEMS = By.XPATH,'//*[@id="salesOrders"]/div[4]/div/div[1]/div[2]/div[1]/div/a[1]'
DROPPING_MENU = By.XPATH,'//*[@id="dropdownMenuButton"]'
EXPORTING_EXCEL = By.XPATH,'//*[@id="export-order-lines"]'
EXPORTING_SCREEN = (By.ID, 'swal2-title')
USER_INPUT = By.ID,"id_username_login"
PASSWORD_INPUT = By.ID,"id_password_login"
MANAGE_BUTTON = By.XPATH,'//*[@id="navbarSupportedContent"]/ul[1]/li[3]/a'
PAGE_BUTTON = By.XPATH,'//*[@id="navbarSupportedContent"]/ul[1]/li[3]/div/a[1]'
ORDERS_TABLE = (By.ID,'ordersTable')
TABLE_PRODUCTS = (By.ID,'tableProducts')
LOGIN_BUTTON = By.XPATH,'//*[@id="loginContainer"]/button'