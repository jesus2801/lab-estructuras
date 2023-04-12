import statistics
import eel
import pandas as pd
import screen1

#Función que devuelve varios valores estadísticos del csv
@eel.expose
def statisticData():
    #Leemos el csv y creamos una lista de cada columna del csv
    df_new = pd.read_csv(screen1.fullpath,delimiter=',', header=0)
    Peaton= df_new['PEATON'].to_list()
    Automovil=df_new['AUTOMOVIL'].to_list()
    Campaero=df_new['CAMPAERO'].to_list()
    Camioneta=df_new['CAMIONETA'].to_list()
    Micro=df_new['MICRO'].to_list()
    Buseta=df_new['BUSETA'].to_list()
    Bus=df_new['BUS'].to_list()
    Camion=df_new['CAMION'].to_list()
    Volqueta=df_new['VOLQUETA'].to_list()
    Moto=df_new['MOTO'].to_list()
    Bicicleta=df_new['BICICLETA'].to_list()
    Diurnio_Nocturno=df_new['DIURNIO/NOCTURNO'].to_list()
    Gravedad=df_new['GRAVEDAD'].to_list()

    #Datos a devolver
    datos={}

    #Vamos recorriendo cada columna y vamos agregando sus valores estadísticos al diccionario
    lists=[('Peaton', Peaton), ('Automovil', Automovil), ('Campaero', Campaero), ('Camioneta', Camioneta), ('Micro', Micro), ('Buseta', Buseta), ('Bus', Bus), ('Camion', Camion), ('Volqueta', Volqueta), ('Moto', Moto), ('Bicicleta', Bicicleta)]
    for i, lista in lists:
        moda=statistics.mode(lista)
        mediana=statistics.median(lista)
        media=statistics.mean(lista)
        maximum=max(lista)
        minimum=min(lista)
        datos[f'{i}']={'Moda':moda,'Mediana':mediana,'Media':media, 'máximo':maximum, 'mínimo':minimum}
    
    #Agregamos los valores estadísticos de las dos excepciones que son diruno/nocturno y gravedad, los cuales
    #manejan valores cualitativos, no cuantitativos
    modadiurniou_nocturno=statistics.mode(Diurnio_Nocturno)
    modagravedad=statistics.mode(Gravedad)
    datos[f"{'Diurnio/Nocturno'}"]={'Moda':modadiurniou_nocturno, 'Mediana': 'N/A', 'Media':'N/A','máximo':'N/A','mínimo': 'N/A'}
    datos[f"{'Gravedad'}"]={'Moda':modagravedad, 'Mediana': 'N/A', 'Media':'N/A','máximo':'N/A','mínimo': 'N/A'}

    #retornamos los datos
    return datos