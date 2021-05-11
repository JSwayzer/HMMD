import re


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        print("Profissão: ")
        return result.group()


# Profissão: select distinct(cod_profissao) from faprocad
# select cod_categ,descricao,nome_conselho_regi,sigla_conselho_reg from mvcatcad order by descricao
def profissao(prof):
    if pro(prof, "MEDICO") == "MEDICO":
        return "MEDC"

    elif pro(prof, "AUXILIAR DE ENFERMAGEM") == "AUXILIAR DE ENFERMAGEM" \
            or pro(prof, "AUXILIAR DE FARMACIA") == "AUXILIAR DE FARMACIA":
        return "AUXE"

    elif pro(prof, "TECNICO DE ENFERMAGEM") == "TECNICO DE ENFERMAGEM":
        return "TECE"

    elif pro(prof, "ENFERMEIRO") == "ENFERMEIRO":
        return "ENFR"

    elif pro(prof, "ADMINISTRATIVO") == "ADMINISTRATIVO":
        return "ADMN"

    elif pro(prof, "ALMOXARIFE") == "ALMOXARIFE":
        return "ALMX"

    elif pro(prof, "ASSISTENTE SOCIAL") == "ASSISTENTE SOCIAL":
        return "ASSO"

    elif pro(prof, "BIOMEDICO") == "BIOMEDICO":
        return "BIME"

    elif pro(prof, "BIOLOGO") == "BIOLOGO":
        return "BIOL"

    elif pro(prof, "BIQUIMICO") == "BIQUIMICO":
        return "BIOQ"

    elif pro(prof, "EMPRESA") == "EMPRESA":
        return "EMPR"

    elif pro(prof, "FARMACEUTICO") == "FARMACEUTICO":
        return "FARM"

    elif pro(prof, "FISICO(NUCLEAR)") == "FISICO(NUCLEAR)":
        return "FINU"

    elif pro(prof, "FISIOTERAPEUTA") == "FISIOTERAPEUTA":
        return "FISI"

    elif pro(prof, "FONOAUDIOLOGO") == "FONOAUDIOLOGO":
        return "FONO"

    elif pro(prof, "INSTRUMENTADOR") == "INSTRUMENTADOR":
        return "INST"

    elif pro(prof, "NUTRICIONISTA") == "NUTRICIONISTA":
        return "NUTR"

    elif pro(prof, "DENTISTA") == "DENTISTA":
        return "ODON"

    elif pro(prof, "PERFUSICIONISTA") == "PERFUSICIONISTA":
        return "PERF"

    elif pro(prof, "PSICOLOGO") == "PSICOLOGO":
        return "PSIC"

    elif pro(prof, "TECNICO EM ANALISES CLINICAS") == "TECNICO EM ANALISES CLINICAS":
        return "TEAC"

    elif pro(prof, "TECNICO DE GESSO") == "TECNICO DE GESSO":
        return "TECG"

    elif pro(prof, "TECNICO DE HEMODIALISE") == "TECNICO DE HEMODIALISE":
        return "TECH"

    elif pro(prof, "TECNICO DE RADIOLOGIA") == "TECNICO DE RADIOLOGIA":
        return "TECR"

    elif pro(prof, "TERAPEUTA OCUPACIONAL") == "TERAPEUTA OCUPACIONAL":
        return "TERA"
