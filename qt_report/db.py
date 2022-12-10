
from cryptography.fernet import Fernet
import cx_Oracle

_key = Fernet.generate_key()
print(_key)

def encrypt(message):
    f = Fernet(_key)
    return f.encrypt(message.encode()).decode()

def decrypt(message):
    f = Fernet(_key)
    return f.decrypt(message.encode()).decode()

def get_db_connection(db_name, Databases):
    db = Databases[db_name]
    dsn = db['db']
    token = db['token']
    username, password = decrypt(token).split('/')
    conn = cx_Oracle.connect(username, password, dsn)
    return conn
