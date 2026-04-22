from flask import Flask
from database import init_db
from routes.lead_routes import lead_bp

app = Flask(__name__)

init_db()

app.register_blueprint(lead_bp)


@app.route("/")
def home():
    return {
    "status": "online",
    "message": "Lead Management API 🚀",
    "endpoints": {
        "GET /leads": "Listar leads",
        "GET /leads/{id}": "Buscar lead",
        "POST /leads": "Criar lead",
        "DELETE /leads/{id}": "Deletar lead"
    }
}

@app.errorhandler(500)
def internal_error(error):
    return {
        "error": "Erro interno no servidor"
    }, 500
    

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)