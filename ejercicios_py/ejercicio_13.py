###Pregunta 1
# Definimos la variable "nombre" con el valor "HUmberto"
nombre = "HUmberto"

# Mostramos el mensaje de saludo por pantalla
print(f"¡Hola {nombre}!")

###Pregunta 2
# Definimos las variables
a = 3
b = 2
c = 5

# Calculamos la expresión paso a paso

resultado = ((a + b) / (2 * c)) ** 2

# Mostramos el resultado por pantalla
print("resultado"+str(resultado))

###Pregunta 3
# Se solicitan al usuario las horas trabajadas y el coste por hora
horas_trabajadas = float(input("¿Cuántas horas has trabajado? "))
coste_hora = float(input("¿Cuál es tu coste por hora? "))

# Se calcula la paga total
paga_total = horas_trabajadas * coste_hora

# Se muestra la paga total por pantalla
print(f"Tu paga total es de {paga_total:.2f} €")

###Pregunta 4

# Se solicitan al usuario los dos números enteros
numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))

# Se calcula la división entera y el resto
cociente = numero1 // numero2
resto = numero1 % numero2

# Se muestran los resultados por pantalla
print(f"El cociente de la división es {cociente}")
print(f"El resto de la división es {resto}")

###Pregunta 5
# Se solicitan al usuario los datos necesarios para el cálculo
cantidad_invertir = float(input("¿Cuánto dinero desea invertir? "))
interes_anual = float(input("¿Cuál es el interés anual porcentual? "))
numero_anios = int(input("¿Cuántos años desea invertir? "))

# Se calcula el capital final
capital_final = cantidad_invertir * (1 + interes_anual / 100) ** numero_anios

# Se muestra el capital final por pantalla
print(f"El capital final de su inversión será de {capital_final:.2f} €")


###Pregunta 6

# Se solicitan al usuario el número de payasos y muñecas vendidos
numero_payasos = int(input("¿Cuántos payasos se han vendido? "))
numero_munecas = int(input("¿Cuántas muñecas se han vendido? "))

# Se calcula el peso total del paquete
peso_total = numero_payasos * 112 + numero_munecas * 75

# Se muestra el peso total por pantalla
print(f"El peso total del paquete es de {peso_total} gramos")


###Pregunta 7
# Lee el número de barras vendidas que no son del día
barras_no_frescas = int(input("Introduce el número de barras no frescas vendidas: "))

# Precio habitual de una barra de pan
precio_habitual = 3.49

# Calcula el descuento
descuento = 0.6  # 60% de descuento
precio_descuento = precio_habitual * descuento

# Calcula el coste final total
coste_total = barras_no_frescas * precio_descuento

# Muestra los resultados
print(f"Precio habitual de una barra de pan: {precio_habitual:.2f}€")
print(f"Descuento por no ser fresca: {precio_descuento:.2f}€")
print(f"Coste final total: {coste_total:.2f}€")

###Pregunta 8
def fahrenheit_a_centigrados(fahrenheit):
    centigrados = (fahrenheit - 32) * 5 / 9
    return centigrados

# Lee la temperatura en grados Fahrenheit
fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))

# Calcula la temperatura en grados centígrados
centigrados = fahrenheit_a_centigrados(fahrenheit)

# Muestra los resultados
print(f"{fahrenheit:.2f} grados Fahrenheit son equivalentes a {centigrados:.2f} grados centígrados.")

###Pregunta 9
def centigrados_a_kelvin(centigrados):
    kelvin = centigrados + 273.15
    return kelvin

# Lee la temperatura en grados centígrados
centigrados = float(input("Introduce la temperatura en grados centígrados: "))

# Calcula la temperatura en grados Kelvin
kelvin = centigrados_a_kelvin(centigrados)

# Muestra los resultados
print(f"{centigrados:.2f} grados centígrados son equivalentes a {kelvin:.2f} grados Kelvin.")


###Pregunta 10
# Número complejo dado
z = 2 + 3j

# Parte imaginaria
parte_imaginaria = z.imag

# Muestra el resultado
print(f"La parte imaginaria de z = {z} es {parte_imaginaria}.")

###Pregunta 11
# Número complejo dado
z = 4 + 2j

# Parte real
parte_real = z.real

# Muestra el resultado
print(f"La parte real de z = {z} es {parte_real}.")

###Pregunta 12
# Número complejo dado
z = 4 + 2j

# Conjugado
conjugado = z.conjugate()

# Muestra el resultado
print(f"El conjugado de z = {z} es {conjugado}.")

###Pregunta 13
# Número binario
binario = '1100001110'

# Convierte a decimal
decimal = int(binario, 2)

# Muestra el resultado
print(f"El equivalente en base decimal de '{binario}' es {decimal}.")

###Pregunta 14
# Valor flotante
flotante = 4.33

# Convierte a cadena
cadena = str(flotante)

# Muestra el resultado
print(f"El valor flotante {flotante} como cadena es '{cadena}'.")

###Pregunta 15
# Números
dividendo = 29
divisor = 5

# Calcula el cociente y el resto
cociente = dividendo // divisor
resto = dividendo % divisor

# Muestra los resultados
print(f"Cociente: {cociente}, Resto: {resto}")

###Pregunta 15
# Números
dividendo = 29
divisor = 5

# Calcula el cociente y el resto
cociente = dividendo // divisor
resto = dividendo % divisor

# Muestra los resultados
print(f"Cociente: {cociente}, Resto: {resto}")

###Pregunta 16
# Número decimal
decimal = 34567

# Convierte a hexadecimal
hexadecimal = hex(decimal)

# Muestra el resultado
print(f"El equivalente hexadecimal de {decimal} es {hexadecimal}.")

###Pregunta 17
# Número dado
numero = 45.67859245

# Aproximación a dos decimales
aproximacion = round(numero, 2)

# Muestra el resultado
print(f"La aproximación de {numero} a dos decimales es {aproximacion}.")

###Pregunta 18
# Número dado
numero = 3.556

# Redondea al entero más cercano
resultado = round(numero)

# Muestra el resultado
print(f"El número 4 se obtiene a partir de {numero}.")

###Pregunta 19
# Número dado
numero = 16.7844

# Redondea al entero más cercano
resultado = round(numero)

# Muestra el resultado
print(f"El número 17 se obtiene a partir de {numero}.")

###Pregunta 20
# Números
dividendo = 3.45
divisor = 1.22

# Calcula el resto
resto = dividendo % divisor

# Muestra el resultado
print(f"El resto de la división entre {dividendo} y {divisor} es {resto}.")

###Pregunta 21
# Números
base = 3.45
exponente = 1.22

# Calcula la potencia
resultado = base ** exponente

# Muestra el resultado
print(f"{base} elevado a la potencia {exponente} es igual a {resultado:.2f}.")





