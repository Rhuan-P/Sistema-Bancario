import re
from datetime import datetime


def validar_doc(doc):
    # Validação simplificada de CPF/CNPJ (apenas como exemplo)
    return bool(re.match(r"^\d{11}$", doc)) or bool(re.match(r"^\d{14}$", doc))


def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False
