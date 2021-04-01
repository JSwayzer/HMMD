# Profissão: select distinct(cod_profissao) from faprocad
# select cod_categ,descricao,nome_conselho_regi,sigla_conselho_reg from mvcatcad order by descricao
def profissao(prof):
    if prof == "ADMINISTRATIVO":
        return "ADMN"

    elif prof == "ALMOXARIFE":
        return "ALMX"

    elif prof == "ASSISTENTE SOCIAL":
        return "ASSO"

    elif prof == "AUXILIAR DE ENFERMAGEM":
        return "AUXE"

    elif prof == "BIOMEDICO":
        return "BIME"

    elif prof == "BIOLOGO":
        return "BIOL"

    elif prof == "BIQUIMICO":
        return "BIOQ"

    elif prof == "EMPRESA":
        return "EMPR"

    elif prof == "ENFERMEIRO":
        return "ENFR"

    elif prof == "FARMACEUTICO":
        return "FARM"

    elif prof == "FINU":
        return "FISICO(NUCLEAR)"

    elif prof == "FISIOTERAPEUTA":
        return "FISI"

    elif prof == "FONOAUDIOLOGO":
        return "FONO"

    elif prof == "INSTRUMENTADOR":
        return "INST"

    elif prof == "MEDICO":
        return "MEDC"

    elif prof == "NUTRICIONISTA":
        return "NUTR"

    elif prof == "DENTISTA":
        return "ODON"

    elif prof == "PERFUSICIONISTA":
        return "PERF"

    elif prof == "PSICOLOGO":
        return "PSIC"

    elif prof == "TECNICO EM ANALISES CLINICAS":
        return "TEAC"

    elif prof == "TECNICO DE ENFERMAGEM":
        return "TECE"

    elif prof == "TECNICO DE GESSO":
        return "TECG"

    elif prof == "TECNICO DE HEMODIALISE":
        return "TECH"

    elif prof == "TECNICO DE RADIOLOGIA":
        return "TECR"

    elif prof == "TERAPEUTA OCUPACIONAL":
        return "TERA"


# Categoria: select * from mvcatcad
# select cod_categ,descricao,nome_conselho_regi,sigla_conselho_reg from mvcatcad order by descricao
# COD_CATEG,DESCRICAO,NOME_CONSELHO_REGI,SIGLA_CONSELHO_REG
def categoria(cat):
    if cat == "ADMINISTRATIVO":
        return "ADM"

    elif cat == "ASSISTENTE SOCIAL":
        return "ASS"

    elif cat == "AUXILIAR DE FARMACIA":
        return "AUXF"

    elif cat == "ENFERMAGEM":
        return "ENF"

    elif cat == "ENFERMEIRO OBSTETRA":
        return "ENO"

    elif cat == "FARMACEUTICO":
        return "CRF"

    elif cat == "FISIOTERAPEUTA":
        return "FIS"

    elif cat == "FONOAUDIOLOGA":
        return "FON"

    elif cat == "INFORMATICA":
        return "INF"

    elif cat == "LABORATORIO":
        return "LAB"

    elif cat == "MEDICO":
        return "MED"

    elif cat == "MEDICO INTERNO":
        return "MEDR"

    elif cat == "MEDICO PEDIATRA":
        return "MEDP"

    elif cat == "MEDICO PS":
        return "MED1"

    elif cat == "NUTRICIONISTA":
        return "NUT"

    elif cat == "PSICOLOGO":
        return "PSI"

    elif cat == "SCIH":
        return "SCIH"

    elif cat == "TECNICO DE ENFERMAGEM":
        return "TENF"

    elif cat == "TERAPEUTA OCUPACIONAL":
        return "TEO"


# Grupo: select * from fagprcad
# select cod_grupro,descricao from fagprcad order by descricao
# COD_GRUPRO,DESCRICAO
def grupomedico(gpm):
    if gpm == "AMBULATORIO DE ESPECIALIDADES":
        return "017"

    elif gpm == "ANALISES CLINICAS":
        return "010"

    elif gpm == "ANESTESIA":
        return "001"

    elif gpm == "ASSISTENCIA MEDICA AMBULATORIA ESPECIALIDADES":
        return "019"

    elif gpm == "ASSISTENCIA MEDICA AMBULATORIA":
        return "018"

    elif gpm == "CARDIOLOGIA":
        return "12"

    elif gpm == "CIRURGIA GERAL":
        return "2"

    elif gpm == "CIRURGIA PEDIATRICA":
        return "28"

    elif gpm == "CLINICA MEDICA":
        return "3"

    elif gpm == "COORD MEDICO DE LABORATORIO":
        return "16"

    elif gpm == "DIRETOR":
        return "31"

    elif gpm == "ENDOSCOPIA":
        return "9"

    elif gpm == "FISIOTERAPEUTA":
        return "FISI"

    elif gpm == "FONOAUDIOLOGO":
        return "FONO"

    elif gpm == "GINECOLOGIA/OBSTRETRICIA":
        return "4"

    elif gpm == "MEDICINA DO TRABALHO":
        return "15"

    elif gpm == "MEDICO RESIDENTE":
        return "30"

    elif gpm == "NEFROLOGIA":
        return "27"

    elif gpm == "NEONATOLOGIA":
        return "11"

    elif gpm == "NEUROLOGIA":
        return "29"

    elif gpm == "NUTROLOGIA":
        return "23"

    elif gpm == "ORTOPEDIA":
        return "6"

    elif gpm == "OTORRINOLARINGOLOGISTA":
        return "OTO"

    elif gpm == "PEDIATRIA":
        return "5"

    elif gpm == "PSIQUIATRIA":
        return "7"

    elif gpm == "RADIOLOGIA":
        return "8"

    elif gpm == "SUPERVISAO":
        return "14"

    elif gpm == "UNID BAS DE SAUDE ADM MON AZUL":
        return "22"

    elif gpm == "UNID BAS DE SAUDE ADM OS-CEJAM":
        return "21"

    elif gpm == "UNID DE APOIO E RETAG DE SAUDE":
        return "20"

    elif gpm == "UROLOGIA":
        return "24"

    elif gpm == "UTI":
        return "13"

    elif gpm == "VASCULAR":
        return "26"

    elif gpm == "VASECTOMIA":
        return "25"


