from candidato import candidato

class prefeito:
    def __init__(self, nome, data_nasc, cor, genero, quimbola, estado_civil, grau_instituicao, 
                 nacionalidade, naturalidade, reeleicao, compo_coligacao, ocupacao, eleicoes_anteriores,
                bens, sites, candidatura, municipio, cnpj, num_voto, partido, coligacao, limit_gastos, vice_prefeito, propostas):
        candidato.__init__(self, nome, data_nasc, cor, genero, quimbola, estado_civil, grau_instituicao, 
                 nacionalidade, naturalidade, reeleicao, compo_coligacao, ocupacao, eleicoes_anteriores,
                bens, sites, candidatura, municipio, cnpj, num_voto, partido)
        self.__coligacao = coligacao
        self.__limit_gastos = limit_gastos
        self.__vice_prefeito = vice_prefeito
        self.__propostas = propostas

    def getColigacao(self):
        return self.__coligacao
    def setColigacao(self, coligacao):
        self.__coligacao = coligacao

    def getLimitGastos(self):
        return self.__limit_gastos
    def setLimitGastos(self, limit_gastos):
        self.__limit_gastos =  limit_gastos
    
    def getVicePrefeito(self):
        return self.__vice_prefeito
    def setVicePrefeito(self, vice_prefeito):
        self.__vice_prefeito = vice_prefeito

    
    def getPropostas(self):
        return self.__propostas
    def setPropostas(self, propostas):
        self.__propostas = propostas