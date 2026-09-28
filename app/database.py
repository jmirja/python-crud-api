from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:password@localhost/python_crud_db"

engine = create_engine(DATABASE_URL)