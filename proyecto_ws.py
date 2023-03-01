import helium as he
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver = ChromeDriverManager().install()

driver = webdriver.Chrome(chrome_driver)


he.set_driver(driver)

###
### busqueda de google de coder house precio y temario, utilice css selector
###

he.go_to("https://www.google.com")

search_box = he.find_all(he.S("[aria-label='Buscar']"))[0]

#buscanmos el nombre del curso por google
he.write("Curso de Python CoderHouse", into=search_box)

search_button = he.find_all(he.S("[aria-label='Buscar con Google']"))[0]

he.press(he.ESCAPE)

he.click(search_button)

#localizamos el link de la pagina de coder house
content = driver.find_element(By.CSS_SELECTOR, 'h3.LC20lb')

he.click(content)

search_results = he.find_all(he.S("p"))

#creamos la variable para guardar el precio
price1 = ''
#buscamos el precio en el texto
search_price1 = he.find_all(he.S('.line-through'))

#lo guardamos en la variable
for search_result in search_price1:
    if "$" not in search_result.web_element.text.lower():
        continue
    price1 = search_result.web_element.text
    break

#buscamos el temario de la pagina
search_temario1 = he.find_all(he.S('.items-start'))

#eliminamos los temas que no son de python o del temario
temario1 = search_temario1[2:]

#convertimos el objeto en texto
for i in range(len(temario1)):
    temario1[i] = temario1[i].web_element.text

#creamos un archivo nuevo para guardar los datos del curso y lo cerramos
with open('cursos.txt', 'w') as f:
    f.write("Curso 1: Python CoderHouse\n")
    f.write('Precio: ' + price1 + '\n')
    f.write('Temario: ' + '')
    for i in range(len(temario1)):
        f.write(temario1[i] + '\n')
##########################################################
##########################################################

#buscamos el segundo curso por google
he.go_to("https://www.google.com")

search_box = he.find_all(he.S("[aria-label='Buscar']"))[0]

he.write("Curso de Python itmaster", into=search_box)

search_button = he.find_all(he.S("[aria-label='Buscar con Google']"))[0]

he.press(he.ESCAPE)

he.click(search_button)

#buscamos el link de la pagina
content = driver.find_element(By.CSS_SELECTOR, 'h3.LC20lb')

he.click(content)

#buscamos el boton de ver precios con XPATH y lo clickeamos
price2_button = driver.find_element(By.XPATH, "//*/div/ul/li/article/section[2]/a[1]")

he.click(price2_button)

#buscamos las cuotas por id lo convertimos a texto y le quitamos los caracteres que no queremos

cuotas = he.S('#precio-curso-cuota-valor')
precio_cuota = cuotas.web_element.text
precio_cuota = precio_cuota.split('$')[-1] 
precio_cuota = float(precio_cuota)

#buscamos cuantas cuotas hay por id y lo convertimos a texto

cant_cuotas =  he.S('#precio-curso-cuotas')
cant_cuotas = cant_cuotas.web_element.text
cant_cuotas = float(cant_cuotas)

#calculamos el precio total
price2 = precio_cuota * cant_cuotas

#lo convertimos a texto
price2 = str(price2)

he.press(he.ESCAPE)

#buscamos el temario por id y lo convertimos a texto
search_temario2 = he.S('#nav-plan')
temario2 = search_temario2.web_element.text

#volvemos a abrir el archivo y agregamos los datos del segundo curso
with open('cursos.txt', 'a') as f:
    f.write('\n'*3)
    f.write("Curso 2: Python ITMaster\n")
    f.write('Precio: ' + price2 + '\n')
    f.write('Temario: ' + temario2 + '\n')

    

driver.quit()