from flask import Blueprint, render_template, redirect, url_for, request, session, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
            session['user'] = request.form['user']
            session['API_KEY'] = request.form['API_KEY']
            return redirect(url_for("views.user", user=session['user']))
    
            # elif session.get("user",None) and session.get("symbol",None):
            #     session.permanent = True
            #     # message flash, redirect to main page
            #     session['user'] = request.form['user']
            #     session['API_KEY'] = request.form['API_KEY']
            #     return redirect(url_for("views.basics", user=session['user']))
        
    else:
        return render_template('login.html')
        

@auth.route('/logout')
def logout():
    if session.get("user",None):
        user = session["user"]
        flash(f"You have successfully logged out, {user}", "info")
    session.pop("user", None)
    session.pop("symbol", None)
    session.pop('API_KEY', None)
    return redirect(url_for("auth.login"))

