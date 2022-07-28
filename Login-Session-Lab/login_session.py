from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/',methods=['POST','GET'] ) # What methods are needed?
def home():
	if request.method=="POST":
		i=0;
		names=[]
		quotes=[]
		ages=[]
		quotes.append(request.form['quote'])
		ages.append(request.form['age'])
		names.append(request.form['name'])
		try:
			login_session['name'] = names[0]
			login_session['age'] = ages[0]
			login_session['quote'] = quotes[0]
		
			if names[0]== "" or ages[0]==""or quotes[0]=="":
				return redirect(url_for('error'))
			else:
				return redirect(url_for('thanks'))
		except:
			return redirect(url_for('error'))
	return render_template('home.html')



@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():
	return render_template('display.html',name=login_session['name'],age=login_session['age'],quote=login_session['quote']  , len=len(login_session['name'])) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)