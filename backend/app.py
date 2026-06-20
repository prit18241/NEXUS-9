from flask import Flask
from routes.cve import cve_bp

app = Flask(__name__) 
app.register_blueprint(cve_bp)

@app.route("/")
def home():
    return {"message": "Welcome to the NEXUS-9 backend!"}

if __name__ == "__main__":
    app.run(debug=True)