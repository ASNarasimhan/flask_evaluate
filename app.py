import uuid, json, csv, os.path
from flask import Flask, render_template, request, url_for, flash, redirect, session, make_response
from werkzeug.exceptions import abort
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/home', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':

        print('post')

        if "node_relavence" in request.form:

            json_id = session['json_id']
            dict_data = session['dict_data']
            dict_data.pop(json_id, None)
            session['dict_data'] = dict_data

            header = ['unique_user_id', 'json_key', 'node_relavence', 'edge_relavence', 'completeness', 'accuracy']

            if not os.path.exists("static/output/user_rating.csv"):
                new_file = True
            else:
                new_file = False


            session_id = session['session_id']
            node_relavence = request.form['node_relavence']
            edge_relavence = request.form['edge_relavence']
            completeness = request.form['completeness']
            accuracy = request.form['accuracy']

            data = []
            data.append(session_id)
            data.append(json_id)
            data.append(node_relavence)
            data.append(edge_relavence)
            data.append(completeness)
            data.append(accuracy)

            with open('static/output/user_rating.csv', 'a', encoding='UTF8', newline='') as f:

                writer = csv.writer(f)

                if new_file:
                    writer.writerow(header)

                # write the data
                writer.writerow(data)

        dict_data = get_random_question()
        session['dict_data'] = dict_data

        return render_template('main.html', dict_data=dict_data)
        
    if ('session_id') in session:
        session_id = session['session_id']
    else:
        session_id=uuid.uuid4()
        session['session_id'] = session_id
        with open('static/TPAMI2022_Viz/OBQA_vizSentences.json') as fp:
            json_data = json.load(fp)
            session['json_data'] = json_data
    return render_template('home.html', session_id=session_id)

def get_random_question():
    json_data = session['json_data']
    while True:
        random_index = randint(0, len(json_data)-1)
        dict_data = [value for value in json_data.values()][random_index]
        if dict_data['imgPath']:
            session['json_id'] = [key for key in json_data.keys()][random_index]
            return dict([value for value in json_data.values()][random_index])
            break

if __name__ == "__main__":
    app.run()