from flask import Flask
#Flask constructor takes the__name__of current module as an argument
app=Flask(__name__)
@app.route('/')
def welcome():
	return "Hello folks,welcome back to the class!"
@app.route('/sub/<name>')

def sub(name):
	return 'this is %s' %name
if __name__=="__main__":
    app.run(debug=True)	
