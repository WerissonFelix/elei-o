from candidato import candidato

class prefeito:
    def __init__(self, nome, data_nasc, cor, genero, quimbola, estado_civil, grau_instituicao, 
                 nacionalidade, naturalidade, reeleicao, compo_coligacao, ocupacao, eleicoes_anteriores,
                bens, sites, candidatura, municipio, cnpj, num_voto, partido, coligacao,etnia_indigena, prefeito):
        candidato.__init__(self, nome, data_nasc, cor, genero, quimbola, estado_civil, grau_instituicao, 
                 nacionalidade, naturalidade, reeleicao, compo_coligacao, ocupacao, eleicoes_anteriores,
                bens, sites, candidatura, municipio, cnpj, num_voto, partido)
        self.__coligacao = coligacao
        self.__etnia_indigena = etnia_indigena
        self.__prefeito = prefeito

    def getColigacao(self):
        return self.__coligacao
    def setColigacao(self, coligacao):
        self.__coligacao = coligacao

    def getEtnia_indigena(self):
        return self.__etnia_indigena
    def setEtnia_indigena(self, etnia_indigena):
        self.__etnia_indigena = etnia_indigena

    
    def getPrefeito(self):
        return self.__vice_prefeito
    def setPrefeito(self, prefeito):
        self.__vice_prefeito = prefeito