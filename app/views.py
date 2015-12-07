from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Saul'} #fake user
	portfolio = [ #fake array of stocks in the user's portfolio
	{
		'symbol': 'AAPL'
		'name': 'Apple Inc'
		'qty': 100
	},
	{
		'symbol': 'MSFT'
		'name': 'Microsoft'
		'qty': 50
	},
	{
		'symbol': 'GOOGL'
		'name': 'Google'
		'qty': 200
	},
	
	]
	return render_template('index.html', title='Home',
							user = user,
							portfolio=portfolio)