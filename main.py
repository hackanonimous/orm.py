import orm
import json
import Tablas.Alumnos as Al
import Tablas.Cursos as Cu
db=orm.SQLiteORM("mi_data_bases")
db.crear_tabla(Al.Alumnos)
db.crear_tabla(Cu.Cursos)

# data={"nombre":"amtonio","edad":15}
# db.insertarUno("Alumnos",data)
resultado=db.mostrar("Alumnos")
print(resultado)