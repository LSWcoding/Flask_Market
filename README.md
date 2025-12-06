# Flask_Market
This repository is for recording the process of learning flask with a project Flask_Market in freecodecamp
-------------------------
__How the project looks like__

<img width="1920" height="867" alt="home" src="https://github.com/user-attachments/assets/98d8a4c0-ba4a-4307-a060-f91ea427bbcd" />
<img width="1920" height="867" alt="loggin" src="https://github.com/user-attachments/assets/3d9756ef-149e-4964-be93-7f209b94318c" />
<img width="1897" height="877" alt="register" src="https://github.com/user-attachments/assets/a5c0e541-5a29-4643-aedc-d587fcd06ece" />
<img width="1920" height="855" alt="home_entered" src="https://github.com/user-attachments/assets/c6c1ac2a-e4f3-4da2-ace8-ca6ac077c22d" />
<img width="1920" height="877" alt="more_information" src="https://github.com/user-attachments/assets/e65d6e80-35d5-4086-acf7-5a87adbb910e" />
<img width="1920" height="870" alt="purchase" src="https://github.com/user-attachments/assets/9127d736-abe6-436a-9725-aefb73b10820" />
<img width="1917" height="856" alt="purchased" src="https://github.com/user-attachments/assets/8d89f9c3-1d0c-4652-92f8-58ce150a175d" />
<img width="1917" height="868" alt="sell" src="https://github.com/user-attachments/assets/0db0d21d-4b05-4e03-82f8-d910f5196a46" />
<img width="1920" height="848" alt="sold" src="https://github.com/user-attachments/assets/bc79343b-f6e5-4659-aff8-f59312768ef3" />

_______________

____Commands in the terminal____
_____________________________

__To import dependencies:__

pip install:

flask

sqlalchemy

flask_wtf

flask_bcrypt

flask_login

wrforms

wtforms.validators

__To start the project:__

$env:FLASK_APP="run.py"

"$env:FLASK_DEBUG=1"

python run (+tab to be like :python /.run.py)

__To manipulate database:__

$env:FLASK_APP="run.py"

python -m flask shell (to enter the shell and operate in the shell)

from market import db

from market.models import Item,User (must be market.models and not market because python imports sth from __ init __.py by default)

db.create_all()

item1 = Item(name="Macbook",price=900,barcode='123456789123',description="test",owner=None) (for example)

db.session.add(item1)

db.session.commit()

Item.query.all() (inspect the items in database)

__To inspect the items in database and show out the information of the items by iteration in the terminal (for example):__

for item in Item.query.all():

... item.name

... item.price

... item.description

... item.id

__To filter in the terminal:__

Item.query.filter_by(price) (price,name,id,barcode....)
To filter in the terminal:

Item.query.filter_by(price) (price,name,id,barcode....)
________________________________________________________
