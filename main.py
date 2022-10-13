from cpf_cnpj import Documento

exemplo_cpf = "23058073844"
exemplo_cnpj = "00494317000121"


cpf_novo = Documento.cria_documento(exemplo_cpf)
print(cpf_novo)
cnpj_novo = Documento.cria_documento(exemplo_cnpj)
print(cnpj_novo)

