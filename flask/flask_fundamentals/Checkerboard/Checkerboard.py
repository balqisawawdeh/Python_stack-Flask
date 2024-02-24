from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', column = 8, row = 8)

@app.route('/<count>')
def col_row(count):
    return render_template('index.html', column = 8, row = int(count))

@app.route('/<count1>/<count2>')
def count_col_row(count1,count2):
    return render_template('index.html', column = int(count1), row = int(count2) )

@app.route('/<count1>/<count2>/<col1>/<col2>')
def all_call(count1, count2, col1, col2):
    return render_template('index.html', column = int(count1), row = int(count2), col1= col1, col2 = col2)
if __name__ == "__main__":
    app.run(debug=True)