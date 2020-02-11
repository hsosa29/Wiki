# -*- coding: utf-8 -*-
import json           
        
data= json.loads(open('jsonCrawler.json').read().encode("utf-8").decode("utf-8","ignore"))
dkeys = data.keys()
dkeys = list(dkeys)
from random import choice
puntero = choice(dkeys)
maximoPuntaje=0
contIteraciones=0
while maximoPuntaje < 400:
        
        if data.__contains__(puntero):
           
            datos = data[puntero]           
            datos['ranking']=str(int(datos['ranking']) + 1)
           
            if int(datos['ranking'])>maximoPuntaje:
                maximoPuntaje=int(datos['ranking'])                
            if len(datos['enlaces'])>0:
                url=choice(datos['enlaces'])                
            else:
                url = choice(dkeys)
            if data.__contains__(url):                
                   puntero=url
                
            else:
                contadorSecundario=0;
                while data.__contains__(url)==False and contadorSecundario<len(datos['enlaces']):
                    if len(datos['enlaces'])>0:
                        url=choice(datos['enlaces'])
                        contadorSecundario=contadorSecundario+1
                    else:
                        url = choice(dkeys)
                           
                if contadorSecundario < len(datos['enlaces']):                    
                       puntero=url                    
                else:
                    url = choice(dkeys)
                    puntero=url
                    
with open('jsonPageRank.json', 'w') as outfile:
    json.dump(data, outfile)



