# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request, redirect
from jinja2  import TemplateNotFound

# App modules
from apps import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    try:
        # Detect the current page
        segment = get_segment( request )
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template( 'pages/' + path, segment=segment )
    except TemplateNotFound:
        return render_template('pages/index.html'), 404

@app.route('/typography')
def typography():
    return render_template('pages/typography.html')

@app.route('/color')
def color():
    return render_template('pages/color.html')

@app.route('/icon-tabler')
def icon_tabler():
    return render_template('pages/icon-tabler.html')

@app.route('/sample-page')
def sample_page():
    return render_template('pages/sample-page.html')  

# Auth pages
@app.route('/accounts/login/')
def login():
    return render_template('accounts/login.html') 

@app.route('/accounts/logout/')
def logout():
    return redirect('/accounts/login/')

@app.route('/accounts/register/')
def register():
    return render_template('accounts/register.html')


@app.route('/accounts/password-reset/')
def password_reset():
    return render_template('accounts/password_reset.html')

@app.route('/accounts/password-reset-done/')
def password_reset_done():
    return render_template('accounts/password_reset_done.html')

@app.route('/accounts/password-reset-confirm/')
def password_reset_confirm():
    return render_template('accounts/password_reset_confirm.html')

@app.route('/accounts/password-reset-complete/')
def password_reset_complete():
    return render_template('accounts/password_reset_complete.html')
    

@app.route('/accounts/password-change/')
def password_change():
    return render_template('accounts/password_change.html')

@app.route('/accounts/password-change-done/')
def password_change_done():
    return render_template('accounts/password_change_done.html')



def get_segment( request ): 
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment    
    except:
        return None  

