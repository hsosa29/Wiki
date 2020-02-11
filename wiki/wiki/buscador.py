import json

data=json.loads(open('jsonIndexer.json').read().encode("utf-8").decode("utf-8","ignore"))

def obtenerRelevancia(lista, palabras):
        rel=0
        for palabra in palabras:
                if lista.has_key(palabra):
                        rel=rel+int(lista[palabra])
               
        return rel

print ("se ha cargado el archivo con el listado de paginas por palabra")
print ("se ha cargado el archivo con los datos PageRank")

entrada=raw_input("Ingrese la palabra que quiere buscar: ")
palabras=entrada.split()
print ("Resultado de Busqueda")


cont=0
       

for x in list(data.keys()):
         relevancia=obtenerRelevancia(data[x]['palabras'],palabras)
         if(relevancia>0):
                        cont=cont+1
                        print ("Titulo de pagina: %s" % data[x]['titulo'])
                                
                        print ("URL:%s \n" % x)
                        
                        fichero_contenido='pags_texto/'+data[x]['ruta'].split('pags_html/')[1].split('.html')[0]+'.txt'
                        archivo_texto_pl=open(fichero_contenido,'r')
                        texto=archivo_texto_pl.read()
                        contenido="..."
                        for word in palabras:
                                posicion= texto.find(word)
                                contenido=contenido+'...'+(texto[posicion:(posicion+200)])
                                contenido=" ".join( contenido.split() )
                        print ("Contenido:" +contenido+'\n')
                        print ("Relevancia de la busqueda "+str(relevancia)+'\n')
                        print ("Rankin de pagina: %s \n" % data[x]['ranking'])
                        print ("Resultado: %s \n" %  cont)
                        print ('------------------------------------------------------------------------------------------------------------')
                        


if cont==0:
        print ('No hay resultados para su busqueda')
