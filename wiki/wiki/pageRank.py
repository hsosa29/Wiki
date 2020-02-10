# -*- coding: utf-8 -*-
import json           
    
    
data= json.loads(open('crawlOut.json').read().encode("utf-8").decode("utf-8","ignore"))
dkeys = data.keys()
dkeys = list(dkeys)
from random import choice
puntero = choice(dkeys)
maximoPuntaje=0
contIteraciones=0
while maximoPuntaje < 400:
        
        if data.has_key(puntero):
            print 'encontrado '+puntero
            datos = data[puntero]           
            datos['ranking']=str(int(datos['ranking']) + 1)
            print "puntuacion actual "+datos['ranking']
            print 'maximo puntaje es '+str(maximoPuntaje)
            if int(datos['ranking'])>maximoPuntaje:
                maximoPuntaje=int(datos['ranking'])                
            if len(datos['enlaces'])>0:
                url=choice(datos['enlaces'])                
            else:
                url = choice(dkeys)
            if data.has_key(url):                
                   puntero=url
                
            else:
                contadorSecundario=0;
                while data.has_key(url)==False and contadorSecundario<len(datos['enlaces']):
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
                    
with open('pageRankOut.json', 'w') as outfile:
    json.dump(data, outfile)



