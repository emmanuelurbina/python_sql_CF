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

    def __str__(self):
        return self.username

    @classmethod
    def all_users(cls):
        try:
            users = User.select()
            return users
        except:
            return "No se pudo completar la consulta"

    @classmethod
    def new_user(cls, username, password, email):
        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.save()

    @classmethod
    def get_user_by_id(cls, id):
        try:
            user = User.select().where(User.id == id).get()
            return user
        except:
            return "No se pudo completar la consulta"

    @classmethod
    def update_status_user(cls, id, status):
        user = User.get_user_by_id(id)
        user.active = status
        user.save()

    @classmethod
    def update_email_user(cls, id, email):
        user = User.get_user_by_id(id)
        user.email = email
        user.save()

    @classmethod
    def delet_user(cls, id):
        user = User.get_user_by_id(id)
        user.delete_instance()


if __name__ == "__main__":
    if not User.table_exists():
        User.create_table()

    # User.new_user("emmanuelurbina", "124", "emmanuelluur@gmail.com")
    # Obtiene usuario
    user = User.get_user_by_id(3)
    print(user)
    user = User.delet_user(3)
