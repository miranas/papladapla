from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
	user={'username':'Nakoma'}
	posts= [
	{
		'author':{'username':'John'},
		'body':'Beutifull day in Portland'
	},
	{
		'author':{'username':'Susan'},
		'body':'Olemajole'		
	},
	{
		'author':{'username':'Zundkvist Korgolski'},
		'body':'Hehetanje med koruznimi storži'
	},
	{
		'author':{'username':'Vitlof Strahunc'},
		'body':'Ne boš ti meni hlodovine žagal'
	}
	]
	return render_template('index.html',title='Home',user=user,posts=posts) 
	
@app.route('/papla')
def index2():
	return 'Papladapla'
	





