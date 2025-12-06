from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin

@login_manager.user_loader#to store the function load_user to login_manager and can be used as login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#after login this function store user,id to session
#everytime browser sends request to the page decorated by @login_required,this function is called to query User object and store to session
#then Flask-Login fetches user.id from session and then assign user.id to current_user
#current_user=user.holding on the login status

#to create Database model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)#primary_key=True:to define that id is unique,unrepeatable and increment automatically as soon as new User object created
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)#combine the model Item with User,backref makes it possible to find back User object by Item object,lazy = True define that only when user.items is called,items are queried and fetched

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"
    #12000->12,000,[:-3]:12.[-3:]:000

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
#hashed password is stored inside the models and password is outside and for user to input ,convert the former to the latter through @password.setter
    #                                                                                                                                def password(self, plain_text_password):


    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price
#preset the item_obj as Item object so that item_obj can use .price

    def can_sell(self, item_obj):
        return item_obj in self.items

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f'Item {self.name}'
    #to display the information of the items instead of the storage address

    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner = None
        user.budget += self.price
        db.session.commit()
