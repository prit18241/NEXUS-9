from flask import Flask
app = Flask(__name__) 
@app.route("/")
def home():
    return {"message": "Welcome to the NEXUS-9 backend!"}

if __name__ == "__main__":
    app.run(debug=True)