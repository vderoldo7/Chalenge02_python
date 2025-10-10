import os
os.system("cls")
"""
Álvaro Freitas Miranda RM: 565364
Rafael Pascotte Mercadante RM: 564928
Vitor Viana Carneiro Deroldo RM: 565537
"""
#=====================================Área da função/procedimento
def ver_exame(te:list,nome_paciente):

    #Função que exibe o exame do paciente, passando uma tabela de exames(lista) e o nome do paciente para mostrar o exame 
    print("Exame:\n"+("-"*20))
    try:
        if not te:
            print("Nenhum exame encontrado.")
            print("-"*20)
        else:
            for e in te:
                if e["paciente"].lower() == nome_paciente.lower():
                    print(f"Exame: {e['tipo']}")
                    print(f"Data: {e['data']}")
                    print("Resultados:")
                    for k,v in e["resultado"].items():
                        print(f"  {k}: {v}")
                    print("-" * 20)
    except KeyError:
        print("Erro: chave inexistente no dicionário do exame.")
    except Exception as e:
        print(f"Erro inesperado ao exibir exame: {e}")

def mensagem(m:list) -> None:
    #Função que passa por parâmetro uma lista, cujo objetivo é adicionar nessa lista as mensagens do usuário ao médico 
    print("Mensagem ao médico:\n"+("-"*30))
    try:
        esc= 1
        while esc !=0:  
            os.system("cls")
            print("Envie uma mensagem ao médico abaixo: ")
            m.append(input("Digite o que quer escrever ao médico: "))
            print("Sua mensagem: ")
            for i, l in enumerate(m, start=1):
                print(f"{i}. {l}")
            print("-"*30)
            print("\nMensagem enviada com sucesso! O médico entrará em contato com você assim que possível!")
            esc=int(input("Pressione qualquer NÚMERO se quiser escrever mais alguma coisa, caso não, digite 0 para sair :....."))
    except ValueError:
        print("Erro: digite apenas números válidos.")
    except Exception as e:
        print(f"Erro inesperado ao enviar mensagem: {e}")

def registra_consulta(c:dict)->None:
    #Função que passa por parêmtro um dicionário de consultas, e adiciona os dados de uma única consulta nesse dicionário
    try:
        c["Hora"]=(input("Hora: "))
        c["Dia"]=int(input("Dia: "))
        while True:
            c["Mês"]=int(input("Mês (Em número!): "))
            if c["Mês"]>12 or c["Mês"]<1:
                print("Temos apenas 12 meses (1 ao 12) digite com coerência!")
            else:
                break
    except ValueError:
        print("Erro: insira apenas valores numéricos válidos.")
    except Exception as e:
        print(f"Erro inesperado ao registrar consulta: {e}")

def add_tab(t:list,c:dict)->None:
    #Função que passa uma lista(tabela) e um dicionário, adicionando o dicionário na lista em forma de tabela
    t.append(c.copy())

def lista_consulta(t:list)->None:
    #Função que passa uma lista(tabela) e exibe mostrando cada informação de consulta (cada dict na lista era uma consulta diferente)
    try:
        print("Listando todas as consultas registradas:\n"+("-"*30))
        if not t:
            print("Nenhuma consulta marcada!\n"+("-"*25))
        else:
            contador=1
            for c in t:
                print(f"{contador}. {c['Dia']:02d}/{c['Mês']:02d}/{c['Ano']} às {c['Hora']} horas")
                contador=contador+1
                print("-"*30)
    except KeyError:
        print("Erro: chave ausente no dicionário de consulta.")
    except Exception as e:
        print(f"Erro inesperado ao listar consultas: {e}")

def remove_consulta(t:list)->None:
    #Função que passa uma lista(tabela) e exibe mostrando cada informação de consulta (cada dict na lista era uma consulta diferente)
    try:
        if not t:
            print(("-"*25)+"Nenhuma consulta marcada!\n"+("-"*25))
        else:
            lista_consulta(t)
            removedor=int(input("Qual consulta deseja cancelar? (Digite o número)"))
            t.pop(removedor-1)
            print("Consulta cancelada com sucesso!")
    except IndexError:
        print("Erro: índice inválido.")
    except Exception as e:
        print(f"Erro inesperado ao remover consulta: {e}")

