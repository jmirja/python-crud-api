from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:123456@localhost/python_crud_db"

engine = create_engine(DATABASE_URL)