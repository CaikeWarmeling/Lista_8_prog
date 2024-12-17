from informacoes import alunos_EM, alunos_superior, professores_geral, professores_EM, professores_superior, disciplinas_gerais, disciplinas_EM, disciplinas_superior, turmas_EM, turmas_superior
erro1 = False
erro2 = False
erro3 = False
not_erro = False

print("-----------------------------------------------------------------------------------------")
print("Bem vindo ao sistema!")
print("-----------------------------------------------------------------------------------------")

interacao1 = int(input("O que deseja fazer: \n 1: Incerir. \n 2: Editar. \n 3: Desativar. \n 4: Excluir. \n Escolha a interação: "))
print("\n")
if interacao1 == 1:
    print("Em desenvolvimento!")

elif interacao1 == 2:
    interacao2 = int(input("O que deseja editar: \n 1: Aluno. \n 2: Professor. \n 3: Disciplina. \n 4: Turma. \n Escolha a interação: "))
    
    if interacao2 == 1:
        segmento_aluno = input("Digite qual o segmento do aluno: ")
        if segmento_aluno == "EM":
            curso_aluno_EM = input("Digite o curso do aluno do ensino médio: ")
            if curso_aluno_EM == "Informatica":
                email_aluno_EM = input("Digite o email do aluno de informática: ")
                senha_aluno_EM = input("Digite a senha do aluno de informática: ")
                for i in alunos_EM:
                    if i.email == email_aluno_EM and i.senha == senha_aluno_EM:
                        i.email = input("digite o novo email do aluno de informática: ")
                        i.senha = input("digite a nova senha do aluno de informática: ")
                        i.turma = input("digite a nova turma do aluno de informática: ")
                        i.endereco = input("digite o novo endereço do aluno de informática: ")
                        i.filiacoes = input("digite a nova filiação do aluno de informática: ")
                        i.curso = input("digite o novo curso do aluno de informática: ")
                        print("Aluno alterado com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True

            elif curso_aluno_EM == "Mecatronica":
                email_aluno_EM = input("Digite o email do aluno de mecatrônica: ")
                senha_aluno_EM = input("Digite a senha do aluno de mecatrônica: ")
                for i in alunos_EM:
                    if i.email == email_aluno_EM and i.senha == senha_aluno_EM:
                        i.email = input("digite o novo email do aluno de mecatrônica: ")
                        i.senha = input("digite a nova senha do aluno de mecatrônica: ")
                        i.turma = input("digite a nova turma do aluno de mecatrônica: ")
                        i.endereco = input("digite o novo endereço do aluno de mecatrônica: ")
                        i.filiacoes = input("digite a nova filiação do aluno de mecatrônica: ")
                        i.curso = input("digite o novo curso do aluno de mecatrônica: ")
                        print("Aluno alterado com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True
                    
            elif curso_aluno_EM == "Eletromecanica":
                email_aluno_EM = input("Digite o email do aluno de Eletromecanica: ")
                senha_aluno_EM = input("Digite a senha do aluno de Eletromecanica: ")
                for i in alunos_EM:
                    if i.email == email_aluno_EM and i.senha == senha_aluno_EM:
                        i.email = input("digite o novo email do aluno de Eletromecanica: ")
                        i.senha = input("digite a nova senha do aluno de Eletromecanica: ")
                        i.turma = input("digite a nova turma do aluno de Eletromecanica: ")
                        i.endereco = input("digite o novo endereço do aluno de Eletromecanica: ")
                        i.filiacoes = input("digite a nova filiação do aluno de Eletromecanica: ")
                        i.curso = input("digite o novo curso do aluno de Eletromecanica: ")
                        print("Aluno alterado com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True
            else:
                print("Curso informado invalido!")

        elif segmento_aluno == "Superior":
            curso_aluno_superior = input("Digite o curso do aluno do curso superior: ")
            if curso_aluno_superior == "Pedagogia":
                email_aluno_superior = input("Digite o email do aluno de pedagogia: ")
                senha_aluno_superior = input("Digite a senha do aluno de pedagogia: ")
                for i in alunos_superior:
                    if i.email == email_aluno_superior and i.senha == senha_aluno_superior:
                        i.email = input("digite o novo email do aluno de pedagogia: ")
                        i.senha = input("digite a nova senha do aluno de pedagogia: ")
                        i.turma = input("digite a nova turma do aluno de pedagogia: ")
                        i.endereco = input("digite o novo endereço do aluno de pedagogia: ")
                        i.filiacoes = input("digite a nova filiação do aluno de pedagogia: ")
                        i.curso = input("digite o novo curso do aluno de pedagogia: ")
                        print("Aluno alterado com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True

            elif curso_aluno_superior == "ciencias da computacao":
                email_aluno_superior = input("Digite o email do aluno de ciencias da computacao: ")
                senha_aluno_superior = input("Digite a senha do aluno de ciencias da computacao: ")
                for i in alunos_superior:
                    if i.email == email_aluno_superior and i.senha == senha_aluno_superior:
                        i.email = input("digite o novo email do aluno de ciencias da computacao: ")
                        i.senha = input("digite a nova senha do aluno de ciencias da computacao: ")
                        i.turma = input("digite a nova turma do aluno de ciencias da computacao: ")
                        i.endereco = input("digite o novo endereço do aluno de ciencias da computacao: ")
                        i.filiacoes = input("digite a nova filiação do aluno de ciencias da computacao: ")
                        i.curso = input("digite o novo curso do aluno de ciencias da computacao: ")
                        print("Aluno alterado com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True
        else:
            print("Segmento informado invalido!")

    elif interacao2 == 2:
        segmento_professor=input("Digite o segmento do professor: ")
        if segmento_professor == "geral":
            email_professor_geral=input("Digite o email do professor: ")
            senha_professor_geral=input("Digite a senha do professor: ")
            for i in professores_geral:
                    if i.email == email_professor_geral and i.senha == senha_professor_geral:
                        i.formacoes = input("Digite a nova formação do professor: ")
                        i.turma = input("digite a nova turma do professor: ")
                        i.disciplinas = input("Digite a nova disciplina do professor: ")
                        i.email = input("digite o novo email do professor: ")
                        i.senha = input("digite a nova senha do professor: ")
                        print("Professor alterado com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True

        elif segmento_professor == "EM":
            email_professor_geral=input("Digite o email do professor: ")
            senha_professor_geral=input("Digite a senha do professor: ")
            for i in professores_geral:
                    if i.email == email_professor_geral and i.senha == senha_professor_geral:
                        i.formacoes = input("Digite a nova formação do professor: ")
                        i.turma = input("digite a nova turma do professor: ")
                        i.disciplinas = input("Digite a nova disciplina do professor: ")
                        i.email = input("digite o novo email do professor: ")
                        i.senha = input("digite a nova senha do aluno de professor: ")
                        print("Professor alterado com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True

        elif segmento_professor == "superior":
            email_professor_geral=input("Digite o email do professor: ")
            senha_professor_geral=input("Digite a senha do professor: ")
            for i in professores_geral:
                if i.email == email_professor_geral and i.senha == senha_professor_geral:
                    i.formacoes = input("Digite a nova formação do professor: ")
                    i.turma = input("digite a nova turma do professor: ")
                    i.disciplinas = input("Digite a nova disciplina do professor: ")
                    i.email = input("digite o novo email do professor: ")
                    i.senha = input("digite a nova senha do aluno de professor: ")
                    print("Professor alterado com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro1=True
        else:
            print("Erro! Formação informada invalida!")

    elif interacao2 == 3:
        tipo_disciplina=input("Digite qual o tipo da diciplina: ")
        if tipo_disciplina == "geral":
            nome_disciplinas=input("Qual o nome da disciplina: ")
            for i in disciplinas_gerais:
                if i.nome == nome_disciplinas:
                    i.id = input("id da disciplina: ")
                    i.nome = input("nome da disciplina: ")
                    i.descricao = input("descricao da disciplina: ")
                    i.segmento = input("segmento da disciplina: ")
                    i.professor_titular = input("professor titular da disciplina: ")
                    print("Disciplina alterada com sucesso!")
                else:
                    erro2=True

        elif tipo_disciplina == "ensino médio":
            nome_disciplinas=input("Qual o nome da disciplina: ")
            for i in disciplinas_EM:
                if i.nome == nome_disciplinas:
                    i.id = input("id da disciplina: ")
                    i.nome = input("nome da disciplina: ")
                    i.descricao = input("descricao da disciplina: ")
                    i.segmento = input("segmento da disciplina: ")
                    i.professor_titular = input("professor titular da disciplina: ")
                    print("Disciplina alterada com sucesso!")
                else:
                    erro2=True

        elif tipo_disciplina == "superior":
            nome_disciplinas=input("Qual o nome da disciplina: ")
            for i in disciplinas_superior:
                if i.nome == nome_disciplinas:
                    i.id = input("id da disciplina: ")
                    i.nome = input("nome da disciplina: ")
                    i.descricao = input("descricao da disciplina: ")
                    i.segmento = input("segmento da disciplina: ")
                    i.professor_titular = input("professor titular da disciplina: ")
                    print("Disciplina alterada com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro2=True
        else:
            print("Erro! Tipo da disciplina informada invalida!")
    
    elif interacao2 == 4:
        segmento_turma = input("Digite qual o segmento da turma: ")
        if segmento_turma == "EM":
            curso_turma_EM = input("Digite qual o curso da turma: ")
            ano_turma_EM = input("Digite o ano da turma: ")
            for i in turmas_EM:
                if i.curso == curso_turma_EM and i.ano == ano_turma_EM:
                    i.nome = input("nome da turma: ")
                    i.segmento = input("segmento da turma: ")
                    i.curso = input("Digite o curso da turma: ")
                    i.ano = input("Digite o ano da turma: ")
                    print("Turma alterada com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro2=True

        elif segmento_turma == "superior":
            curso_turma_superior = input("Digite qual o curso da turma: ")
            ano_turma_superior = input("Digite o ano da turma: ")
            for i in turmas_superior:
                if i.curso == curso_turma_superior and i.ano == ano_turma_superior:
                    i.nome = input("nome da turma: ")
                    i.segmento = input("segmento da turma: ")
                    i.curso = input("Digite o curso da turma: ")
                    i.ano = input("Digite o ano da turma: ")
                    print("Turma alterada com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro2=True
        else:
            print("Erro! Segmento informado invalido!")
    else:
        print("Erro! Opção escolhida invalida!")

elif interacao1 == 3:
    interacao2 = int(input("O que deseja desativar: \n 1: Aluno. \n 2: Professor. \n 3: Disciplina. \n 4: Turma. \n Escolha a interação: "))
    if interacao2 == 1:
        segmento_aluno = input("Digite qual o segmento do aluno: ")
        if segmento_aluno == "EM":
            curso_aluno_EM = input("Digite o curso do aluno do ensino médio: ")
            if curso_aluno_EM == "Informatica":
                email_aluno_EM = input("Digite o email do aluno de informática: ")
                senha_aluno_EM = input("Digite a senha do aluno de informática: ")
                for i in alunos_EM:
                    if i.email == email_aluno_EM and i.senha == senha_aluno_EM:
                        if i.status == True:
                            i.status = False
                            print("Status atualizados com sucesso!")
                            not_erro = True
                        else:
                            erro3=True
                    elif not_erro == False:
                        erro1=True

            elif curso_aluno_EM == "Mecatronica":
                email_aluno_EM = input("Digite o email do aluno de mecatrônica: ")
                senha_aluno_EM = input("Digite a senha do aluno de mecatrônica: ")
                for i in alunos_EM:
                    if i.email == email_aluno_EM and i.senha == senha_aluno_EM:
                        if i.status == True:
                            i.status = False
                            print("Status atualizados com sucesso!")
                            not_erro = True
                        else:
                            erro3=True
                    elif not_erro == False:
                        erro1=True
                    
            elif curso_aluno_EM == "Eletromecanica":
                email_aluno_EM = input("Digite o email do aluno de Eletromecanica: ")
                senha_aluno_EM = input("Digite a senha do aluno de Eletromecanica: ")
                for i in alunos_EM:
                    if i.email == email_aluno_EM and i.senha == senha_aluno_EM:
                        if i.status == True:
                            i.status = False
                            print("Status atualizados com sucesso!")
                            not_erro = True
                        else:
                            erro3=True
                    elif not_erro == False:
                        erro1=True
            else:
                print("Erro! Curso informado invalido!")

        elif segmento_aluno == "Superior":
            curso_aluno_superior = input("Digite o curso do aluno do curso superior: ")
            if curso_aluno_superior == "Pedagogia":
                email_aluno_superior = input("Digite o email do aluno de pedagogia: ")
                senha_aluno_superior = input("Digite a senha do aluno de pedagogia: ")
                for i in alunos_superior:
                    if i.email == email_aluno_superior and i.senha == senha_aluno_superior:
                        if i.status == True:
                            i.status = False
                            print("Status atualizados com sucesso!")
                            not_erro = True
                        else:
                            erro3=True
                    elif not_erro == False:
                        erro1=True

            elif curso_aluno_superior == "ciencias da computacao":
                email_aluno_superior = input("Digite o email do aluno de ciencias da computacao: ")
                senha_aluno_superior = input("Digite a senha do aluno de ciencias da computacao: ")
                for i in alunos_superior:
                    if i.email == email_aluno_superior and i.senha == senha_aluno_superior:
                        if i.status == True:
                            i.status = False
                            print("Status atualizados com sucesso!")
                            not_erro = True
                        else:
                            erro3=True
                    elif not_erro == False:
                        erro1=True
        else:
            print("Erro! Segmento informado invalido!")

    elif interacao2 == 2:
        segmento_professor=input("Digite o segmento do professor: ")
        if segmento_professor == "geral":
            email_professor_geral=input("Digite o email do professor: ")
            senha_professor_geral=input("Digite a senha do professor: ")
            for i in professores_geral:
                if i.email == email_professor_geral and i.senha == senha_professor_geral:
                    if i.status == True:
                        i.status = False
                        print("Status atualizados com sucesso!")
                        not_erro = True
                    else:
                        erro3=True
                elif not_erro == False:
                        erro1=True

        elif segmento_professor == "EM":
            email_professor_geral=input("Digite o email do professor: ")
            senha_professor_geral=input("Digite a senha do professor: ")
            for i in professores_geral:
                    if i.email == email_professor_geral and i.senha == senha_professor_geral:
                        if i.status == True:
                            i.status = False
                            print("Status atualizados com sucesso!")
                            not_erro = True
                        else:
                            erro3=True
                    elif not_erro == False:
                        erro1=True

        elif segmento_professor == "superior":
            email_professor_geral=input("Digite o email do professor: ")
            senha_professor_geral=input("Digite a senha do professor: ")
            for i in professores_geral:
                    if i.email == email_professor_geral and i.senha == senha_professor_geral:
                        if i.status == True:
                            i.status = False
                            print("Status atualizados com sucesso!")
                            not_erro = True
                        else:
                            erro3=True
                    elif not_erro == False:
                        erro1=True
        else:
            print("Erro! Formação do professor informada invalida!")

    elif interacao2 == 3:
        tipo_disciplina=input("Digite qual o tipo da diciplina: ")
        if tipo_disciplina == "geral":
            nome_disciplinas=input("Qual o nome da disciplina: ")
            for i in disciplinas_gerais:
                if i.nome == nome_disciplinas:
                    if i.status == True:
                        i.status = False
                        print("Status atualizados com sucesso!")
                        not_erro = True
                    else:
                        erro3=True
                elif not_erro == False:
                        erro2=True

        elif tipo_disciplina == "ensino médio":
            nome_disciplinas=input("Qual o nome da disciplina: ")
            for i in disciplinas_EM:
                if i.nome == nome_disciplinas:
                    if i.status == True:
                        i.status = False
                        print("Status atualizados com sucesso!")
                        not_erro = True
                    else:
                        erro3=True
                elif not_erro == False:
                        erro2=True

        elif tipo_disciplina == "superior":
            nome_disciplinas=input("Qual o nome da disciplina: ")
            for i in disciplinas_superior:
                if i.nome == nome_disciplinas:
                    if i.status == True:
                        i.status = False
                        print("Status atualizados com sucesso!")
                        not_erro = True
                    else:
                        erro3=True
                elif not_erro == False:
                        erro2=True
        else:
            print("Erro! Tipo de disciplina informada invalida!")

    elif interacao2 == 4:
        segmento_turma = input("Digite qual o segmento da turma: ")
        if segmento_turma == "EM":
            curso_turma_EM = input("Digite qual o curso da turma: ")
            ano_turma_EM = input("Digite o ano da turma: ")
            for i in turmas_EM:
                if i.curso == curso_turma_EM and i.ano == ano_turma_EM:
                    if i.status == True:
                        i.status = False
                        print("Status atualizados com sucesso!")
                        not_erro = True
                    else:
                        erro2 = True
                elif not_erro == False:
                    erro2=True

        elif segmento_turma == "superior":
            curso_turma_superior = input("Digite qual o curso da turma: ")
            ano_turma_superior = input("Digite o ano da turma: ")
            for i in turmas_superior:
                if i.curso == curso_turma_superior and i.ano == ano_turma_superior:
                    if i.status == True:
                        i.status = False
                        print("Status atualizados com sucesso!")
                        not_erro = True
                    else:
                        erro3 = True
                elif not_erro == False:
                    erro2=True
        else:
            print("Erro! Segmento informado invalido!")
    else:
        print("Erro! Opção escolhida invalida!")

elif interacao1 == 4:
    interacao2 = int(input("O que deseja excluir: \n 1: Aluno. \n 2: Professor. \n 3: Disciplina. \n 4: Turma. \n Escolha a interação: "))
    if interacao2 == 1:
        segmento_aluno = input("Digite qual o segmento do aluno: ")
        if segmento_aluno == "EM":
            curso_aluno_EM = input("Digite o curso do aluno do ensino médio: ")
            if curso_aluno_EM == "Informatica":
                email_aluno_EM = input("Digite o email do aluno de informática: ")
                senha_aluno_EM = input("Digite a senha do aluno de informática: ")
                for i in alunos_EM:
                    if i.email == email_aluno_EM and i.senha == senha_aluno_EM:
                        i.primeiro_nome = None
                        i.sobrenome = None
                        i.email = None
                        i.senha = None
                        i.status = None
                        i.turma = None
                        i.endereco = None
                        i.filiacoes = None
                        i.ra = None
                        i.segmento = None
                        i.curso = None
                        print("Aluno excluido com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True

            elif curso_aluno_EM == "Mecatronica":
                email_aluno_EM = input("Digite o email do aluno de mecatrônica: ")
                senha_aluno_EM = input("Digite a senha do aluno de mecatrônica: ")
                for i in alunos_EM:
                    if i.email == email_aluno_EM and i.senha == senha_aluno_EM:
                        i.primeiro_nome = None
                        i.sobrenome = None
                        i.email = None
                        i.senha = None
                        i.status = None
                        i.turma = None
                        i.endereco = None
                        i.filiacoes = None
                        i.ra = None
                        i.segmento = None
                        i.curso = None
                        print("Aluno excluido com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True
                    
            elif curso_aluno_EM == "Eletromecanica":
                email_aluno_EM = input("Digite o email do aluno de Eletromecanica: ")
                senha_aluno_EM = input("Digite a senha do aluno de Eletromecanica: ")
                for i in alunos_EM:
                    if i.email == email_aluno_EM and i.senha == senha_aluno_EM:
                        i.primeiro_nome = None
                        i.sobrenome = None
                        i.email = None
                        i.senha = None
                        i.status = None
                        i.turma = None
                        i.endereco = None
                        i.filiacoes = None
                        i.ra = None
                        i.segmento = None
                        i.curso = None
                        print("Aluno excluido com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True
            else:
                print("Curso informado invalido!")

        elif segmento_aluno == "Superior":
            curso_aluno_superior = input("Digite o curso do aluno do curso superior: ")
            if curso_aluno_superior == "Pedagogia":
                email_aluno_superior = input("Digite o email do aluno de pedagogia: ")
                senha_aluno_superior = input("Digite a senha do aluno de pedagogia: ")
                for i in alunos_superior:
                    if i.email == email_aluno_superior and i.senha == senha_aluno_superior:
                        i.primeiro_nome = None
                        i.sobrenome = None
                        i.email = None
                        i.senha = None
                        i.status = None
                        i.turma = None
                        i.endereco = None
                        i.filiacoes = None
                        i.ra = None
                        i.segmento = None
                        i.curso = None
                        print("Aluno excluido com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True

            elif curso_aluno_superior == "ciencias da computacao":
                email_aluno_superior = input("Digite o email do aluno de ciencias da computacao: ")
                senha_aluno_superior = input("Digite a senha do aluno de ciencias da computacao: ")
                for i in alunos_superior:
                    if i.email == email_aluno_superior and i.senha == senha_aluno_superior:
                        i.primeiro_nome = None
                        i.sobrenome = None
                        i.email = None
                        i.senha = None
                        i.status = None
                        i.turma = None
                        i.endereco = None
                        i.filiacoes = None
                        i.ra = None
                        i.segmento = None
                        i.curso = None
                        print("Aluno excluido com sucesso!")
                        not_erro = True
                    elif not_erro == False:
                        erro1=True
        else:
            print("Segmento informado invalido!")

    elif interacao2 == 2:
        segmento_professor=input("Digite o segmento do professor: ")
        if segmento_professor == "geral":
            email_professor_geral=input("Digite o email do professor: ")
            senha_professor_geral=input("Digite a senha do professor: ")
            for i in professores_geral:
                if i.email == email_professor_geral and i.senha == senha_professor_geral:
                    i.primeiro_nome = None
                    i.sobrenome = None
                    i.cpf = None
                    i.formacoes = None
                    i.turma = None
                    i.disciplinas = None
                    i.email = None
                    i.senha = None
                    i.status = None
                    print("Professor excluido com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro1=True

        elif segmento_professor == "EM":
            email_professor_geral=input("Digite o email do professor: ")
            senha_professor_geral=input("Digite a senha do professor: ")
            for i in professores_geral:
                if i.email == email_professor_geral and i.senha == senha_professor_geral:
                    i.primeiro_nome = None
                    i.sobrenome = None
                    i.cpf = None
                    i.formacoes = None
                    i.turma = None
                    i.disciplinas = None
                    i.email = None
                    i.senha = None
                    i.status = None
                    print("Professor excluido com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro1=True

        elif segmento_professor == "superior":
            email_professor_geral=input("Digite o email do professor: ")
            senha_professor_geral=input("Digite a senha do professor: ")
            for i in professores_geral:
                if i.email == email_professor_geral and i.senha == senha_professor_geral:
                    i.primeiro_nome = None
                    i.sobrenome = None
                    i.cpf = None
                    i.formacoes = None
                    i.turma = None
                    i.disciplinas = None
                    i.email = None
                    i.senha = None
                    i.status = None
                    print("Professor excluido com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro1=True
        else:
            print("Erro! Formação informada invalida!")

    elif interacao2 == 3:
        tipo_disciplina=input("Digite qual o tipo da diciplina: ")
        if tipo_disciplina == "geral":
            nome_disciplinas=input("Qual o nome da disciplina: ")
            for i in disciplinas_gerais:
                if i.nome == nome_disciplinas:
                    i.id = None
                    i.nome = None
                    i.descricao = None
                    i.segmento = None
                    i.professor_titular = None
                    i.status = None
                    print("Disciplina excluida com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro2=True

        elif tipo_disciplina == "ensino médio":
            nome_disciplinas=input("Qual o nome da disciplina: ")
            for i in disciplinas_EM:
                if i.nome == nome_disciplinas:
                    i.id = None
                    i.nome = None
                    i.descricao = None
                    i.segmento = None
                    i.professor_titular = None
                    i.status = None
                    print("Disciplina excluida com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro2=True

        elif tipo_disciplina == "superior":
            nome_disciplinas=input("Qual o nome da disciplina: ")
            for i in disciplinas_superior:
                if i.nome == nome_disciplinas:
                    i.id = None
                    i.nome = None
                    i.descricao = None
                    i.segmento = None
                    i.professor_titular = None
                    i.status = None
                    print("Disciplina excluida com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro2=True
        else:
            print("Erro! Tipo da disciplina informada invalida!")
    
    elif interacao2 == 4:
        segmento_turma = input("Digite qual o segmento da turma: ")
        if segmento_turma == "EM":
            curso_turma_EM = input("Digite qual o curso da turma: ")
            ano_turma_EM = input("Digite o ano da turma: ")
            for i in turmas_EM:
                if i.curso == curso_turma_EM and i.ano == ano_turma_EM:
                    i.nome = None
                    i.segmento = None
                    i.curso = None
                    i.ano = None
                    i.alunos = None
                    i.professores = None
                    i.disciplinas = None
                    i.status = None
                    print("Turma excluida com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro2=True

        elif segmento_turma == "superior":
            curso_turma_superior = input("Digite qual o curso da turma: ")
            ano_turma_superior = input("Digite o ano da turma: ")
            for i in turmas_superior:
                if i.curso == curso_turma_superior and i.ano == ano_turma_superior:
                    i.nome = None
                    i.segmento = None
                    i.curso = None
                    i.ano = None
                    i.alunos = None
                    i.professores = None
                    i.disciplinas = None
                    i.status = None
                    print("Turma excluida com sucesso!")
                    not_erro = True
                elif not_erro == False:
                    erro2=True
        else:
            print("Erro! Segmento informado invalido!")

    else:
        print("Erro! Opção escolhida invalida!")
else:
    print("Erro! Opção escolhida invalida!")

if erro1 == True:
    print("Erro! Email ou senha informada invalido!")
if erro2 == True:
    print("Erro! Nome informado invalido!")
if erro3 == True:
    print("Erro! O segmento informado já esta desativado!")