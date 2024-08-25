class candidato:
    def __init__(self, nome, data_nasc, cor, genero, quimbola, estado_civil, grau_instituicao, 
                 nacionalidade, naturalidade, reeleicao, compo_coligacao, ocupacao, eleicoes_anteriores,
                bens, sites, candidatura, municipio, cnpj, num_voto, partido):
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__cor = cor
        self.__genero = genero
        self.__quimbola = quimbola
        self.__estado_civil = estado_civil
        self.__grau_instituicao = grau_instituicao
        self.__nacionalidade = nacionalidade
        self.__naturalidade = naturalidade
        self.__reeleicao = reeleicao
        self.__compo_coligacao = compo_coligacao
        self.__ocupacao = ocupacao
        self.__eleicoes_anteriores = eleicoes_anteriores
        self.__bens = bens
        self.__sites = sites
        self.__candidatura = candidatura
        self.__municipio = municipio
        self.__cnpj = cnpj
        self.__num_voto = num_voto
        self.__partido = partido
    
    def getNome(self):
        return self.__nome
    def setNome(self,nome):
        self.__nome = nome
    def getDataNasc(self):
        return self.__data_nasc
    def setDataNasc(self,data_nasc):
        self.__data_nasc = data_nasc
    def getCor(self):
        return self.__cor
    def setCor(self, cor):
        self.__cor = cor
    def getGenero(self):
        return self.__genero
    def setGenero(self, genero):
        self.__genero = genero
    def getQuimbola(self):
        return self.__quimbola
    def setQuimbola(self, quimbola):
        self.__quimbola = quimbola
    def getEstadoCivil(self):
        return self.__estado_civil
    def setEstadoCivil(self, estado_civil):
        self.__estado_civil = estado_civil
    def getGrauInstituicao(self):
        return self.__grau_instituicao
    def setGrauInstituicao(self, grau_instutuicao):
        self.__grau_instituicao = grau_instutuicao
    def getNacionalidade(self):
        return self.__nacionalidade
    def setNacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade
    def getNaturalidade(self):
        return self.__naturalidade
    def setNaturalidade(self, naturalidade):
        self.__naturalidade = naturalidade
    def getReeleicao(self):
        return self.__reeleicao
    def setReeleicao(self, reeleicao):
        self.__reeleicao = reeleicao
    def getCompoColigacao(self):
        return self.__compo_coligacao
    def setCompoColigacao(self, compo_coligacao):
        self.__compo_coligacao = compo_coligacao
    def getOcupacao(self):
        return self.__ocupacao
    def setOcupacao(self, ocupacao):
        self.__ocupacao = ocupacao

    def getEleicoesAnteriores(self):
        return self.__eleicoes_anteriores
    def setEleicoesAnteriores(self, eleicoes_anteriores):
        self.__eleicoes_anteriores = eleicoes_anteriores

    def getBens(self):
        return self.__bens
    def setBens(self, bens):
        self.__bens = bens
    
    def getSites(self):
        return self.__sites
    def setSites(self, sites):
        self.__sites = sites
    
    def getOcupacao(self):
        return self.__ocupacao
    def setOcupacao(self, ocupacao):
        self.__ocupacao = ocupacao
    
    def getCandidatura(self):
        return self.__candidatura
    def setCandidatura(self, candidatura):
        self.__candidatura = candidatura
    
    def getMunicipio(self):
        return self.__municipio
    def setMunicipio(self, municipio):
        self.__municipio = municipio

    def getCnpj(self):
        return self.__cnpj
    def setCnpj(self, cnpj):
        self.__cnpj = cnpj
    
    def getNumvoto(self):
        return self.__num_voto
    def setNumVoto(self, num_voto):
        self.__num_voto = num_voto
    
    def getPartido(self):
        return self.__partido
    def setPartido(self, partido):
        self.__partido = partido 