from flask import Blueprint, request, jsonify
from services.lead_service import *
from utils.validators import validate_lead_data
from utils.logger import logger

lead_bp = Blueprint("leads", __name__)


@lead_bp.route("/leads", methods=["GET"])
def get_leads():
    leads = list_leads()

    result = []
    for lead in leads:
        result.append(dict(lead))

    return jsonify(result), 200


@lead_bp.route("/leads/<int:lead_id>", methods=["GET"])
def get_lead_by_id_route(lead_id):
    lead = get_lead(lead_id)

    if not lead:
        return jsonify({"error": "Lead não encontrado"}), 404

    return jsonify(dict(lead)), 200


@lead_bp.route("/leads", methods=["POST"])
def create_lead_route():
    data = request.get_json()
    logger.info(f"Criando lead: {email}")
    nome = data.get("nome")
    email = data.get("email")
    interesse = data.get("interesse")
    valor = data.get("valor")

    error = validate_lead_data(data)

    if error:
     return jsonify({"error": error}), 400
  
    lead_id = create_new_lead(nome, email, interesse, valor)

    return jsonify({
        "message": "Lead criado",
        "id": lead_id
    }), 201
    
@lead_bp.route("/leads/<int:lead_id>", methods=["DELETE"])
def delete_lead_route(lead_id):
    lead = get_lead(lead_id)

    if not lead:
        return jsonify({"error": "Lead não encontrado"}), 404

    delete_existing_lead(lead_id)

    logger.info(f"Lead deletado: {lead_id}")

    return jsonify({
        "message": "Lead deletado com sucesso"
    }), 200    