def alterar_consulta(t:list)->None:
    #Função que passa uma lista (tabela), exibe essa tabela, e pede pro usuário escolher qual índice irá alterar da tabela 
    try:
        if not t:
            print(("-"*25)+"\nNenhuma consulta marcada!\n"+("-"*25))
        else:
            lista_consulta(t)
            escolha = int(input("Qual consulta deseja alterar? ")) - 1
            if 0 <= escolha < len(t):
                print("Digite os novos dados:")
                t[escolha]["Dia"] = int(input("Novo dia: "))
                while True:
                    t[escolha]["Mês"]=int(input("Novo mês (Em número!): "))
                    if t[escolha]["Mês"]>12 or t[escolha]["Mês"]<1:
                        print("Temos apenas 12 meses (1 ao 12) digite com coerência!")
                    else:
                        break
                t[escolha]["Hora"] =(input("Novo horário: "))
                print("Consulta alterada com sucesso!")
            else:
                print("Opção inválida.")
    except ValueError:
        print("Erro: digite apenas números válidos.")
    except Exception as e:
        print(f"Erro inesperado ao alterar consulta: {e}")

def cria_paciente(p:dict)->None:
    #Função que passa um dict por parâmetro(Informações do paciente) e adiciona em suas keys, values
    try:
        p["Nome"]=(input("Nome: "))
        p["Data de nascimento"]=input("Data de nascimento: ")
        p["Idade"]=int(input("idade: "))
        p["Sexo"]=input("Sexo: ")
        p["CPF"]=input("CPF: ")
        p["Telefone"]=input("Telefone: ")
        p["Email"]=input("Email: ")
        p["Endereço"]=input("Endereço: ")
    except ValueError:
        print("Erro: valor inválido para idade.")
    except Exception as e:
        print(f"Erro inesperado ao criar paciente: {e}")

def listar_paciente(t:list)->None:
    #Função que passa uma lista(tabela) por parâmetro, e a exibe
    print("Informações do cadastro:\n"+("-"*24))
    try:
        if not t:
            print("Nenhum paciente cadastrado!\n"+("-"*24))
        else:
            contador=1
            for p in t:
                for k,v in p.items():
                    print(f"{contador}. {k} : {v}")
                print("-"*24)
    except AttributeError:
        print("Erro: objeto informado não é uma lista de pacientes.")
    except Exception as e:
        print(f"Erro inesperado ao listar pacientes: {e}")

def altera_cadastro(t: list) -> None:
    #Função que passa uma lista(tabela) por parâmetro, exibe a tabela, e o usuário escolhe qual índice (cadastro), deseja alterar
    try:
        if not t:
            print(("-"*22)+"\nNenhum cadastro feito!\n"+("-"*22))
        else:
            listar_paciente(t)  
            escolha = int(input("Qual cadastro deseja alterar? (Digite o número)"))
            paciente = t[escolha-1]
            informacao = input("Qual informação deseja alterar? (Digite do jeito que estiver escrito a informação)")
            if informacao not in paciente:
                print("Informação inválida!")
                return
            novo_valor = input(f"{informacao}: ")
            paciente[informacao] = novo_valor
            print("Cadastro alterado com sucesso!")
    except ValueError:
        print("Erro: valor inválido na alteração do cadastro.")
    except Exception as e:
        print(f"Erro inesperado ao alterar cadastro: {e}")

def remove_cadastro(t:list)->None:
    #Função que passa uma lista(tabela) por parâmetro e o usuário escolhe o índice que irá remover
    try:
        if not t:
            print(("-"*22)+"\nNenhum cadastro feito!\n"+("-"*22))
        else:
            listar_paciente(t)
            removedor=int(input("Qual cadastro deseja cancelar? (Digite o número)"))
            t.pop(removedor-1)
    except IndexError:
        print("Erro: índice inválido na remoção.")
    except Exception as e:
        print(f"Erro inesperado ao remover cadastro: {e}")

#Dicionários e listas(tabela de dicionários) criados para a execução do programa e manipulação de dados
consulta={"Hora":0.0,"Dia":0,"Mês":0,"Ano":2025}
tab_consulta=[]
mensagem_medico=[]
exame={
    "id": 1,
    "paciente": "Paciente01",
    "tipo": "Hemograma",
    "data": "12/09/2025",
    "resultado": {
        "Hemoglobina": "14 g/dL",
        "Leucócitos": "7000 /mm³",
        "Plaquetas": "250000 /mm³"
    }
}
tab_exame=[]
paciente={"Nome":"","Data de nascimento":"","Idade":0,"Sexo": "","CPF": "","Telefone": "","Email": "","Endereço": ""}
tab_paciente=[]

