# Proyecto de Funciones en Python

Este proyecto contiene funciones diseñadas para resolver tareas comunes utilizando Python.
---

### 1. Generación de datos de regresión
**Función:** `generate_regression_data`

Genera un conjunto de datos sintéticos para problemas de regresión, con variables independientes y una variable dependiente basada en características de animales.

**Uso:**
```python
X, y = generate_regression_data(100)
print(X.head(), y.head())
```

### 2. Entrenar modelo de regresión lineal múltiple
**Función:** `train_multiple_linear_regression`

Entrena un modelo de regresión lineal múltiple utilizando un conjunto de datos de entrada.

**Uso:**
```python
modelo = train_multiple_linear_regression(X, y)
print(modelo.coef_, modelo.intercept_)
```

### 3. Aplanar listas anidadas
**Función:** `flatten_list`

Convierte una lista de listas en una lista plana utilizando list comprehensions.

**Uso:**
```python
lista_aplanada = flatten_list([[1, 2], [3, 4], [5]])
print(lista_aplanada)  # [1, 2, 3, 4, 5]
```

### 4. Agrupar y calcular la media
**Función:** `group_and_aggregate`

Agrupa un DataFrame por una columna y calcula la media de otra.

**Uso:**
```python
result = group_and_aggregate(df, "category", "values")
print(result)
```


### 5. Entrenar modelo de regresión logística
**Función:** `train_logistic_regression`

Entrena un modelo de regresión logística con un conjunto de datos binarios.

**Uso:**
```python
modelo = train_logistic_regression(X, y)
print(modelo.predict(X))
```



### 6. Aplicar función personalizada a una columna
**Función:** `apply_function_to_column`

Aplica una función personalizada a cada valor de una columna en un DataFrame.

**Uso:**
```python
df_modificado = apply_function_to_column(df, "nombre", lambda x: x.upper())
print(df_modificado
```

### 7. Filtrar y elevar al cuadrado
**Función:** `filter_and_square`

Filtra números mayores que 5 de una lista y devuelve sus cuadrados.

**Uso:**
```python
cuadrados = filter_and_square([1, 6, 8, 2])
print(cuadrados)  # [36, 64]
```





