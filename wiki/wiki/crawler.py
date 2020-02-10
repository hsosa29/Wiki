# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
import os
import string

def obtenerCuentaPalabras(ruta_actual,nombre_arc_act):
    soup=BeautifulSoup(open(ruta_actual),"html.parser")
    for script in soup(["script","style"]):
      script.extract()
    texto_completo = soup.get_text()
    try:
        titulo=soup.find('title').get_text()        
        print 'extrayendo titilo '+titulo
    except:
        titulo='Sin titulo'
    pageRankArchivo[url_act]['titulo']=titulo

    #Se revisa si existe la carpeta para escribir los archivos y sino se crea la carpeta
    carpeta='pags_texto'
    if not os.path.exists(carpeta):
      os.makedirs(carpeta)
    # Se escribe el archivo con el texto plano
    archivo_texto_pl=open(carpeta+'/'+nombre_arc_act+'.txt','w')
    print texto_completo
    textoSinCarEsp = texto_completo.translate ({ord(c): None for c in "↑!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    print textoSinCarEsp
    #textoSinCarEsp = texto_completo.translate(table)
     
    archivo_texto_pl.write(textoSinCarEsp.encode('utf-8'))
    archivo_texto_pl.close()
    #Ahora extraemos la lista de palabras de cada archivo y armamos un diccionario python con las frecuencias. 
    listaPalabras = textoSinCarEsp.split()
    frecPalabras={}
    for palabra in listaPalabras:
      frecPalabras[palabra]=listaPalabras.count(palabra)

    return frecPalabras



archivo_pags=open('pageRankOut.json','r').read()
pageRankArchivo=json.loads(archivo_pags)
lista_pags=list(pageRankArchivo.keys())
print len(lista_pags)
pags_index=0
# Ciclo para leer todos las páginas
for url_act in lista_pags:
  ruta_temp = pageRankArchivo[url_act]['ruta']
  print ruta_temp
  nombre_archivo = ruta_temp.split('pags_html/')[1]
  ruta_temp = 'pags_html/'+nombre_archivo
  calif_pags=obtenerCuentaPalabras(ruta_temp,nombre_archivo.split('.html')[0])
  pageRankArchivo[url_act]['palabras']=calif_pags
  pags_index+=1
  print('Páginas indexadas: '+str(pags_index))
  archivo_pagerankfinal=open('indexerOut.json','w')
  archivo_pagerankfinal.write(json.dumps(pageRankArchivo,indent=4))
  archivo_pagerankfinal.close()
