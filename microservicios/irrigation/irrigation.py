from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Microservicio de autenticación funcionando."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
