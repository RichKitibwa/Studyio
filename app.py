from flask import Flask, render_template, request, redirect, url_for, flash
from model import db, TutorialInfo
from os import environ
from database import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123@localhost/tutorials'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

from model import TutorialInfo


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        keyword = request.form['keyword']
        results = TutorialInfo.query.filter((TutorialInfo.title.like('%{}%'.format(keyword))) |
        (TutorialInfo.description.like('%{}%'.format(keyword)))).all()
        return render_template('results.html', keyword=keyword, results=results)
    return render_template('home.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Get form data and add new tutorial to database
        title = request.form['title']
        description = request.form['description']
        url = request.form['url']
        new_tutorial = TutorialInfo(title=title, description=description, url=url)
        db.session.add(new_tutorial)
        db.session.commit()

        flash('Tutorial added succesfully')
        # Redirect to home page
        return render_template('admin.html')
    # Render admin form template
    return render_template('admin.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    