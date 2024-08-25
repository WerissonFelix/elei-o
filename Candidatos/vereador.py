from candidato import candidato

class vereador:
    def __init__(self, nome, data_nasc, cor, genero, quimbola, estado_civil, grau_instituicao, 
                 nacionalidade, naturalidade, reeleicao, compo_coligacao, ocupacao, eleicoes_anteriores,
                bens, sites, candidatura, municipio, cnpj, num_voto, partido, partido_isolado, etnia_indigena, limit_gastos):
        candidato.__init__(self, nome, data_nasc, cor, genero, quimbola, estado_civil, grau_instituicao, 
                 nacionalidade, naturalidade, reeleicao, compo_coligacao, ocupacao, eleicoes_anteriores,
                bens, sites, candidatura, municipio, cnpj, num_voto, partido)
        self.__partido_isolado = partido_isolado
        self.__etnia_indigena = etnia_indigena
        self.__limit_gastos = limit_gastos
    
    def getPartido_isolado(self):
        return self.__partido_isolado
    def setPartido_isolado(self, partido_isolado):
        self.__partido_isolado = partido_isolado
    
    
    def getEtnia_indigena(self):
        return self.__etnia_indigena
    def setEtnia_indigena(self, etnia_indigena):
        self.__etnia_indigena = etnia_indigena

    def getLimitGastos(self):
        return self.__limit_gastos
    def setLimitGastos(self, limit_gastos):
        self.__limit_gastos = limit_gastos