import re
from validate_docbr import CPF


def nome_invalido(nome):
    return len(nome) < 3 or not all(char.isalpha() or char.isspace() for char in nome)


# def validate_nome(, nome):
#     if not nome.replace(" ", "").isalpha():
#         raise serializers.ValidationError("O nome só pode conter letras e espaços")
#     if len(nome) < 3:
#         raise serializers.ValidationError("O nome deve ter no mínimo 3 caracteres")
#     return nome


def cpf_invalido(numero_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido


def email_invalido(email):
    return "@" not in email or "." not in email.split("@")[-1]


# def validate_email(email):
#     if "@" not in email or "." not in email.split("@")[-1]:
#         raise serializers.ValidationError("O email deve ser válido")
#     return email


def telefone_invalido(telefone):
    # return len(telefone) != 10 or not telefone.isdigit()
    modelo = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    response = re.findall(modelo, telefone)
    return not response


# def validate_telefone(telefone):
#     if len(telefone) < 10 or not telefone.isdigit():
#         raise serializers.ValidationError(
#             "O telefone deve ser somente números e ter pelo menos 10 dígitos"
#         )
#     return telefone
