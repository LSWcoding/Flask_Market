Dependencies
--------------
pip install:

flask

sqlalchemy

flask_wtf

flask_bcrypt

flask_login

wrforms

wtforms.validators

-------------------
in __ __init__ __.py :

to create app 

initialize extends like db ,bcrypt,login_manager

load models

set up configurations

making the constructure clear

from market(the current directory) import xxx means from __ int __ import
_______
in routes, def market_page:

purchase_item = request.form.get("purchased_item") it works like:

a tag:

<input type"hidden" name"purchased_item" value="Macbook">

submitt the tag by POST and the server receive purchased_item = Macbook

then

purchased_item =="Macbook"


