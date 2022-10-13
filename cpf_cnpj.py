from validate_docbr import CPF
from validate_docbr import CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")


class DocCpf:
    def __init__(self, documento):
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def cpf_e_valido(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()


class DocCnpj:
    def __init__(self, documento):
        if self.cnpj_e_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")

    def cnpj_e_valido(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format_cnpj()