# Categoria: select * from mvcatcad
# select cod_categ,descricao,nome_conselho_regi,sigla_conselho_reg from mvcatcad order by descricao
# COD_CATEG,DESCRICAO,NOME_CONSELHO_REGI,SIGLA_CONSELHO_REG
def tipoconselho(tcon):
    if tcon == "ADMINISTRATIVO":
        return ""

    elif tcon == "ASSISTENTE SOCIAL":
        return "CRESS"

    elif tcon == "AUXILIAR DE FARMACIA":
        return "AUXF"

    elif tcon == "ENFERMAGEM":
        return "COREN"

    elif tcon == "ENFERMEIRO OBSTETRA":
        return "COREN"

    elif tcon == "FARMACEUTICO":
        return "CRF"

    elif tcon == "FISIOTERAPEUTA":
        return "CREFITO"

    elif tcon == "FONOAUDIOLOGA":
        return "CRFA"

    elif tcon == "INFORMATICA":
        return "INF"

    elif tcon == "LABORATORIO":
        return "CRBM"

    elif tcon == "MEDICO":
        return "CRM"

    elif tcon == "MEDICO INTERNO":
        return "RG"

    elif tcon == "MEDICO PEDIATRA":
        return "CRM"

    elif tcon == "MEDICO PS":
        return "CRM"

    elif tcon == "NUTRICIONISTA":
        return "CRN"

    elif tcon == "PSICOLOGO":
        return "CRP"

    elif tcon == "SCIH":
        return ""

    elif tcon == "TECNICO DE ENFERMAGEM":
        return "COREN"

    elif tcon == "TERAPEUTA OCUPACIONAL":
        return "CREFITO"


