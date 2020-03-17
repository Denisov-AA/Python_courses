import sqlalchemy.orm
import sqlalchemy.ext.declarative
import sqlalchemy.sql
from Task_2 import Manufacturer, Customer, Product

Base = sqlalchemy.ext.declarative.declarative_base()
engine = sqlalchemy.create_engine('sqlite:///t3.db', echo=True)
Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# for Customer, Product in session.query(Customer.name, Product.name) \
#         .join(Product, Customer.shopping_basket == Product.id):
#     print(Customer + ' bought a ' + Product)

for Manufacturer, Product in session.query(Manufacturer.id, Product.price).filter(Product.price < 10):
    print(Manufacturer, Product)
