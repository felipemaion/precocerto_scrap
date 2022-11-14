import credential
from ui import *

import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
val = "https://sys.precocerto.co/pedidos-de-venda"
wait = WebDriverWait(driver, 2400)
driver.get(val)

def wait_and_click(type,element):
    wait.until(EC.presence_of_element_located((type,element)))
    # wait.until(EC.element_to_be_clickable((type,element)))
    item = driver.find_element(type,element)
    item.click()
    return item


logging.info("Login into system...")
username_login = driver.find_element(*USER_INPUT)
username_login.send_keys(credential.login["username"])

password_login = driver.find_element(*PASSWORD_INPUT)
password_login.send_keys(credential.login["password"])
driver.find_element(*LOGIN_BUTTON).click()

logging.info("Waiting main page to load...")
wait.until(EC.presence_of_element_located(TABLE_PRODUCTS))
                                               

logging.info("Entering 'Pedidos de vendas' page.")
wait_and_click(*MANAGE_BUTTON)
wait_and_click(*PAGE_BUTTON)

logging.info("Page loading...")
wait.until(EC.presence_of_element_located(ORDERS_TABLE))
logging.info("Page loaded.")

logging.info("Checking Synchronization...")


while (driver.find_element(*LAST_SYNC).text == "Carregando..."): 
    # logging.info(".", end="")
    sleep(1)
    if (driver.find_element(*SYNC_BUTTON).text == "SINCRONIZAR") and (driver.find_element(*SYNC_BUTTON).is_enabled()):
        logging.info("Initializing Sync.")
        wait_and_click(*SYNC_BUTTON)
        logging.info("Clicked Sync")
        while (driver.find_element(*SYNC_BUTTON).text == "SINCRONIZAR"):
            pass
            sleep(2)
    if (driver.find_element(*SYNC_BUTTON).text == "SINCRONIZANDO..."):
        logging.info("Waiting sync to finish...")
        while (driver.find_element(*SYNC_BUTTON).text != "SINCRONIZAR"):
            debug = driver.find_element(*SYNC_BUTTON).text
            # logging.info(".", end="")
            sleep(1)

logging.info("Sync finished.")

logging.info("Selecting all items.")
wait_and_click(*SELECT_ALL)
logging.info("All items from all pages...")
wait_and_click(*ALL_ITEMS)
logging.info("Dropping menu.")
wait_and_click(*DROPPING_MENU)
logging.info("Exporting to Excel...")
wait_and_click(*EXPORTING_EXCEL)

wait.until(EC.visibility_of_element_located(EXPORTING_SCREEN))
logging.info("Waiting to finish download.")
wait.until(EC.invisibility_of_element_located(EXPORTING_SCREEN))
logging.info("Exiting in 5 sec.")
sleep(5)
driver.quit()
logging.info("Bye.")