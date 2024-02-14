from flask import Flask , render_template , jsonify 
app = Flask(__name__)

JOBS = [
{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Accra, Ghana',
    'Salary': '100,000,000'
},
{
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Tema, Ghana',
    'Salary': 'Remote'
},
{
    'id': 3,
    'title': 'Prompt Engineer',
    'location': 'Accra, Ghana',
    'Salary': '120,000,000'
},
{
    'id': 4,
    'title': 'AI Researcher',
    'location': 'Kumasi, Ghana',
    'Salary': '130,000,000'
},
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Tema')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
