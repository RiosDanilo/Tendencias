

#Integrantes Danilo Rios, Alejandro Muñoz


from cmath import e
from flask import Flask,jsonify, request
from config import config
from flaskext.mysql import MySQL

#from flask mysqlclient import MySQL
#from flask import MySQL

app = Flask(__name__)
conexion = MySQL(app)

@app.route('/madrid')
def listar_madrid():
    try:
        madrid=conexion.connection.madrid()
        sql = "SELECT #Jugadores, Nombre, Edad FROM madrid"
        madrid.execute(sql)
        datos = madrid.fetchall()
        madrid=[]
        for fila in datos:
            madrid = {'#Jugadores': fila[0], 'Nombre': fila[1], 'Edad': fila[2]}
            madrid.append(madrid)
        return jsonify({'madrid': madrid, 'mensaje': "Estos son los jugadores listados en el equipo."})
    except Exception as e: 
        return jsonify({'mensaje': "Error al listar."})

@app.route('/madrid/<Nombre>')
def leer_madrid(Nombre):
    try:
        madrid=conexion.connection.madrid()
        sql="SELECT #Jugadores, Nombre, Edad FROM madrid WHERE Nombre = '{0}'".format(Nombre)
        madrid.execute(sql)
        datos=madrid.fetchone()
        if datos!= None:
            madrid = {'#Jugadores':datos[0], 'Nombre':datos[1], 'Edad':datos[2]}
            return jsonify({'madrid':madrid,'mensaje':"Equipo Encontrado."})
        else:
            return jsonify({'mensaje':"Equipo no encontrado."})
    except Exception as e:
        return jsonify({'mensaje':"Error"})

@app.route('/madrid')#Este es el metodo POST
def registrar_madrid():
    try:
        madrid=conexion.connection.madrid()
        sql="""INSERT INTO  madrid (#Jugadores, Nombre, Edad)
         VALUES ('{0}','{1}','{2}')""".format(request.json['#Jugadores'], request.json['Nombre'], request.json['Edad'])
        madrid.execute(sql)
        conexion.connection.commit()
        return({'mensaje':"Equipo registrado."})
    except Exception as e:
        return jsonify({'mensaje':"Error"})

@app.route('/madrid/<Nombre>')#Este es el metodo PUT
def modificar_madrid(Nombre):
    try:
        madrid=conexion.connection.madrid()
        sql="UPDATE madrid SET Nombre = '{0}', Edad = '{1}' WHERE #Jugadores = '{2}'".format(request.json['Nombre'], request.json['Edad'], Nombre)
        madrid.execute(sql)
        conexion.connection.commit()
        return({'mensaje':"madrid actualizado."})
    except Exception as e:
        return jsonify({'mensaje':"Error"})

@app.route('/madrid/<Nombre>')#Este es el metodo DELETE
def eliminar_madrid(Nombre):
    try:
        madrid=conexion.connection.madrid()
        sql=" DELETE FROM madrid WHERE #Jugadores = '{0}'".format(Nombre)
        madrid.execute(sql)
        conexion.connection.commit()
        return({'mensaje':"madrid eliminado."})
    except Exception as e:
        return jsonify({'mensaje':"Error"})

def pag_no_encontrada(error):
    return "<h1>La página que buscas no existe</h1>",404 #Mensaje de eror

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pag_no_encontrada)
    app.run()