import sqlalchemy.orm
import sqlalchemy.ext.declarative
import random

Base = sqlalchemy.ext.declarative.declarative_base()


class Manufacturer(Base):
    __tablename__ = 'Manufacturers'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    products_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Products.manufacturer_id'))
    products = sqlalchemy.orm.relationship("Product", backref="products")

    def __repr__(self):
        return f"Manufacturers: {self.id} -- {self.name} -- {self.products_id}"


class Customer(Base):
    __tablename__ = 'Customers'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    shopping_basket = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('Products.id'))

    def __repr__(self):
        return f"Customers: {self.id} -- {self.name} -- {self.shopping_basket}"


class Product(Base):
    __tablename__ = 'Products'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    manufacturer_id = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)

    # manufacturer_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Manufacturers.id'))
    # manufacturer = sqlalchemy.orm.relationship("Manufacturer", backref="manufacturer")

    def __repr__(self):
        return f"Products: {self.id} -- {self.name} -- {self.price}"


if __name__ == '__main__':
    engine = sqlalchemy.create_engine('sqlite:///t3.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    for i in range(1, 100):
        some_product = Product(id=i,
                               manufacturer_id=random.randint(1, 10),
                               name=f'product_{i}',
                               price=random.randint(1, 100))
        session.add(some_product)

    for i in range(1, 10):
        man = Manufacturer(id=i,
                           name=f'Manufacturer_{i}',
                           products_id=f'{i}')
        session.add(man)

    for i in range(1, 50):
        pur = Customer(id=i,
                       name=f'Customer_{random.randint(10, 50)}',
                       shopping_basket=f'{random.randint(1, 100)}')
        session.add(pur)
    session.commit()
