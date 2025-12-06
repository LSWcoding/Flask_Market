__Cheatsheet:__

Features of Flask:

jinjia syntax:{%   %}


render_template,redirect,url_for,flash,request{.method,form.get()}

flask_sqlalchemy{SQLAlchemy}

flask_bcrypt{Bcrypt{.generate_password_hash(),bcrypt.check_password_hash(self.password_hash, attempted_password)}}

flask_login{

LoginManager
{.login_view __,__ .login_message_category0}

login_user ,

logout_user ,

login_required,

current_user

UserMixin
}

flask_wtf{Flaskform{errors.value()}}

wtfroms{StringField(label=,validators=),PasswordField(label=,validators=),SubmitField(lable=,validators=)}

wtforms.validators{Length(min=,max=),Datarequired=,Email(),EqualTo(),ValidationError}








