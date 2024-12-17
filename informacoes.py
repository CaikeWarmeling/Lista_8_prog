from classes import Aluno, Professor, Turma, Disciplina
from random import randint

nomes = [
        "Ana", "Beatriz", "Carlos", "Daniel", "Elisa", "Fábio", "Gabriela",
        "Hugo", "Isabela", "João", "Karla", "Lucas", "Mariana", "Neto",
        "Otávio", "Paula", "Quentin", "Rafael", "Sofia", "Tiago", "Ulisses",
        "Vanessa", "ellington", "Xavier", "Yara", "Zeca", "André", "Bianca",
        "Caio", "Diego", "Estela", "Flávia", "Gustavo", "Helena", "Igor",
        "Juliana", "Kelvin", "Letícia", "Miguel", "Nathalia", "Orlando", "Priscila",
        "Quélvia", "Ricardo", "Samara", "Thales", "Úrsula", "Vitor", "Wagner",
        "Yasmin", "Zara", "Artur", "Breno", "Cássia", "David", "Flávio",
        "Enzo", "Fernanda", "Hugo", "Lúcia", "Joana", "Rogério", "Carlos",
        "Renata", "Simone", "Felipe", "Tatiane", "Paulo", "Marta", "Eduardo",
        "Juliano", "Alice", "Raimundo", "Roberta", "Júlia"
]

sobrenomes = [
        "Silva", "Santos", "Oliveira", "Costa", "Pereira", "Rodrigues", "Almeida",
        "Sousa", "Ferreira", "Gomes", "Martins", "Lima", "Carvalho", "Ribeiro",
        "Fernandes", "Araújo", "Nascimento", "Mendes", "Dias", "Pinto", "Vieira",
        "Moreira", "Barbosa", "Gonçalves", "Campos", "Cavalcante", "Teixeira",
        "Moura", "Souza", "Cunha", "Maciel", "Queiroz", "Freitas", "Figueiredo",
        "Borges", "Fonseca", "Castro", "Lopes", "Nascimento", "Costa", "Alves",
        "Azevedo", "Tavares", "Martins", "Ramos", "Siqueira", "Guilherme", "Santana",
        "Monteiro", "Lourenço", "Pereira", "Barros", "Faria", "Britto", "Dantas",
        "Severino", "Matos", "Silveira", "Lacerda", "Borges", "Medeiros",
        "Lima", "Lopes", "Pimentel", "Batista", "Serrano", "Cardoso",
        "Ferreira", "Lima", "Cavalcanti"
]

enderecos = [
        "João Silva, Rua das Flores, 123, São Paulo, SP, 01000-000",
        "Maria Oliveira, Avenida Brasil, 456, Rio de Janeiro, RJ, 20000-000",
        "Carlos Pereira, Rua da Paz, 789, Belo Horizonte, MG, 30000-000"
        "Ana Souza, Rua São João, 101, Curitiba, PR, 80000-000"
        "Avenida Atlântica, 1010, Rio de Janeiro, RJ, 22010-000",
        "Rua do Sol, 555, Salvador, BA, 40000-000",
        "Avenida Beira-Mar, 100, Fortaleza, CE, 60000-000"
]

cpfs = [
        "123.456.789-00", "234.567.890-01", "345.678.901-02", "456.789.012-03", "567.890.123-04",
        "678.901.234-05", "789.012.345-06", "890.123.456-07", "901.234.567-08", "012.345.678-09",
        "234.567.890-10", "345.678.901-11", "456.789.012-12", "567.890.123-13", "678.901.234-14",
        "789.012.345-15", "890.123.456-16", "901.234.567-17", "012.345.678-18", "123.456.789-19",
        "234.567.890-20", "345.678.901-21", "456.789.012-22", "567.890.123-23", "678.901.234-24",
        "789.012.345-25", "890.123.456-26", "901.234.567-27", "012.345.678-28", "123.456.789-29",
        "234.567.890-30", "345.678.901-31", "456.789.012-32", "567.890.123-33", "678.901.234-34",
        "789.012.345-35", "890.123.456-36", "901.234.567-37", "012.345.678-38", "123.456.789-39",
        "234.567.890-40", "345.678.901-41", "456.789.012-42", "567.890.123-43", "678.901.234-44",
        "789.012.345-45", "890.123.456-46", "901.234.567-47", "012.345.678-48", "123.456.789-49",
        "234.567.890-50", "345.678.901-51", "456.789.012-52", "567.890.123-53", "678.901.234-54",
        "789.012.345-55", "890.123.456-56", "901.234.567-57", "012.345.678-58", "123.456.789-59",
]

