from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.select import Select  
from time import sleep  
import openpyxl


driver = webdriver.Chrome()
driver.get('https://www.themoviedb.org/')
sleep(15)

movie = driver.find_elements(By.XPATH, "//div[@class='card style_1']")

for movies in movie:
    movies.click()
    sleep(5)

    janelas = driver.window_handles
    driver.set_window_size(1920,1080)


    name_movie = driver.find_elements(By.XPATH,"//div[@class='title ott_false']//a")
    name_movie = name_movie[0]
    name_movie = name_movie.text    

    type_Movie = driver.find_elements(By.XPATH, "//div[@class='title ott_false']//div//span[@class='genres']")
    type_Movie = type_Movie[0]
    type_Movie = type_Movie.text

    runtime_Movie = driver.find_elements(By.XPATH, "//div[@class='title ott_false']//div//span[@class='runtime']")
    runtime_Movie = runtime_Movie[0]
    runtime_Movie = runtime_Movie.text 

    sinopse = driver.find_elements(By.XPATH, "//div[@class='header_info']//div")
    sinopse = sinopse[0]
    sinopse = sinopse.text

    workbook = openpyxl.load_workbook('TheMoviesDB_Python.xlsx')

    try:
       pagina_excel = workbook[name_movie]

       pagina_excel['A1'].value = "Filme"
       pagina_excel['B1'].value = "Gêneros"
       pagina_excel['C1'].value = "Duração"
       pagina_excel['D1'].value = "Sinopse"

       pagina_excel['A2'].value = name_movie
       pagina_excel['B2'].value = type_Movie
       pagina_excel['C2'].value = runtime_Movie
       pagina_excel['D2'].value = sinopse

       workbook.save('TheMoviesDB_Python.xlsx')
       driver.back()
       driver.refresh()
        
    except Exception as error:

       workbook.create_sheet(name_movie)
       pagina_excel = workbook[name_movie]

       pagina_excel['A1'].value = "Filme"
       pagina_excel['B1'].value = "Gêneros"
       pagina_excel['C1'].value = "Duração"
       pagina_excel['D1'].value = "Sinopse"

       pagina_excel['A2'].value = name_movie
       pagina_excel['B2'].value = type_Movie
       pagina_excel['C2'].value = runtime_Movie
       pagina_excel['D2'].value = sinopse

       workbook.save('TheMoviesDB_Python.xlsx')
       driver.back()    
       driver.refresh()       
   
    sleep(15)

driver.close()