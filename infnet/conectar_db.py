from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os, configparser

CONFIG = "config.txt"

def ler_config():
    dir_corrente = os.path.dirname(__file__)
    config = os.path.join(dir_corrente, CONFIG)
    params = configparser.ConfigParser()
    params.read(config)
    return params

def conectar():
    try:
        params = ler_config()
        #engine = create_engine("mysql+pymysql://root:lpmaia@localhost/infnet", echo=True)
        engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                               .format(user=params.get("DB", "username"),
                                       pw=params.get("DB", "password"),
                                       host=params.get("DB", "host"),
                                       db=params.get("DB", "database")))
        session = sessionmaker(bind=engine)()
    except Exception as ex:
        print(ex)
    return session

def desconectar(session):
    if (session):
        session.close_all()
