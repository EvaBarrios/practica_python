# 1) se debe desarrollar un programa que: 
# a) solicite la edad al usuario, 
# b) pregunte si es humano o perro, 
# c) calcule su edad en función de su especie


entrada_usuario=input("hace cuántos años naciste? Ingresa número ")
condicion=input("si ud es humano ingrese A, si es perro, ingrese B ")

edad=int(entrada_usuario)
edad_perro=edad*7

if condicion =="A": print("ud tiene "+str(edad)+" años")
else: print("ud tiene "+str(edad_perro)+" años")



