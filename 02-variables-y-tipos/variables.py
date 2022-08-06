"""
Una variable es un contenedor de información
que dentro guardará un dato.
Se pueden crear muchas variables y cada una puede tener un dato distinto 
"""

# Aquí creamos algunas variables y le asignamos valor
texto = "Aprendiz de Python"
texto2 = "en clase" 
número = 1
texto3 = "ya llevamos"
decimal = 2.5
texto4 = "horas"

# Aquí mostramos el valor de las variables creadas anteriormente
print(texto)
print(texto2)
print(número)
print(texto3) 
print(decimal)
print(texto4)

# Aquí vemos que si cambio el valor de una variable, y luego pido mostrar, 
# se visualizará el último valor asignado
decimal = 2.8
print(decimal) 
# Esto se llama: sustitución/reasignación de variables/valores


# CONCATENACIÓN
nombre = "Eva"
apellido = "Barrios"
ocupación = "Profesora de Matemática"

# A continuación, tres maneras de concatenar
# 1) En una línea con el signo "+"
print(nombre + " " + apellido + "-" + ocupación) 
# 2) Con uso de "f" delante de un string y doble llave, permite interpolar
print(f"{nombre} {apellido} - {ocupación}") # OBS: Alt+123 y Alt+125 para llaves
# 3) Con función/método "format", y uso de llaves:
print("Hola, mi nombre es {} {} y soy {}".format(nombre, apellido, ocupación))