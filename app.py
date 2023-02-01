from flask import Flask

@app.route("/")
def home():
   return "Hello World!"

@app.route('/add', methods = ["POST"])
def add():
  command = request.form['post']
  return redirect(url_for("home", command = command))

# To run
#sudo ./app.py

# For the RPI
#app.run(host='0.0.0.0', port=80, debug=True)
 
# For testing on a normal Pc
app.run(debug=True)