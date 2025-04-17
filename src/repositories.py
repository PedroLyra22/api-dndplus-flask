from db.config import get_db_connection
from src.models import Raca
from flask import jsonify
from pymysql.cursors import DictCursor

class RacaRepository:
    @staticmethod
    def find_all():
        connection = get_db_connection()
        with connection.cursor(DictCursor) as cursor:
            sql = """
            SELECT id, nome, tipo_de_criatura, tamanho, velocidade, tracos_especiais, descricao
            FROM raca
            """
            cursor.execute(sql)
            rows = cursor.fetchall()
        connection.close()

        racas = [Raca(**row) for row in rows] if rows else []
        return jsonify([raca.__dict__ for raca in racas])

    @staticmethod
    def find_all_names():
        connection = get_db_connection()
        with connection.cursor(DictCursor) as cursor:
            sql = """
            SELECT id, nome FROM raca
            """
            cursor.execute(sql)
            rows = cursor.fetchall()
        connection.close()

        return jsonify(rows)