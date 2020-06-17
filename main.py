import pymysql.cursors

host = "localhost"
user = "root"
password = ""
database = "minicurso_mysql"
user_schema = """
CREATE TABLE IF NOT EXISTS `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;
"""
insert_new_user = """
    INSERT INTO users (username, password) VALUES('{}', '{}')
 """
get_user_by_id = """
    SELECT * FROM users WHERE id = '{}'
"""
update_user_by_id = """
    UPDATE users SET password='{}' WHERE id='{}'
"""
delete_user_by_id = "DELETE FROM users WHERE id='{}'"
if __name__ == "__main__":
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=database)
    try:
        # crea tabla
        """
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS users")
            cursor.execute(user_schema)
        """

        # Ingresa nuevo usuario

        """
        with connection.cursor() as cursor:
            # se ejectuan las sentencias sql



            username = input("Ingrese Username: ")
            password_user = input("Ingrese password: ")
            cursor.execute(insert_new_user.format(username, password_user))
            connection.commit()
        """
        # actualiza registro
        """
        with connection.cursor() as cursor:
            id_user = int(input("Ingrese ID a modificar: "))
            password_user = input("Ingrese Nuevo password: ")
            cursor.execute(update_user_by_id.format(password_user, id_user))
            connection.commit()
        """
        """
        with connection.cursor() as cursor:
            cursor.execute(get_user_by_id.format(1))
            results = cursor.fetchone()
            print(results)
        """
        with connection.cursor() as cursor:
            id_user = int(input("ID a elminiar: "))
            cursor.execute(delete_user_by_id.format(id_user))
            connection.commit()
    except pymysql.Error as error:
        print("Ocurrio un error \n Descripción error: {}".format(error))
    finally:
        # Cierra Conexíon
        connection.close()
