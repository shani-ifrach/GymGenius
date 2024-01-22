from flask import Flask, render_template, request, jsonify
from src.database import get_db_as_df
from src.api import get_nutirtion_info
import json
from hdfs.hdfs_funcs import update_csv_file

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
    else:
        exercises = table_df[table_df['bodyPart'] == chosen_bodypart]
    return render_template('exercises_list.html', chosen_bodypart=chosen_bodypart, exercises = exercises)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/call_update_csv", methods=["POST"])
def call_update_csv():
    data_received = request.get_json()
    param = data_received.get('param', '')

    # Call the Python function with the parameter
    result = update_csv_file(int(param))

    return jsonify({'result': result})

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