#criando alunos e turmas EM:
print("-----------------------------------------------------------------------------------------")
print("Alunos EM\n")

alunos_EM = []
for i in range(1, 4):
    if i == 1:
            cursos = "informatica"
    elif i == 2:
            cursos = "mecatronica"
    else:
            cursos = "eletromecanica"

    for i in range(1, 21):
        nome = nomes[randint(0, len(nomes) - 1)]
        filiacoes = nomes[randint(0, len(nomes) - 1)]
        sobrenome = sobrenomes[randint(0, len(sobrenomes) - 1)]
        email = f"{nome}.{sobrenome}@gmail.com"
        endereco = enderecos[randint(0, len(enderecos) - 1)]

        alunos_EM.append(Aluno(
            primeiro_nome=nome,
            sobrenome=sobrenome,
            email=email,
            senha="12345678",
            turma="01",
            endereco=endereco,
            filiacoes=filiacoes,
            ra=f"2024{randint(100, 999)}",
            segmento="EM",
            curso=cursos,
            status=True)),

        print(alunos_EM[-1].email,"\n", alunos_EM[-1].curso,"\n", alunos_EM[-1].ra)

#criando alunos e tumas superior:
print("-----------------------------------------------------------------------------------------")
print("Alunos superior\n")

alunos_superior = []
for i in range(1, 4):
        if i == 1:
                cursos = "bacharel em ciencias da computacao"
        elif i == 2:
                cursos = "bacharel em pedagogia"
        else:
                cursos = "bacharel em ciencias da computacao", "bacharel em pedagogia"

        for i in range(1, 6):
                nome = nomes[randint(0, len(nomes) - 1)]
                filiacoes = nomes[randint(0, len(nomes) - 1)]
                sobrenome = sobrenomes[randint(0, len(sobrenomes) - 1)]
                email = f"{nome}.{sobrenome}@gmail.com"
                endereco = enderecos[randint(0, len(enderecos) - 1)]

                alunos_superior.append(Aluno(
                        primeiro_nome=nome,
                        sobrenome=sobrenome,
                        email=email,
                        senha="12345678",
                        turma="01",
                        endereco=endereco,
                        filiacoes=filiacoes,
                        ra=f"2024{randint(100, 999)}",
                        segmento="superior",
                        curso=cursos,
                        status=True)),

                print(alunos_superior[-1].email,"\n", alunos_superior[-1].curso,"\n", alunos_superior[-1].ra)

# Disciplinas gerais: portugues, matematica, fisica, quimica, biologia.
# Disciplinas EM: informatica: programação, mecatronica: elementos de maquina, eletromecanica: hidraulica e pneumatica.
# Disciplinas superior: pedagogia: gramatica ciencias da computacao: teoria dos grafos.
 
#Criando professores gerais:
print("-----------------------------------------------------------------------------------------")
print("Professores gerais\n")

professores_geral = []
for i in range(1, 6):
        if i == 1:
                disciplinas = "portugues"
        elif i == 2:
                disciplinas = "matematica"
        elif i == 3:
                disciplinas = "fisica"
        elif i == 4:
                disciplinas = "quimica"
        else:
                disciplinas = "biologia"

        for i in range(1, 3):
                nome = nomes[randint(0, len(nomes) - 1)]
                sobrenome = sobrenomes[randint(0, len(sobrenomes) - 1)]
                cpf = cpfs[randint(0, len(cpfs) -1)]
                email = f"{nome}.{sobrenome}@gmail.com"

                professores_geral.append(Professor(
                        primeiro_nome=nome,
                        sobrenome=sobrenome,
                        cpf=cpf,
                        formacao=nome, 
                        turmas="01",
                        disciplinas=disciplinas,
                        email=email,
                        senha="12345678",
                        status=True))
                
                print(professores_geral[-1].email,"\n", professores_geral[-1].disciplinas)

#Criando professores EM:
print("-----------------------------------------------------------------------------------------")
print("Professores EM\n")

