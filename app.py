from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Flask is frábært...</h1><a href="/sida1">Síða 1|</a><a href="/sida2">http spurningar</a>'

@app.route('/sida1')
def sida1():
	return'<h1>Síða 1, nú er gaman...<h1>'

@app.route('/sida2')
def sida2():
	return render_template("http.html")

if __name__ == "__main__":
	app.run(debug=True)
