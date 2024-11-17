# Librerías

# !pip install faker          # para instalar en caso de no tener la librería
from faker import Faker
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression


# Funciones

def filter_dataframe(df, columna:str, umbral:float):
  """
    Función que recibe un dataframe y filtra los valores mayores a un umbral dado.

    Entrada:  df -> Dataframe a filtrar
              columna -> Columna del dataframe a filtrar
              umbral -> Valor al que tiene que ser mayor

    Salida:   df_filtrado -> Dataframe filtrado
  """
  df_filtrado = df[df[columna] > umbral]

  return df_filtrado

def generate_regression_data(n_samples):
    """
    Función para generar datos simulados relacionados con animales para un problema de regresión.

    Entrada:  n_samples -> Número de muestras a generar (entero positivo).

    Salida:   df -> DataFrame con las variables independientes y dependiente.
    """
    fake = Faker()

    # Generar variables independientes
    variables_independientes = {
        "peso_kg": [fake.random_int(min=1, max=500) for _ in range(n_samples)],  # peso (1 - 500 kg)
        "edad_años": [fake.random_int(min=0, max=20) for _ in range(n_samples)],  # edad (0 y 20 años)
        "longitud_cm": [fake.random_int(min=30, max=300) for _ in range(n_samples)]  # longitud (30 y 300 cm)
    }
    df = pd.DataFrame(variables_independientes)

    # Generar variable dependiente
    df["consumo_alimento_kg"] = (
        df["peso_kg"] * 0.05 +
        df["edad_años"] * 0.3 +
        df["longitud_cm"] * 0.02 +
        fake.random_number(digits=2)
    )

    # separar en serie y dataframe
    y = df["consumo_alimento_kg"]
    X = df.drop("consumo_alimento_kg", axis=1)

    return X, y

def train_multiple_linear_regression(X, y):
    """
    Función para entrenar un modelo de regresión lineal múltiple.

    Entrada:  X -> DataFrame con las variables independientes.
              y -> Serie con la variable dependiente.

    Salida:   modelo -> Modelo entrenado de LinearRegression.
    """
    # Crear modelo
    modelo = LinearRegression()

    # Entrenar el modelo con los datos ingresados
    modelo.fit(X, y)

    return modelo

def flatten_list(lista_de_listas):
    """
    Función que toma una lista de listas y la convierte en una lista plana
    utilizando list comprehensions anidados.

    Entrada: lista_de_listas -> Una lista con varias listas.

    Salida: lista_plana -> Una lista con los datos de varias en una sola.
    """
    lista_plana = [elemento for sublista in lista_de_listas for elemento in sublista]

    return lista_plana

def group_and_aggregate(df, columna_agrupar:str, columna_agregar:str):
    """
    Función para agrupar un DataFrame por una columna y calcular la media de otra columna.

    Entrada:    df -> DataFrame de entrada.
                columna_agrupar -> Nombre de la columna para agrupar (str).
                columna_agregar -> Nombre de la columna para calcular la media (str).

    Salida:     df_agrupado -> DataFrame con los valores agrupados y la media calculada.
    """
    # Agrupar y calcular la media
    df_agrupado = df.groupby(columna_agrupar)[columna_agregar].mean().reset_index()

    df_agrupado.rename(columns={columna_agregar: f"{columna_agregar}"}, inplace=True)

    return df_agrupado

def train_logistic_regression(X, y):
    """
    Función para entrenar un modelo de regresión logística con un conjunto de datos binarios.

    Entrada:      X -> DataFrame con las características.
                  y -> Serie con las etiquetas.

    Salida:       modelo -> Modelo entrenado de regresión logística.
    """
    # Crear modelo
    modelo = LogisticRegression()

    # Entrenar
    modelo.fit(X, y)

    return modelo

def apply_function_to_column(df, nombre_columna:str, funcion):
    """
    Aplica una función personalizada a cada valor de una columna en un DataFrame.

    Entrada:      df: DataFrame de entrada.
                  nombre_columna: Nombre de la columna a la que se aplicará la función.
                  funcion: Función a aplicar.

    Salida:       df -> DataFrame original pero con la columna modificada por la función
    """

    df[nombre_columna] = df[nombre_columna].apply(funcion)

    return df

def filter_and_square(lista_numeros):
    """
    Filtra los valores mayores a 5 de una lista y devolver los cuadrados de estos números.

    Entrada:      lista_numeros -> Una lista de números a procesar.

    Salida:       lista_procesada -> Una lista de los cuadrados de los números mayores que 5.
    """

    lista_procesada = [numero ** 2 for numero in lista_numeros if numero > 5] # filtrar y elevar al cuadrado

    return lista_procesada