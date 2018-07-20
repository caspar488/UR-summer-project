from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def index():
	# return"hi!"
	return render_template("index.html")

@app.route('/about')
def about():
	# return"hi!"
	return render_template("about.html")


@app.route('/contact')
def contact():
	# return"hi!"
	return render_template("contact.html")


@app.route('/info')
def info():
	# return"hi!"
	return render_template("info.html")


@app.route('/photogallery')
def photogallery():
	# return"hi!"
	return render_template("photo_gallery.html")



if __name__ == '__main__':
	app.run(debug=True)

