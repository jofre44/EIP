import pandas as pd
import numpy as np
import plotly.graph_objs as go

print("Actividad 1. Buenas Practicas Python")
print("Alumno: Jose Sepulveda \n")



def read_data():
    """
    Funcion para lectura del csv de finanzas 2020. El archivo, separado y path estan harcoded
    Output:
        data: dataframe con los datas del csv.
    """
    data = pd.DataFrame()
    data_ok = False
    read_ok = False
    ncol_ok = False
    while not data_ok:
        csv_name = 'finanzas2020'
        separador = '\t'
        csv_file = csv_name + '.csv'
        
        try:
            data = pd.read_csv(csv_file, sep=separador)
            read_ok = True
        except:
            print("Archivo no leido. Chequear que el archivo se encuentre en la direccion correcta o sea el nombre correcto")
            print("\n\n")
        if read_ok:
            if len(data.columns) == 12:
                print("El archivo se ha leido de manera correcta. Numero de columas correcto")
                ncol_ok = True
            else:
                print("Numero de columnas incorrecto, chequear separador")
                print(data.head())
                print("\n\n")

        if ncol_ok:
            data_ok = True
        else:
            read_ok = False
            ncol_ok = False

    return data


def mayor_gasto_mensual(data):

    """
    Funcion que calcula el mayor gasto mensual 
    Paramatros:
        data: dataframe proveniente de la funcion read_data
    Output:
        mes: string del mes en que se ha gastado mas 
        total: float del monto del mes que mas se ha gastado
    """
        
    # Convertimos data a numerica
    data_gastos = data.apply(pd.to_numeric, errors='coerce')

    # Eliminamos valores positivos
    data_gastos[data_gastos>0] = 0

    # Sumamos y ordenamos
    gastos_mensuales = pd.DataFrame(data_gastos.sum(axis=0))
    gastos_mensuales.sort_values(by=0, inplace=True)
    mes = gastos_mensuales.index[0]
    total = gastos_mensuales[0].iloc[0]
    
    return (mes, total)


def mayor_ahorro_mensual(data):
    """
    Funcion que calcula el mayor ahorro mensual 
    Paramatros:
        data: dataframe proveniente de la funcion read_data
    Output:
        mes: string del mes en que se ha ahorrado mas 
        total: float del monto del mes que mas se ha ahorrado
    """

    # Convertimos data a numerica
    data = data.apply(pd.to_numeric, errors='coerce')

    #  Sumatoria por mes
    ahorro_mensual = pd.DataFrame(data.sum(axis=0))
    ahorro_mensual.sort_values(by=0, ascending=False, inplace=True)
    mes = ahorro_mensual.index[0]
    total = ahorro_mensual[0].iloc[0]
    return (mes, total)

def gastos_media_mean_anual(data):
    """
    Funcion que calcula el gasto medio y promedio del año
    Paramatros:
        data: dataframe proveniente de la funcion read_data
    Output:
        gasto_promedio: float del gasto promedio de los gastos producidos en el año
        gasto_medio: float del gasto medio de los gastos producidos en el año
    """

    # Convertimos data a numerica
    data = data.apply(pd.to_numeric, errors='coerce')
    gastos_list = [data.iloc[i,j]  for j in range(0, len(data.columns)) for i in range(0,len(data)) if data.iloc[i,j] < 0]

    # Calculo de gasto promedio y medio del año
    gasto_promedio = round(np.mean(gastos_list), 2)
    gasto_medio = round(np.median(gastos_list), 2)

    return (gasto_promedio, gasto_medio)


def gastos_ingresos_ano(data):
    """
    Funcion que calcula el gasto e ingresos del año
    Paramatros:
        data: dataframe proveniente de la funcion read_data
    Output:
        gastos_ano: float de los gastos totales del año
        ingresos_ano: float de los ingresos totales del año
    """

    # Convertimos data a numerica
    data = data.apply(pd.to_numeric, errors='coerce')

    # DF necesarios
    data_gastos = data.copy()
    data_gastos[data_gastos>0] = 0
    gastos_mensuales = pd.DataFrame(data_gastos.sum(axis=0))

    data_ingresos = data.copy()
    data_ingresos[data_ingresos<0] = 0
    ingresos_mensuales = pd.DataFrame(data_ingresos.sum(axis=0))

    gastos_ano = gastos_mensuales.sum()[0]
    ingresos_ano = ingresos_mensuales.sum()[0]

    return (gastos_ano, ingresos_ano)




