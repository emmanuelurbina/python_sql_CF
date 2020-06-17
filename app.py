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
            if users:
                return users
            return "No hay usuarios"
        except:
            return "No se pudo completar la consulta"

    @classmethod
    def new_user(cls, username, password, email):
        try:
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
        except:
            print("Ocurrio un error")

    @classmethod
    def get_user_by_id(cls, id):
        try:
            user = User.select().where(User.id == id).get()
            return user
        except User.DoesNotExist as err:
            return "No se pudo completar la consulta "

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

    @classmethod
    def last_user(cls):
        try:
            user = User.select().order_by(User.id.desc()).limit(1).get()
            if user:
                return user
            return "No hay usuarios"
        except:
            return "No se pudo realizar la consulta"


class Store(pw.Model):
    user = pw.ForeignKeyField(User, primary_key=True)
    name = pw.CharField(max_length=50)
    address = pw.TextField()
    active = pw.BlobField(default=True)
    create_at = pw.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'stores'

    @classmethod
    def new_store(cls, user, name, address):
        Store.create(user=user, name=name, address=address)

    @classmethod
    def get_store_by_userId(cls, id):
        try:
            store = Store.select().where(Store.user == id).get()
            if store:
                return store
            return "No hay tiendas"
        except:
            return "No se pudo realizar la consulta"

    def __str__(self):
        return self.name


if __name__ == "__main__":
    if not User.table_exists():
        User.create_table()
    if not Store.table_exists():
        Store.create_table()

    store = Store.get_store_by_userId(1)
    print(store)
