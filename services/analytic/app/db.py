import mysql.connector    
from logger import logger




def db_connection():
    connect = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "root",
        "database": "digital_hunter"
    }

    try:
        conn = mysql.connector.connect(**connect)
        logger.info("The connection to mysql was successful.")
        return conn
    
    except Exception as e:
        logger.error("The connection to mysql failed.")
        return None

