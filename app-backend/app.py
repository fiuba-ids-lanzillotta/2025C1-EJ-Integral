from flask import Flask
from flask_cors import CORS
from routes.alumnos import alumnos_bp
from routes.materias import materias_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(alumnos_bp, url_prefix="/alumnos")
app.register_blueprint(materias_bp, url_prefix="/materias")


if __name__ == "__main__":
    app.run(debug=True)