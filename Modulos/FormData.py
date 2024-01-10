
from bs4 import BeautifulSoup


def form_data(email, passwd):
    
    return {
        "lsd": "",  # Valor específico, pode mudar com o tempo
        "jazoest": "",     # Valor específico, pode mudar com o tempo
        "m_ts": "",  # Valor específico, pode mudar com o tempo
        "li": "",  # Valor específico, pode mudar com o tempo
        "try_number": "",
        "unrecognized_tries": "",
        "email": f"{email}",
        "pass": f"{passwd}",
        "login": "Entrar",
        "bi_xrwh": 0,
    }


def params():
    return {
        'refsrc': 'deprecated',
        'lwv': '100',
        'refid': '8',
    }
