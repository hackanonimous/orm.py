import sqlite3
import json

class SQLiteORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f"{db_name}.db")
        self.cursor = self.conn.cursor()

    def create_table(self, table_definition):
        # Crea una tabla a partir de la definición en formato JSON
        for table_name, columns in table_definition.items():
            columns_str = ", ".join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
            query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns_str})"
            self.cursor.execute(query)
        self.conn.commit()

    def insert(self, table_name, data):
        # Inserta un nuevo registro en la tabla
        columns = ', '.join(data.keys())
        values = ', '.join([f":{key}" for key in data.keys()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(query, data)
        self.conn.commit()

    def update(self, table_name, data, where):
        # Actualiza registros en la tabla
        set_clause = ', '.join([f"{key} = :{key}" for key in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where}"
        self.cursor.execute(query, data)
        self.conn.commit()

    def delete(self, table_name, where):
        # Elimina registros de la tabla
        query = f"DELETE FROM {table_name} WHERE {where}"
        self.cursor.execute(query)
        self.conn.commit()

    def select(self, table_name, where=None):
        # Realiza una consulta SELECT
        query = f"SELECT * FROM {table_name}"
        if where:
            query += f" WHERE {where}"

        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]

        results = []
        for row in rows:
            result_dict = dict(zip(columns, row))
            results.append(result_dict)

        return results

    def close(self):
        self.conn.close()
