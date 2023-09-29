from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By

driver = Firefox()

driver.get('https://www.pensador.com/bom_dia_mensagens_e_frases/')

elems = driver.find_elements(By.CSS_SELECTOR, 'blockquote p')

for e in elems:
    print(e.text)

driver.close()