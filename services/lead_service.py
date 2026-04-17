from repositories.lead_repository import *


def list_leads():
    return get_all_leads()


def get_lead(lead_id):
    return get_lead_by_id(lead_id)


def create_new_lead(nome, email, interesse, valor):
    return create_lead(nome, email, interesse, valor)


def update_existing_lead(lead_id, nome, email, interesse, valor):
    return update_lead(lead_id, nome, email, interesse, valor)


def delete_existing_lead(lead_id):
    return delete_lead(lead_id)