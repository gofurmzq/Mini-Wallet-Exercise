# import sqlalchemy as sa
# from app.config import settings


# db_engine = sa.create_engine(
#     settings.DB,
#     pool_recycle=settings.DB_POOL_RECYCLE,
#     pool_size=settings.DB_POOL_SIZE,
#     pool_pre_ping=settings.DB_POOL_PRE_PING,
#     echo=settings.DB_ECHO
# )

# from app import settings
# from pymongo import MongoClient

# mongo_client = MongoClient(settings.MONGO_CONNECTION)
# mongo_db = mongo_client[settings.MONGO_DB]
