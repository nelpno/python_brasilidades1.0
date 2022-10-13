import re

from telefones_br import TelefonesBr

telefone = "551633360949"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

# padrao = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
# resposta = re.search(padrao,telefone)
# print(resposta.group())