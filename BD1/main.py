import sqlite3

#Crear o actualizar la DB
connection = sqlite3.connect('example.db')

#El cursor es el que hace las consultas
cursor = connection.cursor()

#Crear o utilizar una tabla
cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            rol TEXT NOT NULL
            )
''')

#Insertar datos
user_data= [
        ('Basir', 15, 'normal'),
        ('Ana', 25, 'admin'),
        ('Luis', 35, 'normal'),
        ('Maria', 28, 'admin')
    ]
cursor.executemany("INSERT INTO users (name, age, rol) VALUES (?, ?, ?)", user_data)
connection.commit()

#Consultar datos
cursor.execute("SELECT * FROM users")
#Agarro los usuarios y los guardo en una variable
users = cursor.fetchall()

print("------ Usuarios en la base de datos ------")

for user in users:
    print(f"User -> {user[1]} | Age -> {user[2]} | Rol -> {user[3]}")
    
#Cerrar la conexion
connection.close()