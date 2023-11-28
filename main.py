# from sqlite3 import *
# def creardb():
#     conn=connect("databases.db")
#     conn.commit()
#     conn.close()
# def crearTabla():
#     conn=connect("databases.db")
#     cursor=conn.cursor()
#     sentencia="""
#         CREATE TABLE Alumnos(
#          id INTEGER PRIMARY KEY AUTOINCREMENT,
#          nombre text(250),
#          edad integer
#         )
#     """
#     cursor.execute(sentencia)
#     conn.commit()
#     conn.close()
# def insertarUno(nombre,edad):
#     conn=connect("databases.db")
#     cursor=conn.cursor()
#     sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES('{nombre}',{edad})"
#     cursor.execute(sentencia)
#     conn.commit()
#     conn.close()
# def insertaVarios(lista):
#     conn=connect("databases.db")
#     cursor=conn.cursor()
#     sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES(?,?)"
#     cursor.executemany(sentencia,lista)
#     conn.commit()
#     conn.close()
# if __name__=="__main__":
#     #crearTabla()
#     #insertarUno("jose",30)
#     #insertarUno("milan",7)
#     array=[
#         ("silvia",20),
#         ("adriano",3),
#         ("silda",22),
#         ("mirella",19),
#         ("mercedes",20),
#     ]
#     insertaVarios(array)

import orm
import Tablas.Alumnos as Al
import Tablas.Cursos as Cu
db=orm.SQLiteORM("mi_data_bases")
db.create_table(Al.Alumnos)
db.create_table(Cu.Cursos)

data={"nombre":"amtonio","edad":15}
db.insert("Alumnos",data)