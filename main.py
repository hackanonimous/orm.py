import orm
import Tablas.Alumnos as Al
import Tablas.Cursos as Cu
db=orm.SQLiteORM("mi_data_bases")
db.create_table(Al.Alumnos)
db.create_table(Cu.Cursos)

data={"nombre":"amtonio","edad":15}
db.insert("Alumnos",data)