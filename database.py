from datetime import datetime
from decimal import Decimal
from pony.orm import *

db = Database()

class Usuario(db.Entity):
    _table_ = 'usuarios'
    id = PrimaryKey(int, auto=True)
    chat_id = Optional(int)
    nome = Optional(str, 300)
    carteira = Optional(str, 300)
    data = Optional(datetime)
    saldo = Optional(Decimal, precision=16, scale=8)
    total_deposito = Optional(Decimal, precision=16, scale=8)
    total_saque = Optional(Decimal, precision=16, scale=8)

@db_session
def user_exist(chat_id):
    ""
    return True if Usuario.get(chat_id=chat_id) else None

@db_session
def create_user(id , chat_id, nome, carteira, data=None, saldo=0, total_deposito=0, total_saque=0):
    data = datetime.utcnow()
    Usuario(id=id,
            chat_id=chat_id,
            nome=nome,
            carteira=carteira,
            data=data,
            saldo=saldo,
            total_deposito=total_deposito,
            total_saque=total_saque
            )

@db_session
def insert_saque(userid, saque):
    user = Usuario[userid]
    user.total_saque = saque


@db_session
def insert_deposito(userid, deposito):
    user = Usuario[userid]
    user.total_deposito = deposito

@db_session
def insert_wallet(userid, wallet):
    user = Usuario[userid]
    user.carteira = wallet

@db_session
def change_name(userid, name):
    user = Usuario[userid]
    user.name = name

@db_session
def consultar_saque(userid):
    user = Usuario[userid]
    return user.total_saque

@db_session
def consultar_deposito(userid):
    user = Usuario[userid]
    return user.total_deposito

@db_session
def consultar_saldo(userid):
    user = Usuario[userid]
    return user.saldo


if __name__ == "__main__":
    print("Criando tabelas...")
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
    set_sql_debug(True)
    print("Bando de dados criado com sucesso!")
