# importação de funções específica do módulo calc.py
from function_create_fathos import *
# outra forma seria importa tudo de um única vez:
# from calc import *

# while True:
#    try:
op = -1
while op != 0:
    print("Script para criar profissionais no Fathos"
          "\n1 - SQL Script para Checar se usuário já existe e se está inativo no FATHOS"
          "\n2 - SQL Script para Checar se usuário já existe e se está inativo no MEDVIEW"
          "\n3 - SQL Script para Inativar usuário FATHOS"
          "\n4 - SQL Script para Inativar usuário MEDIVEW"
          "\n5 - SQL Script para Criar usuário FATHOS"
          "\n6 - SQL Script para Criar usuário MEDIVEW"
          "\n0 - Sair do programa")
    op = int(input("Escolha sua opção: "))
    if op == 1:
        # ler arquivo fonte dos dados
        # NOME
        readFile = open("admitidos.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_fathos.txt", "w")
        createFile.write("select x.inativo, x.nome_pro, x.cod_pro, x.cpf, x.data_nascimento "
                         "from faprocad x where ( x.nome_pro in (")
        # loop para ler linha por linha para manipulação
        # escrever nome:
        for x in readFile:
            x = x.upper()
            # separar linhas por vírgula (','), transformando em variável do tipo list
            linha = x.split(',')

            # escrever no arquivo as informações manipuladas

            # CHAPA,NOME,ADMISSAO,CARGO,REGISTRO,SECAO,DTNASCIMENTO,CPF,CARTIDENTIDADE,GESTOR,COD HCIS, UFCRM
            # após separado por vírgula, os textos podem ser lidos pelo índice: 0,1,2,3,4,5,6,7,8,9,10,11
            # escreverNome = (", '"+linha[1]+"'\n")
            # print(escreverNome)
            createFile.write("'"+linha[1]+"',")

        createFile.write(")")
        createFile.close()
        readFile.close()

        # CPF
        readFile = open("admitidos.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_fathos.txt", "a")
        createFile.write("\n or x.cpf in (")
        for y in readFile:
            linha = y.split(',')
            createFile.write("'"+linha[7]+"',")
            print(linha[7])
        createFile.write(")")
        createFile.close()
        readFile.close()

        # CRM
        readFile = open("admitidos.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_fathos.txt", "a")
        createFile.write("\n or x.crm in (")
        for z in readFile:
            linha = z.split(',')
            createFile.write("'"+linha[4]+"',")
        createFile.write("))")
        createFile.close()
        readFile.close()

        # data_nascimento
        readFile = open("admitidos.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_fathos.txt", "a")
        createFile.write("\n and x.data_nascimento in (")
        for w in readFile:
            linha = w.split(',')
            createFile.write("To_Date('"+linha[6]+"', 'DD/MM/YYYY'),")
        createFile.write(");")
        createFile.close()
        readFile.close()
    elif op == 2:
        # CHAPA,NOME,DTNASCIMENTO,CPF,COD HCIS,LOGIN
        # após separado por vírgula, os textos podem ser lidos pelo índice: 0,1,6,7,10,12
        readFile = open("admitidos.txt", "r")
        createFile = open("checar_medview.txt", "w")
        createFile.write('select x.ind_usuario_ativo, sn_usu_bloqueado, x.matricula, x.apelido, x.nome, '
                         'x.cod_pro, x.cpf, x.dh_nascimento from fausucad x where ( x.nome in (')
        # NOME
        for nome in readFile:
            nome = nome.upper()
            linha = nome.split(',')
            createFile.write("'"+linha[1]+"',")
        createFile.write(")")
        createFile.close()
        readFile.close()

        # apelido
        readFile = open("admitidos.txt", "r")
        createFile = open("checar_medview.txt", "a")
        createFile.write("\n or x.apelido in (")
        for apelido in readFile:
            apelido = apelido.upper()
            linha = apelido.split(',')
            createFile.write("'"+linha[12]+"',")
        createFile.write(")")
        createFile.close()
        readFile.close()

        # matricula
        readFile = open("admitidos.txt", "r")
        createFile = open("checar_medview.txt", "a")
        createFile.write("\n or x.matricula in (")
        for matricula in readFile:
            linha = matricula.split(',')
            createFile.write("'"+linha[0]+"',")
        createFile.write(")")
        createFile.close()
        readFile.close()

        # CPF
        readFile = open("admitidos.txt", "r")
        createFile = open("checar_medview.txt", "a")
        createFile.write("\n or x.cpf in (")
        for cpf in readFile:
            linha = cpf.split(',')
            createFile.write("'"+linha[7]+"',")
            print(linha[7])
        createFile.write(")")
        createFile.close()
        readFile.close()

        # cod_pro
        readFile = open("admitidos.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_medview.txt", "a")
        createFile.write("\n or x.cod_pro in (")
        for cod_pro in readFile:
            linha = cod_pro.split(',')
            createFile.write("'"+linha[10]+"',")
        createFile.write("))")
        createFile.close()
        readFile.close()

        # data_nascimento
        readFile = open("admitidos.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_medview.txt", "a")
        createFile.write("\n and x.dh_nascimento in (")
        for dh_nascimento in readFile:
            linha = dh_nascimento.split(',')
            createFile.write("To_Date('"+linha[6]+"', 'DD/MM/YYYY'),")
        createFile.write(");")
        createFile.close()
        readFile.close()
    elif op == 3:
        readFile = open("admitidos.txt", "r")
        createFile = open("inativar_fathos.txt", "a")
        for x in readFile:
            x = x.upper()
            linha = x.split(',')
            # CHAPA,NOME,ADMISSAO,CARGO,REGISTRO,SECAO,DTNASCIMENTO,CPF,
            # CARTIDENTIDADE,GESTOR,COD HCIS, UFCRM,LOGIN,DH_VALIDADE
            # após separado por vírgula, os textos podem ser lidos pelo índice: 0,1,2,3,4,5,6,7,8,9,10,11,12,13
            createFile.write("update faprocad x set x.inativo = 'S' "
                             "where x.nome_pro = '"+linha[1]+"' and x.cpf = '"+linha[7]+"';\n")
        createFile.close()
        readFile.close()
    elif op == 4:
        readFile = open("admitidos.txt", "r")
        createFile = open("inativar_medview.txt", "a")
        for x in readFile:
            x = x.upper()
            linha = x.split(',')
