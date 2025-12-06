Cheatsheet
--------------------------------

__Features of Flask__

____________________________________
jinjia syntax:{%   %}

__to inherit__

in the inherited class:

 {% block title %}
 
 {% endblock %}
 
 in the inheriting classes:
 
{% extends 'base.html' %}

{% block title %}

Home Page

{% endblock %}

__if:__

{% if conditions %}

xxxxxxxxxxxxxxx

{% else %}

xxxxxxxxxxxx

{% end if %}

__for loop:__

 {% for item in items %}
 {% include 'includes/items_modals.html' %}
    <tr>
               
    <td>{{ item.id }}</td>
               
    <td>{{ item.name }}</td>
               
    <td>{{ item.barcode }}</td>
               
    <td>{{ item.price }}$</td>
              
    </tr>
            
{% endfor %}

____________________________________________


render_template,redirect,url_for,flash,request{.method,form.get()}

flask_sqlalchemy{SQLAlchemy}

flask_bcrypt{Bcrypt{.generate_password_hash(),bcrypt.check_password_hash(self.password_hash, attempted_password)}}

flask_login{

LoginManager
{.login_view __,__ .login_message_category}

login_user 


logout_user 


login_required


current_user


UserMixin

}

flask_wtf{Flaskform{errors.value()}}

__Other Features__

______________________________

wtfroms{

StringField(label=,validators=)

PasswordField(label=,validators=)

SubmitField(lable=,validators=)

}

wtforms.validators{

Length(min=,max=)

Datarequired=Email()

EqualTo()

ValidationError

}








