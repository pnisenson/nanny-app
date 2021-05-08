#from flask import Flask, render_template, redirect, jsonify
from flask import Flask, render_template, redirect, request
import os

# Create an instance of Flask
app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
	return redirect("/index.html")

@app.route("/index.html", methods=['GET', 'POST'])
def main():
	#Return template and data
	errors= []
	if request.method == "POST":
		try:
			print("Hi")
			print(request.form)
			print(request.form['lunch'])
			if os.path.exists("nannyinfo.py"):
				os.remove("nannyinfo.py")
			File_object = open(r"nannyinfo.py","a")
			File_object.write(f"Wake Up Time is: '{str(request.form['wakeUp'])}' \n")
			File_object.write(f"First Nap should be at '{str(request.form['firstNap'])}' \n")
			File_object.write(f"For lunch today, we have '{request.form['lunch']}' \n")
			File_object.write(f"For dinner today, we have '{request.form['snack']}' \n")
			File_object.write(f"As a reminder '{request.form['reminder']}' \n")
			results = 1
			return render_template("index.html", results=results)
		except:
			errors.append("Form not complete. Please make sure it's valid and try again.")
			return render_template('index.html', errors=errors)
	return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
