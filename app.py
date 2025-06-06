from flask import Flask
from routes.predict import predict_blueprint

app = Flask(__name__)
app.register_blueprint(predict_blueprint, url_prefix='/api')

@app.route('/')
def index():
    return "Student API Backend is Running"

if __name__ == '__main__':
    app.run(debug=True)
