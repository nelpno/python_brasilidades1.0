from validate_docbr import CNPJ


class Cnpj:
    def __init__(self, documento):
        if self.cnpj_e_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")

    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format_cnpj()
