import csv
import eel
import pandas as pd
import os

#creamos la ruta absoluta del archivo csv
absoultepath=os.path.dirname(__file__)
relativepath='./files/myfile.csv'
fullpath=os.path.join(absoultepath,relativepath)
#leemos 
df_new=pd.read_csv(fullpath,delimiter=';', header=0)

#Funcion que recibe un rango de filas y las muestra a través de una matriz. La función usa el archivo .csv con las columnas a utilizar
@eel.expose
def gettable(start: int, end: int):
    data=[]
    #Lectura del archivo
    with open(fullpath,newline='',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        for i, row in enumerate(reader):
            if(i == 0): data.append(row)
            if i>=start and i<=end:
               data.append(row)
    return data

 #Se recibe un indicador correspondiente a la columna orden del archivo .csv y se elimina la fila correspondiente a él
@eel.expose
def deleterecord(orden:int):
    try:
     #Lectura del archivo
     with open(fullpath,newline='',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        filas=[filas for filas in reader]
        #Recorrido de las filas hasta hallar el indicador
        for i, fila in enumerate(filas):
            if fila[0]==str(orden):
                del filas[i]
                break
    
    #Escritura del nuevo archivo sin el registro que se deseaba eliminar
     with open(fullpath,'w',newline='',encoding='utf-8') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(filas)
        return True
    except:
        return False

#Función para añadir un nuevo registro a la tabla csv
@eel.expose   
def addrecord(newrecord:list):
 
 try:
    #leemos el csv
    df_order=pd.read_csv(fullpath,delimiter=',', header=0)
    #Extraemos el último orden del csv y le sumamos uno
    #para así tener el índice del nuevo registro
    order=df_order['ORDEN'].to_list()
    last=int(order[-1])+1
    newrecord[0]=last

    #Abrimos el archivo csv y escribimos una nueva linea con el nuevo registro
    csvfile=open(fullpath,'a',newline='\n',encoding='utf-8')
    writer=csv.writer(csvfile,delimiter=',')
    writer.writerow(newrecord)
    csvfile.close()
    
    #retornamos true en caso de éxito
    return True
 except:
    #retornamos false en caso de error
    return False

#Función para mostrar un registro especifico dado un indicador de la columna orden
@eel.expose 
def printRecord(orden:int):
    #Lectura del archivo
    with open(fullpath,newline='',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        #Recorrido de las filas hasta hallar el indicador 
        for fila in reader:
            if fila[0]==str(orden):
                #Retornamos un diccionario que nos indique que se encontró la fila y la muestre
                return {'error': False, 'record': fila}
        #En caso de no encontrarse el indicador igualmente se retorna un diccionario pero indicando que no existe tal registro en el archivo    
        return { 'error': True, 'msg': 'not found' }