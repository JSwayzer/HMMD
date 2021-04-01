# importação de funções específica do módulo calc.py
from function_create_fathos import *
# outra forma seria importa tudo de um única vez:
# from calc import *

while True:
    try:
        notas = []

        op = -1
        while op != 9:
            print("Script para criar profissionais no Fathos")
            print("1 - SQL Script para Checar se usuário já existe no FATHOS"
                  "\n2 - SQL Script para Checar se usuário já existe no MEDVIEW"
                  "\n3 - SQL Script para Inativar usuário FATHOS"
                  "\n4 - SQL Script para Inativar usuário MEDIVEW"
                  "\n3 - SQL Script para Criar usuário FATHOS"
                  "\n5 - SQL Script para Criar usuário MEDIVEW"
                  "\n9 - Sair do programa")
            op = int(input("Escolha sua opção: "))
            if op == 1:
                # ler arquivo fonte dos dados
                readFile = open("admitidos.txt", "r")

                # criar o arquivo que armazenará as novas informações já tratadas
                createFile = open("checar_fathos.txt", "w")

                # loop para ler linha por linha para manipulação
                for x in readFile:
                    x = x.upper()
                    # separar linhas por vírgula (','), transformando em variável do tipo list
                    linha = x.split(',')
                    # CHAPA,NOME,ADMISSAO,CARGO,REGISTRO,SECAO,DTNASCIMENTO,CPF,CARTIDENTIDADE,GESTOR,COD HCIS, UFCRM
                    # após separado por vírgula, os textos podem ser lidos pelo índice: 0,1,2,3,4,5,6,7,8,9,10,11
                    print("DRT"+linha[0]+"\n"+linha[1]+"\n"+linha[7]+"\n"+linha[6]+"\n"+linha[3]+"\n"+linha[4])
                    exit()

                    # Chamar função para definir a Profissão
                    codProfissao = profissao(linha[3])
                    # Chamar função para definir a Categoria profissional
                    codCategoria = categoria(linha[3])
                    # Chamar função para definir o Tipo de Conselho Regional
                    codConselho = tipoconselho(3)

                    # Essas variáveis podem ser vazias, caso não seja médico ou outras profissões que tenha
                    # regsitro em Conselho regional
                    numRegistro = ""
                    ufCRM = ""
                    indPermIntern = "N"
                    indPermAssLaudo = "N"

                    if codProfissao.upper() == "MEDC":
                        numRegistro = linha[4]
                        ufCRM = linha[11]
                        # Chamar função para definir o Grupo Medico
                        gpMedico = grupomedico(linha[3])
                        # Chamar função para definir o Especialidade Médica
                        espMedica = especialidade(3)
                        indPermIntern = "S"
                        indPermAssLaudo = "S"

                    elif codProfissao.upper() == "ENFR":
                        numRegistro = linha[4]
                        ufCRM = linha[11]

                    elif codProfissao.upper() == "TECE":
                        numRegistro = linha[4]
                        ufCRM = linha[11]

                    # escrever no arquivo as informações manipuladas

                    # createFile.write(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8],linha[9])

                    createFile.write("DRT"+linha[0])

                    print(
                        "INSERT INTO FAPROCAD ( cpf,crm,uf_crm,cod_ant,cod_pro_corp,cod_profissao,"
                        "fone_celular,bip_pager,email,nome_reduzido,cod_cnes,NU_CNS,SN_EXIBE_RES_CIRURGIA,"
                        "cod_categ,SN_NAO_TEM_INFORMOU_EMAIL,cep_res,end,bairro_res,cidade_res,estado_res,"
                        "NUMERO_RES,COMPLEMENTO_RES,fone_res,cep_tra,end_tra,bairro_tra,cidade_tra,estado_tra,"
                        "NUMERO_TRAB,COMPLEMENTO_TRAB,fone_tra,TP_EST_CIVIL,DS_ORGAO_EMIS_ID,NO_PAI,"
                        "DS_FORMAC_PROF,NU_ID,DS_NACIONALIDADE,NO_MAE,TP_ESCOLARIDADE,SG_UF_NASC,FK_LOCALI_NASC,"
                        "TP_RACA_COR,TP_SIT_CONJUGAL,SG_UF_ID,NU_OUTROS_DOCUMENT,DS_CARGO,SN_INCAPAZ_BIOM,banco,"
                        "conta,agencia,funcionario,staff,docente,sn_cooperado,perc_impos,recibo,ind_perm_intern,"
                        "ind_perm_ass_laudo,sn_lib_laudo_prov,ind_perm_comanda,cta_provisao_mega,cta_adianta_mega,"
                        "cod_movto_mega,repasse_grupo_mega,classe_finan_mega,cod_pro,nome_pro,data_nascimento,"
                        "inativo,tratamento,grupo,perc_hosp,tipo_pac_autoriz,cod_tp_conselho,cod_tipo_lograd_re,"
                        "cod_tipo_lograd_tr,DS_HORARIOS,FK_CEP_RES,FK_CEP_TRA ) "
                        "VALUES "
                        "('"+linha[7]+"','"+numRegistro+"','"+ufCRM+"','"+linha[10]+"','','"+codProfissao+"',"
                        "'','','','','','','N','"+codCategoria+"','S',"
                        "'04948970','ESTRADA DO M BOI MIRIM 4815','JARDIM ANGELA (ZONA SUL)','SAO PAULO','SP','5203',"
                        "NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'1158322500',NULL,'','','','','','',"
                        "NULL,NULL,NULL,NULL,NULL,NULL,'','','N','','','','S','N','N','N',0,'N',"
                        "'"+indPermIntern+"','"+indPermAssLaudo+"','N','S',"
                        "'','','','N','','"+linha[10]+"','"+linha[1]+"',To_Date('"+linha[6]+"', 'DD/MM/YYYY'),"
                        "'N',NULL,'"+gpMedico+"',NULL,'IAUE','"+codConselho+"',NULL,NULL,NULL,885459,NULL);")

                    createFile.close()

                readFile.close()

            elif op == 2:
                print("Script para criar profissionais no Fathos")
                print("Script para criar profissionais no Fathos")
            elif op == 3:
                print("Script para criar profissionais no Fathos")
                print("Script para criar profissionais no Fathos")
            elif op == 4:
                print("Script para criar profissionais no Fathos")
                print("Script para criar profissionais no Fathos")
            elif op == 5:
                print("Script para criar profissionais no Fathos")
                print("Script para criar profissionais no Fathos")
    except ValueError:
        print("\nOops! Não foi informado um valor válido, tente novamente...\n\n")
    break
