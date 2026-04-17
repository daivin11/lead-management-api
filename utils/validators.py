import re


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


def validate_lead_data(data):
    nome = data.get("nome")
    email = data.get("email")

    if not nome or not email:
        return "Nome e email são obrigatórios"

    if not validate_email(email):
        return "Email inválido"

    return None