# Flask_Market
This repository is for recording the process of learning flask with a project Flask_Market in freecodecamp
-------------------------

To start a Flask program:
------------------------

"$env:FLASK_APP=app.py"

"$env:FLASK_DEBUG=1"

"python -m flask run"


to inherit
-----------------------
in the inherited class:

 {% block title %}
 
 {% endblock %}
 
 in the inheriting classes:
 
{% extends 'base.html' %}

{% block title %}

Home Page

{% endblock %}

---------------------
notes:the folder name 'templates'is default and unchangeable because flask get into the folder templates to search for the resources
---------------------------------------------------
in VScode everytime we need to add something to the database in the terminal we should type in the terminal like:

python -m flask shell (to get into the flask shell and add sth to the database there)

it will return like

Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
App: market
Instance: F:\Flask_Market\instance

then input:

from market import app,db  (the database object)

from market import Item  (the model)

db.create_all() 

item = Item(xxxxx)

db.session.add(item)

db.session.commit

Item.query.all() (to view the item added)

if we are not in the flask shell, 

RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.

will frequently appear

if the codes have been changed and wanting to see the new result in the terminal we should restart the flask shell then type the commands to see it

----------------------------

to iterate the Items in the databse:

type in the terminal(flask shell):

for item in Item.query.all():

...     item.name

...     item.price

...     item.description

...     item.id

then the result:

'IPhone10'

500

'desc'

1

'Laptop'

900

'description'

2

--------------

to filter(in the flask shell):

Item.query.filter_by(price) (price,name,id,barcode....)



![family-guy-griffin-on-toilet-bowl-zk2c0t05e080bs7t](https://github.com/user-attachments/assets/62d17591-a3d3-4753-b612-a8dfffad2289)
