from flask import Flask, render_template, request
from src.database import get_db_as_df
from src.api import get_nutirtion_info
import json
import pandas as pd

num = 0

app = Flask(__name__)
table_df = get_db_as_df("exercises7")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/photo-detail')
def photo_detail():
    return render_template('photo-detail.html')

@app.route('/photos')
def photos():
    global num
    num += 1
    return render_template('photos.html',photos_count = num, exercises=["static\images\img-06.jpg", "static\images\img-05.jpg", "static\images\img-04.jpg", "static\images\img-03.jpg", "static\images\img-02.jpg"])


@app.route('/try/<param>')
def photo(param):
    """
    :param param: goes with the url and passes the exercise
    :return: should find the data on the passed exercise and passing the data to the html file
    """
    ex_title = param
    explanation = param
    photo_img = "static\images\home.jpg"

    return render_template('try.html', title=ex_title, img=photo_img, text=explanation)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/trainer')
def trainer():
    return render_template('trainer.html')

@app.route('/all exercises')
def all_ex():
    return render_template('all_ex.html')

@app.route('/list exercises/<chosen_bodypart>')
def exercises_list(chosen_bodypart):
    if chosen_bodypart == "all":
        exercises = table_df
    else:
        exercises = table_df[table_df['bodyPart'] == chosen_bodypart]
    return render_template('exercises_list.html', chosen_bodypart=chosen_bodypart, exercises = exercises)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/favorites exercises')
def favorites():
    return render_template('favorites.html')

@app.route('/nutrition', methods=['GET', 'POST'])
def nutrition():
    desc = None
    if request.method == 'POST':
        # Get the value from the form
        input_value = request.form.get('user_input').replace(",", " ")
        desc = get_nutirtion_info(input_value)[1:-1].split('},')
        desc = [i+'}' if not i.endswith("}") else i for i in desc]
        desc = [json.loads(i) for i in desc]

    return render_template('nutrition.html', descs = desc)

if __name__ == '__main__':
    app.run(debug=True)
