import peewee as pw
from datetime import datetime
HOST = "localhost"
USER = "root"
PASSWORD = ""
DB = "minicurso_mysql"
PORT = 3306

db = pw.MySQLDatabase(database=DB,
                      host=HOST,
                      port=PORT,
                      user=USER,
                      passwd=PASSWORD)


class User(pw.Model):
    username = pw.CharField(unique=True, max_length=50, index=True)
    password = pw.CharField(max_length=50)
    email = pw.CharField(max_length=50, null=True)
    active = pw.BooleanField(default=True)
    create_at = pw.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'users'


if __name__ == "__main__":
    if not User.table_exists():
        User.create_table()

    user = User.create(username="emmanuelluur",
                       password="123456",)
