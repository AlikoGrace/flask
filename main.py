from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = "PASS" if score >= 50 else "FAIL"
    exp = {'score': score, 'res': res}
    return render_template('result.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The student failed ' + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = 'fail' if marks < 50 else 'success'
    return redirect(url_for(result, score=marks))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4
    
    res = 'fail' if total_score < 50 else 'success'
    return redirect(url_for(res, score=int(total_score)))

if __name__ == '__main__':
    app.run(debug=True)
