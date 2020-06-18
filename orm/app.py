from models import Store, User, Product, Category, CategoriesProducts


def create_tables():

    if CategoriesProducts.table_exists():
        CategoriesProducts.drop_table()

    if Category.table_exists():
        Category.drop_table()

    if Product.table_exists():
        Product.drop_table()

    if Store.table_exists():
        Store.drop_table()

    if User.table_exists():
        User.drop_table()

    User.create_table()
    Store.create_table()
    Product.create_table()
    Category.create_table()
    CategoriesProducts.create_table()


def create_users():
    User.new_user("emmanuelluur", "123", "example@ex.com")
    User.new_user("emmanuel", "123555", "example@ex.com")


def create_stores():
    Store.new_store(user=1, name='tienda facilita uno', address='Oficinas')
    Store.new_store(user=2, name='tienda facilita dos', address='Oficinas')


def create_products():
    Product.new_product(store=1, name='Pan',
                        description='Pan integral', price=5.5, stock=50)
    Product.new_product(store=1, name='Leche',
                        description='Baja en gradas', price=15.5, stock=100)
    Product.new_product(store=1, name='Jamon',
                        description='de pavo', price=30.9, stock=80)
    Product.new_product(store=1, name='mayonesa',
                        description='mayonesa', price=30.9, stock=80)

    Product.new_product(store=2, name='Soda',
                        description='Dieta', price=10.0, stock=50)
    Product.new_product(store=2, name='Fritura',
                        description='Frituras de papa', price=20.5, stock=100)
    Product.new_product(store=2, name='Salsa',
                        description='chile habanero', price=29, stock=80)
    Product.new_product(store=2, name='Mostaza',
                        description='Mostaza', price=30.9, stock=80)


def insert_categories():
    Category.new(name='Liquidos', description='liquidos')
    Category.new(name='Embutidos', description='embutidos')
    Category.new(name='Snacks', description='snacks')
    Category.new(name='Aderezos', description='aderezos')
    Category.new(name='Carnes', description='carnes')


def insert_categories_products():
    CategoriesProducts.new(categorie=1, product=2)
    CategoriesProducts.new(categorie=1, product=5)
    CategoriesProducts.new(categorie=1, product=7)

    CategoriesProducts.new(categorie=2, product=3)

    CategoriesProducts.new(categorie=3, product=6)

    CategoriesProducts.new(categorie=4, product=4)
    CategoriesProducts.new(categorie=4, product=8)

    CategoriesProducts.new(categorie=5, product=3)


def create_schema():
    create_tables()
    create_users()
    create_stores()
    create_products()
    insert_categories()
    insert_categories_products()


if __name__ == "__main__":
    jamon = Product.select().where(Product.name == 'Leche').get()

    for categorie in jamon.categories:
        print(categorie)
