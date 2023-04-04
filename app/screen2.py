#datos estadísticos, los que ustedes quieran....
#en general son bastante fáciles de hacer, solo es seguir ciertas fórmulas

#mediana, media, desviación estandar, etc...
#hagan varias funciones sobre eso.

#-------------------------------------------
#las gráficas si me toca a mi del lado del cliente porque ahí es donde se grafica xd

#datos estadísticos, los que ustedes quieran....
#en general son bastante fáciles de hacer, solo es seguir ciertas fórmulas

#mediana, media, desviación estandar, etc...
#hagan varias funciones sobre eso.

#-------------------------------------------
#las gráficas si me toca a mi del lado del cliente porque ahí es donde se grafica xd

#Moda, media, mediana y valores máximos y mínimos de las listas usadas
import statistics
import eel
import screen1 

@eel.expose
def statisticdata():
    datos={}
    lists=[('Peaton', screen1.Peaton), ('Automovil', screen1.Automovil), ('Campaero', screen1.Campaero), ('Camioneta', screen1.Camioneta), ('Micro', screen1.Micro), ('Buseta', screen1.Buseta), ('Bus', screen1.Bus), ('Camion', screen1.Camion), ('Volqueta', screen1.Volqueta), ('Moto', screen1.Moto), ('Bicicleta', screen1.Bicicleta)]
    for i, lista in lists:
        moda=statistics.mode(lista)
        mediana=statistics.median(lista)
        media=statistics.mean(lista)
        maximum=max(lista)
        minimum=min(lista)
        datos[f'Lista {i}']={'Moda':moda,'Mediana':mediana,'Media':media, 'Valor máximo':maximum, 'Valor mínimo':minimum}
    
    modadiurniou_nocturno=statistics.mode(screen1.Diurnio_Nocturno)
    modagravedad=statistics.mode(screen1.Gravedad)
    datos[f"Lista {'Diurnio/Nocturno'}"]={'Moda':modadiurniou_nocturno, 'Mediana': 'N/A', 'Media':'N/A','Valor máximo':'N/A','Valor mínimo': 'N/A'}
    datos[f"Lista {'Gravedad'}"]={'Moda':modagravedad, 'Mediana': 'N/A', 'Media':'N/A','Valor máximo':'N/A','Valor mínimo': 'N/A'}
    return datos





#datosestadisticos=statisticdata()
#print(datosestadisticos)

#Solo se calcula la moda de las listas de Diurnio/Nocturno y gravedad porque son listas que no contienen
