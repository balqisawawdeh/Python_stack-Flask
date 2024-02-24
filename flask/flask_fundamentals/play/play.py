from flask import Flask , render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route("/play/<int:x>/")
def play(x):
  return render_template("index.html", box="hello", times=x)
@app.route("/play/<int:x>/<string:color>")
def play_color(x,color):
  return render_template("index.html", color=color, times=x)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


