# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
import os
import string

def getPalabras(ruta_actual,nombre_arc_act):
    soup=BeautifulSoup(open(ruta_actual),"html.parser")
    for script in soup(["script","style"]):
      script.extract()
    texto_completo = soup.get_text()
    try:
        titulo=soup.find('title').get_text()        
        print ('extrayendo titulo '+titulo)
    except:
        titulo='Sin titulo'
    pageRankArchivo[url_act]['titulo']=titulo

    #Se crea la carpeta pags_texto
    carpeta='pags_texto'
    if not os.path.exists(carpeta):
      os.makedirs(carpeta)
   
    text_file=open(carpeta+'/'+nombre_arc_act+'.txt','w')
    print texto_completo
    textoSinCarEsp = texto_completo.translate ({ord(c): None for c in "↑!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    print textoSinCarEsp
        
    text_file.write(textoSinCarEsp.encode('utf-8'))
    text_file.close()
    #Armar diccionario a partir del archivo de texto plano.
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
# Lectura de todas las páginas
for url_act in lista_pags:
  ruta_temp = pageRankArchivo[url_act]['ruta']
  print ruta_temp
  nombre_archivo = ruta_temp.split('pags_html/')[1]
  ruta_temp = 'pags_html/'+nombre_archivo
  calif_pags=getPalabras(ruta_temp,nombre_archivo.split('.html')[0])
  pageRankArchivo[url_act]['palabras']=calif_pags
  pags_index+=1
  print('Páginas indexadas: '+str(pags_index))
  archivo_pagerankfinal=open('indexerOut.json','w')
  archivo_pagerankfinal.write(json.dumps(pageRankArchivo,indent=4))
  archivo_pagerankfinal.close()
