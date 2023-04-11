import eel
import pandas as pd
import numpy as np
import screen1
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, roc_auc_score
import statsmodels.api as sm


#Función que suma los actores viales y los guarda en una lista
def cambiar_datos_Gravedad():
    #Leemos el csv y creamos una lista de las columnas del csv a la que le convertiremos los valores
    df_new = pd.read_csv(screen1.fullpath,delimiter=',', header=0)
    Gravedad = df_new['GRAVEDAD'].to_list()
    
    Gravedad_new = []

    # Reemplazamos los valores de la columna "gravedad" en la lista creada
    for elemento in Gravedad:
        if elemento == "Con Heridos":
            Gravedad_new.append(0)
        elif elemento == "Solo Daños":
            Gravedad_new.append(1)
        else:
            Gravedad_new.append(2)

    return Gravedad_new

def cambiar_datos_dn():
    #Leemos el csv y creamos una lista de las columnas del csv a la que le convertiremos los valores
    df_new = pd.read_csv(screen1.fullpath,delimiter=',', header=0)
    Diurnio_Nocturno = df_new['DIURNIO/NOCTURNO'].to_list()
    
    DN_new = []
    
    # Reemplazamos los valores de la columna "diurno/nocturno" en la lista creada
    for element in Diurnio_Nocturno:
        if element == "Diurno":
            DN_new.append(0)
        else:
            DN_new.append(1)

    return DN_new

#Funcion que suma los actores viales y los guarda en una lista
def actoresViales():
    #Leemos el csv y guardamos las columnas que necesitamos (actores viales)
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

    #En la lista actoresViales guardamos el resultado la funcion sum aplicada a cada tupla generada con los datos de las listas
    actoresViales = list(map(sum, zip(Peaton, Automovil, Campaero, Camioneta, Micro, Buseta, Bus, Camion, Volqueta, Moto, Bicicleta)))

    return actoresViales

@eel.expose
def getPrediction(a_viales : int, dn : int):
    # Variables dependientes e independientes para el training test

    x1, x2 = actoresViales(), cambiar_datos_dn()
    x11 = x1[:int(len(x1) / 2)]
    x12 = x1[int(len(x1) / 2):]
    x21 = x2[:int(len(x2) / 2)]
    x22 = x2[int(len(x2) / 2):]

    x = np.column_stack((x11, x21))
    yn = cambiar_datos_Gravedad()
    y = yn[:int(len(yn) / 2)]


    #Datos a predecir
    datos_p = np.column_stack((a_viales, dn))
    datosmetricas = np.column_stack((x12, x22))

    # Dividir los datos en train(90%) y test(10%)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.9)


    # Instanciamos variable de regresión logistica
    r_logistica = LogisticRegression()

    # Se ajusta el modelo
    r_logistica.fit(x_train, y_train)

    # Se realizan las predicciones
    y_predict = r_logistica.predict(datos_p)
    y_predict2 = r_logistica.predict(datosmetricas)
    y_predict2 = y_predict2[:len(y_predict2) - 1909]

    # Se realizan las probabilades de cada caso
    pb = r_logistica.predict_proba(datos_p)

    # Presición del modelo
    p = r_logistica.score(x_test, y_test)

    # Intercepciones del modelo
    i = r_logistica.intercept_
    
    # Coeficientes del modelo
    c = r_logistica.coef_

    #Calculo de las métricas
    # 2. Error cuadratico medio
    errorMC =mean_squared_error(y_test, y_predict2)

    #2. P-value
    x_train_const = sm.add_constant(x_train)
    model = sm.Logit(y_train, x_train_const)
    results = model.fit()
    p_value = results.pvalues[1]
    print(len(), x_train_const)
    #3. AUC: area bajo la curva, mide el desempeño
    #auc = roc_auc_score(y_test, r_logistica.predict_proba(x_test)[:, 1])

    return {
        "Prediccion" : y_predict,
        "Probabilidades" : pb,
        "Precisión" : p,
        "Intercepciones" : i,
        "Coeficientes" : c,
        "Error cuadratico medio" : errorMC
        #"P-value" : p_value,
        #"AUC": auc
    }

ejemplo = getPrediction(4,0)
print(ejemplo)