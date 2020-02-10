import json


#with open('indice.json') as data_file:
#    data = json.load(data_file)
data=json.loads(open('indexerOut.json').read().encode("utf-8").decode("utf-8","ignore"))
#pprint(data)

def obtenerRelevancia(lista, palabras):
        rel=0
        for palabra in palabras:
                if lista.has_key(palabra):
                        rel=rel+int(lista[palabra])
               
        return rel

print "se ha cargado el archivo con el listado de pagnas por palabra"
print "se ha cargado el archivo con los datos pagerank"

entrada=raw_input("Ingrese la palabra que quiere buscar: ")
palabras=entrada.split()
print "Resultado de Busqueda"


cont=0
       

for x in list(data.keys()):
         relevancia=obtenerRelevancia(data[x]['palabras'],palabras)
         if(relevancia>0):
                        cont=cont+1
                        print "Titulo de pagina: %s" % data[x]['titulo']
                                
                        print "URL:%s \n" % x
                        #print "Ruta pagina: %s" % data[x]['ruta']
                        fichero_contenido='pags_texto/'+data[x]['ruta'].split('pags_html/')[1].split('.html')[0]+'.txt'
                        archivo_texto_pl=open(fichero_contenido,'r')
                        texto=archivo_texto_pl.read()
                        contenido="..."
                        for word in palabras:
                                posicion= texto.find(word)
                                contenido=contenido+'...'+(texto[posicion:(posicion+200)])
                                contenido=" ".join( contenido.split() )
                        print "Contenido:" +contenido+'\n'
                        print "Relevancia de la busqueda "+str(relevancia)+'\n'
                        print "Rankin de pagina: %s \n" % data[x]['ranking']
                        print "Resultado: %s \n" %  cont
                        print '------------------------------------------------------------------------------------------------------------'
                        


if cont==0:
        print 'No se encontraron coincidencias para su busqueda'
