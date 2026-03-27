import pandas as pd
from datapreputils import delete_null_values,replace_missing_values, min_max, z_score,mode, harmonic_mean, geometric_mean, remove_duplicates, mean_normalization
from datapreputils import median_function

data = [10,None, 20, 20, 30, 40, None]

print("Datos:", data)

#Limpieza
print("\n--- Limpieza de datos ---")

df = pd.DataFrame(data)
data_clean = replace_missing_values(df, method="mean")
data_clean1 = delete_null_values(data_clean)
data_clean2 = remove_duplicates(data_clean1)


print("\nDataFrame original:")
print(df)
print("\nReemplazar valores faltantes:")
print(data_clean)
print("\nEliminar valores nulos:")
print(data_clean1)
print("\nEliminar duplicados")
print(data_clean2)

#Estadisticas

# Convertir a lista
new_data_list = data_clean2[0].tolist()

print("\n--- Estadísticas ---")
print("Moda:", mode(new_data_list))
print("Media armónica:", harmonic_mean(new_data_list))
print("Media geométrica:", geometric_mean(new_data_list))

#Normalizacion
print("\n--- Normalización ---")
print("Min-Max:", min_max(new_data_list))
print("Z-score:", z_score(new_data_list))
print("Media Normalizada:", mean_normalization(new_data_list))

print("Personalizacion de modulo")
print("Media armónica:", harmonic_mean(new_data_list))

print("Añadiendo la función de calculo de mediana")
print("Valor de la mediana", median_function(new_data_list))