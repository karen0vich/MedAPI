import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def init_database():

    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='password',
        host='localhost'
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE medical_system")
    cursor.execute("CREATE USER medical_user WITH PASSWORD 'medical_password'")
    cursor.execute("GRANT ALL PRIVILEGES ON DATABASE medical_system TO medical_user")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_database()