# ESPECIALIDADES: select distinct(cod_esp) from faesppro
# select cod_esp, descricao from faespcad order by descricao
# COD_ESP	DESCRICAO
def especialidade(esp):
    if esp == "ACUPUNTURA":
        return "001"
    elif esp == "ALERGIA E IMUNOLOGIA":
        return "0030"
    elif esp == "ANATOMIA PATOLOGICA":
        return "0063"
    elif esp == "ANESTESIOLOGIA":
        return "002"
    elif esp == "ANESTESISTA UROLOGIA":
        return "0093"
    elif esp == "ANGIOLOGISTA":
        return "0031"
    elif esp == "BUCO MAXILO":
        return "0059"
    elif esp == "CANCEROLOGIA":
        return "003"
    elif esp == "CANCEROLOGIA/CIRURGICA":
        return "0032"
    elif esp == "CANCEROLOGIA/CLINICA":
        return "004"
    elif esp == "CANCEROLOGIA/PEDIATRICA":
        return "0033"
    elif esp == "CARDIOLOGIA":
        return "005"
    elif esp == "CIRURGIA CARDIOVASCULAR":
        return "0034"
    elif esp == "CIRURGIA DA MAO":
        return "006"
    elif esp == "CIRURGIA DE CABECA E PESCOCO":
        return "0035"
    elif esp == "CIRURGIA DO APARELHO DIGESTIVO":
        return "007"
    elif esp == "CIRURGIA GERAL":
        return "0036"
    elif esp == "CIRURGIA GINECOLOGIA":
        return "0073"
    elif esp == "CIRURGIA OFTALMOLOGIA":
        return "0072"
    elif esp == "CIRURGIA ORTOPEDIA":
        return "0070"
    elif esp == "CIRURGIA OTORRINO":
        return "0071"
    elif esp == "CIRURGIA PEDIATRICA":
        return "008"
    elif esp == "CIRURGIA PLASTICA":
        return "0037"
    elif esp == "CIRURGIA TORACICA":
        return "009"
    elif esp == "CIRURGIA UROLOGIA":
        return "0074"
    elif esp == "CIRURGIA VASCULAR":
        return "0038"
    elif esp == "CITOLOGIA":
        return "0060"
    elif esp == "CLINICA MEDICA":
        return "0010"
    elif esp == "COLOPROCTOLOGIA":
        return "0039"
    elif esp == "CUIDADOS PALIATIVOS":
        return "0091"
    elif esp == "DERMATOLOGIA":
        return "0011"
    elif esp == "DIAGNOSTICO POR IMAGEM":
        return "0012"
    elif esp == "DIAGNOSTICO POR IMAGEM":
        return "0040"
    elif esp == "ENDOCRINOLOGIA E METABOLOGIA":
        return "0041"
    elif esp == "ENDOSCOPIA":
        return "0013"
    elif esp == "ENFERMAGEM":
        return "0083"
    elif esp == "ENFERMAGEM ALEITAMENTO MATERNO":
        return "0082"
    elif esp == "ENFERMAGEM ESTOMATERAPEUTA":
        return "0076"
    elif esp == "ENFERMAGEM OBSTETRICA":
        return "0075"
    elif esp == "EXAME":
        return "0084"
    elif esp == "FISIOTERAPIA":
        return "0088"
    elif esp == "FISIOTERAPIA MOTORA":
        return "0078"
    elif esp == "FISIOTERAPIA RESPIRATORIA":
        return "0077"
    elif esp == "FONOAUDIOLOGIA":
        return "0079"
    elif esp == "GASTROENTEROLOGIA":
        return "0042"
    elif esp == "GENETICA MEDICA":
        return "0014"
    elif esp == "GERIATRIA":
        return "0043"
    elif esp == "GINECOLOGIA E OBSTETRICIA":
        return "0015"
    elif esp == "HANSENOLOGIA":
        return "0062"
    elif esp == "HEMATOLOGIA E HEMOTERAPIA":
        return "0044"
    elif esp == "HOMEOPATIA":
        return "0016"
    elif esp == "INFECTOLOGIA":
        return "0045"
    elif esp == "LABORATORIO":
        return "0086"
    elif esp == "MASTOLOGIA":
        return "0017"
    elif esp == "MEDICINA DE FAMILIA/COMUNIDADE":
        return "0046"
    elif esp == "MEDICINA DO TRABALHO":
        return "0018"
    elif esp == "MEDICINA DO TRAFEGO":
        return "0047"
    elif esp == "MEDICINA ESPORTIVA":
        return "0019"
    elif esp == "MEDICINA FISICA E REABILITACAO":
        return "0048"
    elif esp == "MEDICINA INTENSIVA":
        return "0020"
    elif esp == "MEDICINA LEGAL":
        return "0049"
    elif esp == "MEDICINA NUCLEAR":
        return "0021"
    elif esp == "MEDICINA PREVENTIVA E SOCIAL":
        return "0050"
    elif esp == "MEDICINA SANITARIA":
        return "0068"
    elif esp == "MELHOR EM CASA":
        return "PROH"
    elif esp == "MELHOR EM CASA":
        return "PROHD"
    elif esp == "NEFROLOGIA":
        return "0022"
    elif esp == "NEONATOLOGIA":
        return "0085"
    elif esp == "NEUROCIRURGIA":
        return "0051"
    elif esp == "NEUROLOGIA":
        return "0023"
    elif esp == "NEUROLOGIA PEDIATRICA":
        return "0069"
    elif esp == "NEUROLOGISTA PEDIATRA":
        return "0067"
    elif esp == "NUTRIÇÃO":
        return "0081"
    elif esp == "NUTROLOGIA":
        return "0052"
    elif esp == "OFTALMOLOGIA":
        return "0024"
    elif esp == "ONCOLOGIA CLINICA":
        return "0064"
    elif esp == "ORTOPEDIA E TRAUMATOLOGIA":
        return "0053"
    elif esp == "OTORRINOLARINGOLOGIA":
        return "0025"
    elif esp == "PATOLOGIA":
        return "0054"
    elif esp == "PATOLOGIA CLINICA/MEDICINAL":
        return "0026"
    elif esp == "PEDIATRIA":
        return "0055"
    elif esp == "PNEUMOLOGIA":
        return "0027"
    elif esp == "PRE OPERATORIO":
        return "0090"
    elif esp == "PROCTOLOGIA":
        return "0089"
    elif esp == "PRONTO SOCORRO":
        return "0087"
    elif esp == "PSICOLOGIA":
        return "0080"
    elif esp == "PSIQUIATRIA":
        return "0056"
    elif esp == "RADIOLOGIA E DIAGNOSTICO":
        return "0028"
    elif esp == "RADIOTERAPIA":
        return "0057"
    elif esp == "REUMATOLOGIA":
        return "0029"
    elif esp == "SERVICO SOCIAL":
        return "0092"
    elif esp == "SEXOLOGIA":
        return "0061"
    elif esp == "TERAPIA INTENSIVA":
        return "0065"
    elif esp == "TISIOLOGIA":
        return "0066"
    elif esp == "UROLOGIA":
        return "0058"