professores_EM = []
for i in range(1, 4):
        if i == 1:
                disciplinas = "programacao"
        elif i == 2:
                disciplinas = "elementos de maquina"
        else:
                disciplinas = "hidraulica e pneumatica"

        for i in range(1, 3):
                nome = nomes[randint(0, len(nomes) - 1)]
                sobrenome = sobrenomes[randint(0, len(sobrenomes) - 1)]
                cpf = cpfs[randint(0, len(cpfs) -1)]
                email = f"{nome}.{sobrenome}@gmail.com"

                professores_EM.append(Professor(
                        primeiro_nome=nome,
                        sobrenome=sobrenome,
                        cpf=cpf,
                        formacao=disciplinas, 
                        turmas="01",
                        disciplinas=disciplinas,
                        email=email, 
                        senha="12345678",
                        status=True))
                
                print(professores_EM[-1].email,"\n", professores_EM[-1].disciplinas)

#Criando professores superior:
print("-----------------------------------------------------------------------------------------")
print("Professores superior\n")

professores_superior = []
for i in range(1, 3):
        if i == 1:
                disciplinas = "gramatica"
        else:
                disciplinas = "teoria dos grafos"

        for i in range(1, 3):
                nome = nomes[randint(0, len(nomes) - 1)]
                sobrenome = sobrenomes[randint(0, len(sobrenomes) - 1)]
                cpf = cpfs[randint(0, len(cpfs) -1)]
                email = f"{nome}.{sobrenome}@gmail.com"

                professores_superior.append(Professor(
                        primeiro_nome=nome,
                        sobrenome=sobrenome,
                        cpf=cpf,
                        formacao=disciplinas, 
                        turmas="01",
                        disciplinas=disciplinas,
                        email=email, 
                        senha="12345678",
                        status=True))
                
                print(professores_superior[-1].email,"\n", professores_superior[-1].disciplinas)

#criando as disciplinas gerais EM:
print("-----------------------------------------------------------------------------------------")
print("Disciplinas gerais\n")

disciplinas_gerais = []
for i in range(1, 6):
        if i == 1:
                nome = "portugues"
                descricao = "Estudo da língua portuguesa, incluindo gramática, leitura, escrita e literatura, com foco em comunicação e interpretação de textos"
        elif i == 2:
                nome = "matematica"
                descricao = "Estudo de números, formas e estruturas, abordando tópicos como álgebra, geometria, cálculo e estatística, desenvolvendo raciocínio lógico"
        elif i == 3:
                nome = "fisica"
                descricao = "Ciência que estuda a matéria, energia e os fenômenos naturais, explicando leis do movimento, luz, som, eletricidade, entre outros"
        elif i == 4:
                nome = "quimica"
                descricao = "Estudo das substâncias, suas reações e transformações, investigando a composição e propriedades da matéria"
        else:
                nome = "biologia"
                descricao = "Estudo dos seres vivos, seus processos vitais, anatomia, evolução e ecologia, explorando a interação dos organismos com o ambiente"

        professor_titular = ""
        for professor in professores_geral:
                if professor.disciplinas == nome:
                        professor_titular = professor.email

        disciplinas_gerais.append(Disciplina(
                id= "01",
                nome=nome,
                descricao=descricao,
                segmento="informatica, mecatronica, eletromecanica",
                professor_titular=professor_titular,
                status=True))
        print(disciplinas_gerais[-1].nome,"\n", disciplinas_gerais[-1].professor_titular)
        
#criando as disciplinas dos cursos EM
print("-----------------------------------------------------------------------------------------")
print("Disciplinas EM\n")

disciplinas_EM = []
for i in range(1, 4):
        if i == 1:
                nome = "programacao"
                descricao = "Estudo de técnicas para escrever códigos de computador, utilizando linguagens de programação para criar softwares, aplicativos e sistemas."
                segmento="informatica"
        elif i == 2:
                nome = "elementos de maquina"
                descricao = "Estudo dos componentes e mecanismos usados em máquinas, como engrenagens, eixos e rolamentos, focando em seu funcionamento e design."
                segmento="mecatronica"
        else:
                nome = "hidraulica e pneumatica"
                descricao = "Estudo do uso de fluidos (geralmente água) para transmitir energia e realizar trabalhos, como em sistemas de pressão e máquinas hidraulicas. Estudo do uso de ar comprimido para gerar movimento e realizar tarefas em sistemas mecânicos, como em atuadores e ferramentas pneumaticas."
                segmento="eletromecanica"

        professor_titular = ""
        for professor in professores_EM:
                if professor.disciplinas == nome:
                        professor_titular = professor.email

        disciplinas_EM.append(Disciplina(
                id= "01",
                nome=nome,
                descricao=descricao,
                segmento=segmento,
                professor_titular=professor_titular,
                status=True))
        print(disciplinas_EM[-1].nome,"\n", disciplinas_EM[-1].professor_titular)

