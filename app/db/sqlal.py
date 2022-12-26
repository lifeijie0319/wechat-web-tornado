from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine():
    engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:50000/wxdb', echo=True)
    return engine


def get_session(engine=get_engine()):
    Session = sessionmaker(bind=engine)
    db_session = Session()
    return db_session
