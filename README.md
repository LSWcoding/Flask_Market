____________
__Error__

PS F:\codemarket> python -m flask shell
Usage: python -m flask shell [OPTIONS]
Try 'python -m flask shell --help' for help.

Error: Could not locate a Flask application. Use the 'flask --app' option, 'FLASK_APP' environment variable, or a 'wsgi.py' or 'app.py' file in the current directory.

__Solution__

type in terminal:
$env:FLASK_APP="run.py"
_________________________
__Commands__

to add sth to database:

$env:FLASK_APP:"run.py"

python -m flask shell #to enter the shell to manipulate database

from market import db

from market.models import Item,User #must be market.models and not market because python imports sth from __ init __.py by default

db.create_all()

item1 = Item(name="Macbook",price=900,barcode='123456789123',description="test",owner=None) #for example

db.session.add(item1)

db.session.commit()

Item.query.all() #inspect the items in database
 
