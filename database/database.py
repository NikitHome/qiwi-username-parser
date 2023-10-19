import pymysql


def connect_db():
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='Admin',
            password='12345',
            database='usernames',
            cursorclass=pymysql.cursors.DictCursor
        )
        
        print("Successfully connected...")
        print("#" * 20)
        
        try:
            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE IF NOT EXIST `users`(id int AUTO_INCREMENT," \
                                " num_phone varchar(32), PRIMARY KEY (id)" \
                                " name varchar(32));"
                                
                cursor.execute(create_table_query)
                print("Table created successfully")
            
        finally:
            connection.close()
        
    except Exception as ex:
        print("Connection refused...")
        print(ex)
        
    return connection


def insert(only_num_mess, owner):
    connection = connect_db()
    
    with connection.cursor() as cursor:
        insert_query = f"INSERT INTO `users` (num_phone, name) VALUES ('{only_num_mess}', '{owner}');"
        cursor.execute(insert_query)
        connection.commit()