from ast import If
from cmd import PROMPToso


#perro = "santi" #asignamos a la variable perro, el string santi
#print("hola mundo") #aca hice una impresion en pantalla de un string

perro = input("como se llama tu perro?") #creamos un condicional y una entrada de texto para comparar el nombre de tu perro y mostrar mensajes dependiendo del ingreso del string del usuario
if perro == "santi": print("feliz dia "+perro)
else: print("feliz dia aunque te llames "+perro)
