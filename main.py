import requests
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def root():
	res= ''
	country= request.args.get('country')
	resp = requests.get('http://restcountries.eu/rest/v2/name/'+country+'?fullText=true')
	if resp.status_code !=200:
	    res+= 'api error<br>'
	    return 'ERROR 400'
	else:
	  res+= ('Country Full Name: '+country+'<br>')
	  for item in resp.json():
	    res+= ('Country Full Capital: '+item['capital']+'<br>')
	    for j in item['languages']:
	       res+= ('Country Common Language: '+j['name']+'<br>')
	    for j in item['currencies']:
	       res+= ('Country Currency Name: '+j['name']+'<br>')
	       resp2=requests.get('http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols='+j['code'])
	       rate=resp2.json()
	       rates=rate['rates']
	       res+= ('Country Currency Rate: '+str(rates[j['code']])+'<br>')
	return res
app.run(host='0.0.0.0',debug=True)
