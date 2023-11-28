import os
import orm
actual=os.getcwd()
lista_archivos=os.listdir(f"{actual}/Tablas")
for archivos in lista_archivos:
    print(archivos[:-3])
print(orm.suma(4,5))