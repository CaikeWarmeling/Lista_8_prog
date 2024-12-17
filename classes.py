class Pessoa:
    def __init__(self, primeiro_nome, sobrenome, turma, email, senha, status):
        self.primeiro_nome=primeiro_nome
        self.sobrenome=sobrenome
        self.turma=turma
        self.email=email
        self.senha=senha
        self.status=status

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha

class Aluno(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, email, senha, status, turma, endereco, filiacoes, ra, segmento, curso):
        super().__init__(primeiro_nome, sobrenome, turma, email, senha, status)
        self.endereco = endereco 
        self.filiacoes = filiacoes
        self.ra = ra
        self.segmento = segmento
        self.curso = curso

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @property
    def ra(self):
        return self.__ra

    @ra.setter
    def ra(self, novo_ra):
        self.__ra = novo_ra

class Professor(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, cpf, formacao, turmas, disciplinas, email, senha, status):
        super().__init__(primeiro_nome, sobrenome, turmas, email, senha, status)
        self.cpf = cpf
        self.formacao = formacao
        self.disciplinas = disciplinas

    @property
    def cpf(self):
        return self.__cpf
        
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

class Turma:
    def __init__(self, nome, segmento, curso, ano, alunos, professores, disciplinas, status):
        self.nome=nome
        self.segmento=segmento
        self.curso=curso
        self.ano=ano
        self.alunos=alunos
        self.professores=professores
        self.disciplinas=disciplinas
        self.status=status

class Disciplina:
    def __init__(self, id, nome, descricao, segmento, professor_titular, status):
        self.id=id
        self.nome=nome
        self.descricao=descricao
        self.segmento=segmento
        self.professor_titular=professor_titular
        self.status=status

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, novo_id):
        self.__id = novo_id