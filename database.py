from datetime import datetime
from decimal import Decimal
from pony.orm import *


db = Database()

class Oriondb (db.Entity):
    _table_ = 'oriondb'
    id = PrimaryKey(int, auto=True)
    chat_id = Optional(int, size=16)
    nome = Optional(str, 300)
    carteira = Optional(str, 300)
    data = Optional(datetime)
    total_deposito = Optional(Decimal, precision=16, scale=8)
    total_saque = Optional(Decimal, precision=16, scale=8)

db.bind(provider='sqlite', filename='database.Orion', create_db=True)
db.generate_mapping(create_tables=True)
set_sql_debug(True)

@db_session
def oriondb_exist(chat_id):
    return True if oriondb.get(chat_id=chat_id) else None

@db_session
def oriondb_create(chat_id,nome,carteira,data,total_deposito,total_saque ):
    oriondb(chat_id=chat_id,nome=nome,carteira=carteira,data=data,total_deposito=total_deposito,total_saque=total_saque)









'''with db_session:
    user_id = oriondb(chat_id=message.from_user.id)
    nome_id = oriondb(nome=message.from_user.username)
    carteiraNST= oriondb(carteira=message.chat.text)
    saldo_deposito= oriondb (total_deposito =message.chat.text)
    saldo_saque= oriondb (total_saque =message.chat.text)
'''