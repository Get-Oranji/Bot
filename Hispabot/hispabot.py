import os
import tkinter
from tkfilebrowser import askopenfilename
from selenium import webdriver

browser = webdriver.Chrome(executable_path='/chromedriver') 

browser.maximize_window()
tablon = input("Inserta el tablon donde quieres hacer el post. Ex: /mu/: ")
browser.get('http://www.hispachan.org' + tablon) 
#Entra en la pagina de Hispachan junto al tablon donde quieres hacer tu post

titulo = browser.find_element_by_name('subject')
#Busca el elemento titulo del post y almacena la forma de acceder a el en titulo

post = browser.find_element_by_name('message') 
#Busca el elemento post del post y almacena la forma de acceder a el en post
tkinter.Tk().withdraw()
imagenI = askopenfilename()
while true:
 if imagenI:
  imagen = browser.find_element_by_name("imagefile").send_keys(imagenI)
  break
 else:
  print("Por favor, inserte bien el archivo")
#Busca el elemento seleccionar archivo del post y abre un dialogo Tkinter para seleccionar el archivo que quieras#

input_ = input("Inserta el titulo del post: ")
titulo.send_keys(input_)
#Le envia el titulo que insertes

input_ = input("Inserta el post: ")
post.send_keys(input_)
#Le envia el post que insertes

click = browser.find_element_by_class_name("enviar").click()
#Busca el boton de enviar y le hace click... Si, no tiene misterio
print("Tu post ha sido enviado")
 
print("Objeto Navegador -> ", browser)


