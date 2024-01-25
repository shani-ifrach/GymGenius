from flask import Flask, render_template, request, jsonify
from src.database import get_db_as_df
from src.api import get_nutrition_info
import json
from aws_utils.dynamo_db_funcs import insert_event_to_dynamodb
from datetime import datetime
from aws_utils.dynamo_db_funcs import get_favorites

app = Flask(__name__)
table_df = get_db_as_df("exercises")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/all exercises')
def all_ex():
    return render_template('all_ex.html')

@app.route('/list exercises/<chosen_bodypart>')
def exercises_list(chosen_bodypart):
    if chosen_bodypart == "all":
        exercises = table_df
    elif chosen_bodypart == 'favorites':
        favs = get_favorites()
        if favs is None:
            favs = []
        exercises = table_df[table_df["id"].isin(tuple(favs))]
    else:
        exercises = table_df[table_df['bodyPart'] == chosen_bodypart]
    return render_template('exercises_list.html', chosen_bodypart=chosen_bodypart, exercises = exercises)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/call_insert_event_to_dynamodb", methods=["POST"])
def call_insert_event_to_dynamodb():
    data_received = request.get_json()
    param = data_received.get('param', '')
    print(param)
    # Call the Python function with the parameter
    result = insert_event_to_dynamodb({'id': int(param), 'event_time': str(datetime.now())})
    print(result)

    return jsonify({'result':result})


@app.route('/nutrition', methods=['GET', 'POST'])
def nutrition():
    desc = None
    if request.method == 'POST':
        # Get the value from the form
        input_value = request.form.get('user_input').replace(",", " ")
        desc = get_nutrition_info(input_value)[1:-1].split('},')
        desc = [i+'}' if not i.endswith("}") else i for i in desc]
        desc = [json.loads(i) for i in desc]

    return render_template('nutrition.html', descs = desc)

if __name__ == '__main__':
    app.run(debug=True)
