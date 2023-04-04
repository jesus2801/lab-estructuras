#getTable(start: int, end: int): int[][] -> obtener matriz que representa la tabla principal
#deleteRecord(orden: int): void -> eliminar registro
#addRecord(aquí irán las columnas que decidan que van a conformar la tabla principal): void -> Agregar registro
#printrecord(orden)->specific row
#Recomiendo haber creado ya la tabla con las nuevas columnas, etc, etc, antes de comenzar a crear las funciones
import csv
import pandas as pd
import eel
import numpy as np
#Se crea la tabla principal con el archivo
df=pd.read_csv('app/datos.csv',delimiter=';', header=0)
#Variables independientes
Peaton= df['PEATON'].to_list()
Automovil=df['AUTOMOVIL'].to_list()
Campaero=df['CAMPAERO'].to_list()
Camioneta=df['CAMIONETA'].to_list()
Micro=df['MICRO'].to_list()
Buseta=df['BUSETA'].to_list()
Bus=df['BUS'].to_list()
Camion=df['CAMION'].to_list()
Volqueta=df['VOLQUETA'].to_list()
Moto=df['MOTO'].to_list()
Bicicleta=df['BICICLETA'].to_list()
Diurnio_Nocturno=df['DIURNIO/NOCTURNO'].to_list()
#Variables dependientes
Gravedad=df['GRAVEDAD'].to_list()
df_new=df[["ORDEN","PEATON","AUTOMOVIL","CAMPAERO","CAMIONETA","MICRO","BUSETA","BUS","CAMION","VOLQUETA","MOTO","BICICLETA","DIURNIO/NOCTURNO","GRAVEDAD"]]

@eel.expose
def gettable(start: int, end: int, data):
    new=data.loc[data['ORDEN'].between(start,end)]
    new.columns=['']*len(new.columns)
    matriz=new.values
    return matriz

#tabla=gettable(10,20, df_new)
#print(tabla)

@eel.expose
def deleteRecord(orden: int, data):
    new=data.loc[data['ORDEN']!=orden]
    new=new.reset_index(drop=True)
    new.columns=['']*len(new.columns)
    matriz=new.values
    return matriz

#delete=deleteRecord(2,df_new) 
#print(delete)  
@eel.expose
def addrecord(data, newrecord):
    nuevo=pd.DataFrame([newrecord],columns=data.columns)
    newdf=pd.concat([data,nuevo],ignore_index=True)
    newdf.columns=['']*len(newdf.columns)
    matriz=newdf.values
    return matriz

#new=addrecord(df_new,[df_new['ORDEN'].max()+1,1,1,1,1,1,1,1,1,1,1,1,'Diurno','Con muertos'])
#print(new)

@eel.expose
def printrecord(data, orden:int):
    selectedrow=data.iloc[orden-1]
    print(selectedrow)

#call=printrecord(df_new, 7)
