from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route('/passed/<int:score>')
def passed(score):
    return "Congrats!,you've passed and your marks is"+str(score)
@app.route('/failed/<int:score>')
def failed(score):
    return "oops!,you've failed and your marks is"+str(score)
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<35:
        result="failed"
    else:
        result="passed"
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True)
    