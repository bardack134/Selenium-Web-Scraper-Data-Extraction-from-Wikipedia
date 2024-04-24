# import webdriver

from pprint import pprint
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



# Mantener el navegador abierto después de que el script ha sido ejecutado
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# Crear objeto webdriver para Chrome con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)

# Diccionario donde se guardarán los elementos encontrados
events_dictionary = {}


try:

    # Obtener página web
    driver.get("https://en.wikipedia.org/wiki/Main_Page")

    sleep(10)  # Esperar 10 segundos para que la página cargue completamente
    
    # Iterar sobre los primeros 5 elementos de la lista de eventos
    
        
        # Encontrar el año del evento utilizando XPath
    number = driver.find_element(By.XPATH, value=f'//*[@id="articlecount"]/a[1]')
        
       
        
        
except Exception as err:
    print(f"El elemento no fue encontrado: {err}")  # Imprimir un mensaje de error si ocurre una excepción

else:
    # Imprimir el diccionario de eventos
    print(number.text)
    
finally:
    # Cerrar el navegador
    driver.quit()