def menu()->None:
    #Programa principal apenas colocado em um def
    while True:
        os.system("cls")
        print("| AIDA - Assistente | \nComo posso ajudar? \n1 - Área de consultas \n2 - Ver resultados de exames \n3 - Enviar uma mensagem ao médico\n4 - Cadastro do paciente\n0 - Sair")
        try:
            #O usuário vai escolher uma das opções do menu
            escolha=int(input("Escolha: "))
        except ValueError:
            print("Digite apenas números válidos.")
            continue

        if escolha==1:
            while True:
                os.system("cls")
                print("1 - Marcar nova consulta\n2 - Listar consultas\n3 - Alterar consulta\n4 - Cancelar consulta\n0 - Voltar")
                try:
                    #O usuário irá escolher uma das opções da área consulta
                    escolha_consulta=int(input("Escolha: "))
                except ValueError:
                    print("Digite apenas números válidos.")
                    continue
                if escolha_consulta==1:
                    #Agenda um consulta do usuário
                    os.system("cls")
                    print("Agende sua consulta: ")
                    registra_consulta(consulta)
                    add_tab(tab_consulta,consulta)
                    print("Consulta Marcada!")
                    input("Aperte enter para continuar")
                elif escolha_consulta==2:
                    #Mostra todas as consultas do usuário (caso não tenha nenhuma, aparece que não tem consultas)
                    os.system("cls")
                    lista_consulta(tab_consulta)
                    input("Aperte enter para continuar")
                elif escolha_consulta==3:
                    #O usuário escolhe qual consulta quer alterar e muda o que precisa na consulta marcada
                    os.system("cls")
                    alterar_consulta(tab_consulta)
                    input("Aperte enter para continuar")
                elif escolha_consulta==4:
                    #O usuário cancela uma consulta
                    os.system("cls")
                    remove_consulta(tab_consulta)
                    input("Aperte enter para continuar")
                elif escolha_consulta==0:
                    os.system("cls")
                    print("Voltando ao menu principal")
                    break
                else:
                    os.system("cls")
                    print("Escolha alguma opção coerente!")
                    continue
        elif escolha==2:
            #Mostra o exame do usuário (Nesse caso o exame já é um pronto fictício por que ainda não estamos conectados no banco de dados)
            os.system("cls")
            add_tab(tab_exame,exame)
            ver_exame(tab_exame,"Paciente01")
        elif escolha==3:
            #O usuário pode mandar uma mensagem ou mais aou médico
            os.system("cls")
            mensagem(mensagem_medico)
        elif escolha==4:
            while True:
                os.system("cls")
                print("1 - Cadastrar paciente\n2 - Informações do cadastro\n3 - Alterar informações\n4 - cancelar cadastro\n0 - Voltar")
                try:
                    #O usuário irá escolher uma das áreas do cadastro paciente do programa
                    escolha_cadastro=int(input("Escolha: "))
                except ValueError:
                    print("Digite apenas números válidos.")
                    continue
                if escolha_cadastro==1:
                    #O usuário pode se cadastrar, ou cadastrar algum parente por exemplo
                    os.system("cls")
                    cria_paciente(paciente)
                    add_tab(tab_paciente,paciente)
                    print("Paciente cadastrado com sucesso!")
                    input("Aperte enter para continuar")
                elif escolha_cadastro==2:
                    #Mostra ao usuário as informações do cadastro (caso não tenha ainda, mostra nenhum paciente cadastrado)
                    os.system("cls")
                    listar_paciente(tab_paciente)
                    input("Aperte enter para continuar")
                elif escolha_cadastro==3:
                    #O usuário escolhe alterar algum cadastro
                    os.system("cls")
                    altera_cadastro(tab_paciente)
                    input("Aperte enter para continuar")
                elif escolha_cadastro==4:
                    #O usuário remove um cadastro
                    os.system("cls")
                    remove_cadastro(tab_paciente)
                    print("Cadastro removido com sucesso!")
                    input("Aperte enter para continuar")
                elif escolha_cadastro==0:
                    os.system("cls")
                    print("Voltando ao menu principal")
                    break
                else:
                    os.system("cls")
                    print("Escolha alguma opção coerente!")
                    continue
        elif escolha==0:
            os.system("cls")
            print("Obrigado por usar a assistente AIDA!")
            break
        else:
            os.system("cls")
            print("Escolha uma das 3 opções!")
            continue
        input("Pressione qualquer tecla para voltar ao menu principal:.....")

#=====================================Área de execução do programa principal
menu()
