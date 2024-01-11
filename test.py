import datetime

# Introduce la fecha de nacimiento en formato 'YYYY-MM-DD'
fecha_nacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")
# Calcula la edad a partir de la fecha de nacimiento
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
edad = datetime.datetime.now().year - fecha_nacimiento.year
edad = datetime.datetime.now().year - fecha_nacimiento.year
edad = datetime.datetime.now().year - fecha_nacimiento.year
# Imprime la edad calculada

print("Tu edad es:", edad)


db_url_prueba = "mysql+pymysql://root:test@127.0.0.1:3306/esquema"