#criando as disciplinas dos cursos superior:
print("-----------------------------------------------------------------------------------------")
print("Disciplinas superior\n")

disciplinas_superior = []
for i in range(1, 3):
        if i == 1:
                nome = "gramatica"
                descricao = "Estudo das regras e estruturas que governam a língua, incluindo sintaxe, morfologia, fonologia e ortografia, com o objetivo de entender e produzir corretamente a linguagem."
                segmento="bacharel em pedagogia"
        else:
                nome = "teoria dos grafos"
                descricao = "Área da matemática que estuda grafos, que são estruturas compostas por vértices (nós) e arestas (conexões entre os nós). É usada para modelar redes, caminhos e relações em diversos contextos, como computacao e redes sociais."
                segmento="bacharel em ciencias da computacao"

        professor_titular = ""
        for professor in professores_superior:
                if professor.disciplinas == nome:
                        professor_titular = professor.email

        disciplinas_superior.append(Disciplina(
                id= i,
                nome=nome,
                descricao=descricao,
                segmento=segmento,
                professor_titular=professor_titular,
                status=True))
        print(disciplinas_superior[-1].nome,"\n", disciplinas_superior[-1].professor_titular)

#Criando turmas EM
print("-----------------------------------------------------------------------------------------")
print("Turmas EM")

turmas_EM = []
for i in range(1, 4):
        if i == 1:
                nome = "turma informatica 01"
                curso = "informatica"
                disciplinas = "programacao"
        elif i == 2:
                nome = "turma mecatronica 01"
                curso = "mecatronica"
                disciplinas = "elementos de maquina"
        else:
                nome = "turma eletromecanica 01"
                curso = "eletromecanica"
                disciplinas = "hidraulica e pneumatica"

        nome_alunos = []
        for alunos in alunos_EM:
                if alunos.curso == curso:
                        nome_alunos.append(alunos.email)

        nome_professor = []
        for professor in professores_geral:
            nome_professor.append(professor.email)
        for professor in professores_EM:
            if professor.disciplinas == disciplinas:
                nome_professor.append(professor.email)

        nome_disciplinas = []
        for disciplina in disciplinas_gerais:
            nome_disciplinas.append(disciplina.nome)
        for disciplina in disciplinas_EM:
            if disciplina.nome == disciplinas:
                nome_disciplinas.append(disciplina.nome)

        turmas_EM.append(Turma(
                nome=nome,
                segmento="EM",
                curso=curso,
                ano="2024",
                alunos=nome_alunos,
                professores=nome_professor, 
                disciplinas=nome_disciplinas,
                status=True))
        print("\n PROFESSORES: ",turmas_EM[-1].professores,"\n \n ALUNOS: ", turmas_EM[-1].alunos,"\n \n DISCIPLINAS: ", turmas_EM[-1].disciplinas)

#Criando turmas superior
print("-----------------------------------------------------------------------------------------")
print("Turmas superior")

turmas_superior = []
for i in range(1, 3):
        if i == 1:
                nome = "turma bacharel em pedagogia 01"
                curso = "bacharel em pedagogia"
                disciplina = "gramatica"
        else:
                nome = "turma bacharel em ciencias da computacao 01"
                curso = "bacharel em ciencias da computacao"
                disciplina = "teoria dos grafos"

        nome_alunos = []
        for alunos in alunos_superior:
                conferindo = alunos.curso == ("bacharel em ciencias da computacao","bacharel em pedagogia")
                if alunos.curso == curso or conferindo:
                        nome_alunos.append(alunos.email)

        nome_professor = []
        for professor in professores_superior:
            if professor.disciplinas == disciplina:
                nome_professor.append(professor.email)

        turmas_EM.append(Turma(
                nome=nome,
                segmento="superior",
                curso=curso,
                ano="2024",
                alunos=nome_alunos,
                professores=nome_professor, 
                disciplinas=disciplina,
                status=True))
        print("\n PROFESSORES: ",turmas_EM[-1].professores,"\n \n ALUNOS: ", turmas_EM[-1].alunos,"\n \n DISCIPLINAS: ", turmas_EM[-1].disciplinas)

print("\n \n \n")
print("Banco de dados acima")