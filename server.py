import os
import csv
from flask import Flask, render_template, send_from_directory, request, redirect
app = Flask(__name__)
print(__name__)


@app.route('/')
# @app.route('/index.html')
def my_home():
    return render_template('index.html')


# This will dynamically handle all the below code
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        w_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, try again.'


def w_database(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def w_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writer.writerow([email,subject,message])


# @app.route('/')
# @app.route('/index.html')
# def my_home():
#     return render_template('index.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs'
#
#
# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'this is my dog'