import config
import psycopg2
import psycopg2.extras
from dataClasses.sqlResultStatus import SqlStatusResult

def createConnection():
    params = config.getPostgresConnectionConfig()
    conn = psycopg2.connect(**params)
    return conn

def execute(command):
    try:        
        connection = createConnection()
        with connection.cursor() as cursor:
            cursor.execute(command)
            connection.commit()
        return SqlStatusResult(isSuccess=True, description="command is executed successfully")

    except Exception as err:
        return SqlStatusResult(isSuccess=False,description=err)

    finally:
        connection.close()

def executeMany(command, df):
    try:
        connection = createConnection()
        with connection.cursor() as cursor:
            for index, row in df.iterrows():
                cursor.execute(command, row.to_dict())
            connection.commit()
        return SqlStatusResult(isSuccess=True,description="all data is inserted successfully")

    except Exception as err:
        return SqlStatusResult(isSuccess=False, description=err)

    finally:
        connection.close()

def selectData(command, params):
    try:
        connection = createConnection()
        result = []        
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(command, params)
            for row in cursor.fetchall():
                result.append(dict(row))
        return SqlStatusResult(isSuccess=True, data=result)

    except Exception as err:
        return SqlStatusResult(isSuccess=False, description=err)

    finally:
        connection.close()