# createFile.write("update fausucad x set x.ind_usuario_ativo = 'N' and sn_usu_bloqueado = 'S' "
# "where x.matricula = '"+linha[0]+"' or x.apelido = '"+linha[12]+"' or x.cod_pro = '"+linha[10]+"' "
# "(x.nome = '"+linha[1]+"' and x.cpf = '"+linha[7]+"' and x.dh_nascimento = '"+linha[6]+"';\n")
            createFile.write("update fausucad x set x.ind_usuario_ativo = 'N' and sn_usu_bloqueado = 'S' "
                             "where x.nome = '"+linha[1]+"' and x.cpf = '"+linha[7]+"' and"
                             " x.dh_nascimento = '"+linha[6]+"';\n")
        createFile.close()
        readFile.close()
    elif op == 5:
        # ler arquivo fonte dos dados
        readFile = open("admitidos.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_fathos.txt", "w")

        # loop para ler linha por linha para manipulação
        for x in readFile:
            x = x.upper()
            # separar linhas por vírgula (','), transformando em variável do tipo list
            linha = x.split(',')
        # CHAPA,NOME,ADMISSAO,CARGO,REGISTRO,SECAO,DTNASCIMENTO,
        # CPF,CARTIDENTIDADE,GESTOR,COD HCIS, UFCRM,LOGIN,DH_VALIDADE
        # após separado por vírgula, os textos podem ser lidos pelo índice: 0,1,2,3,4,5,6,7,8,9,10,11,12,13
        # print("DRT"+linha[0]+"\n"+linha[1]+"\n"+linha[7]+"\n"+linha[6]+"\n"+linha[3]+"\n"+linha[4])
        # exit()

        # Chamar função para definir a Profissão
        codProfissao = profissao(linha[3])
        print(codProfissao)
        # Chamar função para definir a Categoria profissional
        codCategoria = categoria(linha[3])
        print(codCategoria)
        # Chamar função para definir o Tipo de Conselho Regional
        codConselho = tipoconselho(3)
        print(codConselho)

        # Essas variáveis podem ser vazias, caso não seja médico ou outras profissões que tenha
        # regsitro em Conselho regional
        numRegistro = ""
        ufCRM = ""
        indPermIntern = "N"
        indPermAssLaudo = "N"
        gpMedico = "''"

        if codProfissao == "MEDC":
            numRegistro = linha[4]
            ufCRM = linha[11]
            # Chamar função para definir o Grupo Medico
            gpMedico = grupomedico(linha[3])
            # Chamar função para definir o Especialidade Médica
            espMedica = especialidade(3)
            indPermIntern = "S"
            indPermAssLaudo = "S"

        elif codProfissao == "ENFR":
            numRegistro = linha[4]
            ufCRM = linha[11]

        elif codProfissao == "TECE":
            numRegistro = linha[4]
            ufCRM = linha[11]

        createFile.write("INSERT INTO FAPROCAD ( cpf,crm,uf_crm,cod_ant,cod_pro_corp,cod_profissao,"
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
                         "cod_tipo_lograd_tr,DS_HORARIOS,FK_CEP_RES,FK_CEP_TRA ) VALUES "
                         "('"+linha[7]+"','"+numRegistro+"','"+ufCRM+"','"+linha[10]+"','"
                         "','"+codProfissao+"','','','','','','','N','"+codCategoria+"','S',"
                         "'04948970','ESTRADA DO M BOI MIRIM 4815','JARDIM ANGELA (ZONA SUL)','SAO PAULO','SP','5203',"
                         "NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'1158322500',NULL,'','','','','','',"
                         "NULL,NULL,NULL,NULL,NULL,NULL,'','','N','','','','S','N','N','N',0,"
                         "'N',"+linha[10]+"','"+linha[1]+"',To_Date('"+linha[6]+"', 'DD/MM/YYYY'),"
                         "'N',NULL,'"+gpMedico+"',NULL,'IAUE','"+codConselho+"',NULL,NULL,NULL,885459,NULL);")


        print("INSERT INTO FAPROCAD ( cpf,crm,uf_crm,cod_ant,cod_pro_corp,cod_profissao,"
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
              "cod_tipo_lograd_tr,DS_HORARIOS,FK_CEP_RES,FK_CEP_TRA ) VALUES "
              "('"+linha[7]+"','"+numRegistro+"','"+ufCRM+"','"+linha[10]+"','"
              "','"+codProfissao+"','','','','','','','N','"+codCategoria+"','S',"
              "'04948970','ESTRADA DO M BOI MIRIM 4815','JARDIM ANGELA (ZONA SUL)','SAO PAULO','SP','5203',"
              "NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'1158322500',NULL,'','','','','','',"
              "NULL,NULL,NULL,NULL,NULL,NULL,'','','N','','','','S','N','N','N',0,"
              "'N',"+linha[10]+"','"+linha[1]+"',To_Date('"+linha[6]+"', 'DD/MM/YYYY'),"
              "'N',NULL,'"+gpMedico+"',NULL,'IAUE','"+codConselho+"',NULL,NULL,NULL,885459,NULL);")

#    except ValueError:
#        print("\nOops! Não foi informado um valor válido, tente novamente...\n\n")
#    break
