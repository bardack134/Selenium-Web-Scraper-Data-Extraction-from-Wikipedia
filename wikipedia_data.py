# import webdriver

from pprint import pprint
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import KEYS
from selenium.webdriver.common.keys import Keys


# Mantener el navegador abierto después de que el script ha sido ejecutado
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)


# Crear objeto webdriver para Chrome con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)

# Diccionario donde se guardarán los elementos encontrados
events_dictionary = {}


try:

    # Obtener página web
    driver.get("https://en.wikipedia.org/wiki/Main_Page")

    sleep(5)  # Esperar x segundos para que la página cargue completamente

    
        
    # Encontrar el anumero de articulos usando XPath
    # number = driver.find_element(By.XPATH, value=f'//*[@id="articlecount"]/a[1]')
    number = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
        
       
    #hacemos click en el elemento encontradu
    # number.click()
    
    
    #encontrar link lement usando find_element_by_link
    content_portals=driver.find_element(By.LINK_TEXT, 'Content portals')
        
        
    # content_portals.click()
    
     
    #encontrando el elemento input 'search'
    search_input=driver.find_element(By.NAME, value='search') 
    search_input.send_keys("Sapporo", Keys.ENTER) 
    
        
except Exception as err:
    print(f"El elemento no fue encontrado: {err}")  # Imprimir un mensaje de error si ocurre una excepción


else:
    # Imprimir el diccionario de eventos
    print(number.text)
    
      
finally:
    # Cerrar el navegador
    # driver.quit()
    pass