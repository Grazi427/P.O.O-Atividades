campus_list = []

class Curso:
    # Representa um curso oferecido por um campus
    def __init__(self, nome, duracao_semestres):
        self.nome = nome
        self.duracao_semestres = duracao_semestres

    def __str__(self):
        return f"Curso: {self.nome} ({self.duracao_semestres} semestres)"


class Campus:
    # Representa um campus da universidade com seus cursos
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.cursos = []
        
    def encontrar_curso(self, nome_curso):
        # Auxiliar para buscar um Curso na lista por nome
        for curso in self.cursos:
            if curso.nome == nome_curso:
                return curso
        return None

    def adicionar_curso(self, curso):
        # Adiciona um objeto Curso à lista de cursos
        self.cursos.append(curso)

    def remover_curso(self, nome_curso):
        # Remove um curso pelo nome, iterando pela lista
        curso_para_remover = self.encontrar_curso(nome_curso)
        if curso_para_remover:
            self.cursos.remove(curso_para_remover)
            return True
        return False

    def __str__(self):
        # Percorre a lista de cursos para a string de exibição
        cursos_str = "\n    ".join(str(curso) for curso in self.cursos)
        if not cursos_str:
            cursos_str = "Nenhum curso cadastrado."
            
        return (
            f"---- Campus: {self.nome} ----\n"
            f"  Endereço: {self.endereco}\n"
            f"  Cursos:\n    {cursos_str}"
        )

def encontrar_campus(nome_campus):
    # Auxiliar para buscar um Campus na lista global por nome
    for campus in campus_list:
        if campus.nome == nome_campus:
            return campus
    return None

def adicionar_campus():
    # Adiciona um novo campus ao sistema
    print("\n--- Adicionar Novo Campus ---")
    nome = input("Nome do Campus: ").strip()
    if not nome:
        print("O nome do campus não pode ser vazio.")
        return
        
    # Busca na lista se o nome já existe
    if encontrar_campus(nome):
        print(f"O Campus '{nome}' já existe.")
        return
        
    endereco = input("Endereço do Campus: ").strip()
    
    novo_campus = Campus(nome, endereco)
    # Adiciona à lista
    campus_list.append(novo_campus)
    print(f"Campus '{nome}' adicionado com sucesso!")

def visualizar_campus():
    # Exibe todos os campus e seus cursos (iterando pela lista)
    print("\n--- Campus Cadastrados ---")
    if not campus_list:
        print("Nenhum campus cadastrado.")
        return
        
    for campus in campus_list:
        print("---")
        print(campus)
    print("---")

def editar_campus():
    # Edita o endereço de um campus existente
    visualizar_campus()
    if not campus_list:
        return
        
    print("\n--- Editar Campus ---")
    nome = input("Digite o nome do Campus que deseja editar: ").strip()
    
    campus_encontrado = encontrar_campus(nome)
    
    if campus_encontrado:
        print(f"Campus selecionado: {campus_encontrado.nome} (Endereço atual: {campus_encontrado.endereco})")
        novo_endereco = input("Digite o NOVO endereço (ou deixe vazio para manter o atual): ").strip()
        
        if novo_endereco:
            campus_encontrado.endereco = novo_endereco
            print(f"Endereço do Campus '{nome}' atualizado para: {novo_endereco}")
        else:
            print("Nenhuma alteração de endereço realizada.")
    else:
        print(f"Campus '{nome}' não encontrado.")

def excluir_campus():
    # Exclui um campus do sistema (removendo da lista)
    visualizar_campus()
    if not campus_list:
        return
        
    print("\n--- Excluir Campus ---")
    nome = input("Digite o nome do Campus que deseja EXCLUIR: ").strip()
    
    campus_para_excluir = encontrar_campus(nome)
    
    if campus_para_excluir:
        confirmacao = input(f"Tem certeza que deseja excluir o Campus '{nome}' e todos os seus cursos? (s/n): ").lower().strip()
        if confirmacao == 's':
            # Remove o objeto Campus da lista
            campus_list.remove(campus_para_excluir)
            print(f"Campus '{nome}' excluído com sucesso!")
        else:
            print(f"Exclusão do Campus '{nome}' cancelada.")
    else:
        print(f"Campus '{nome}' não encontrado.")


def selecionar_campus(select):
    # Auxiliar para selecionar um campus para ações de curso.
    visualizar_campus()
    if not campus_list:
        print("Por favor, adicione um campus primeiro.")
        return None
        
    print(f"\n--- {select} Curso ---")
    nome_campus = input("Digite o nome do Campus onde o curso será gerenciado: ").strip()
    
    return encontrar_campus(nome_campus)

def adicionar_curso():
    # Adiciona um novo curso a um campus
    campus = selecionar_campus("Adicionar")
    if not campus:
        return
        
    nome_curso = input("Nome do Novo Curso: ").strip()
    if not nome_curso:
        print("O nome do curso não pode ser vazio.")
        return
        
    # Verifica a existência na lista de cursos do campus
    if campus.encontrar_curso(nome_curso):
        print(f"O Curso '{nome_curso}' já existe no Campus '{campus.nome}'.")
        return
        
    while True:
        try:
            duracao = int(input("Duração em Semestres: ").strip())
            if duracao <= 0:
                print("A duração deve ser um número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número inteiro para a duração.")
            
    novo_curso = Curso(nome_curso, duracao)
    campus.adicionar_curso(novo_curso)
    print(f"Curso '{nome_curso}' adicionado ao Campus '{campus.nome}' com sucesso!")

def editar_curso():
    # Edita o nome ou duração de um curso
    campus = selecionar_campus("Editar")
    if not campus:
        return

    if not campus.cursos:
        print(f"O Campus '{campus.nome}' não possui cursos para editar.")
        return

    print("\nCursos existentes neste campus:")
    # Itera pela lista de cursos
    for curso in campus.cursos:
        print(f"- {curso}")
        
    nome_curso_antigo = input("Digite o nome do Curso que deseja editar: ").strip()
    
    curso_encontrado = campus.encontrar_curso(nome_curso_antigo)
    
    if curso_encontrado:
        print(f"\nCurso selecionado: {curso_encontrado.nome} (Duração atual: {curso_encontrado.duracao_semestres} semestres)")
        
        # Editar Nome
        novo_nome = input("Digite o NOVO nome do curso (ou deixe vazio para manter): ").strip()
        if novo_nome and novo_nome != nome_curso_antigo:
            # Verifica se o novo nome já existe
            if campus.encontrar_curso(novo_nome):
                print(f"O nome '{novo_nome}' já está em uso. Alteração de nome cancelada.")
                return
            
            # Basta atualizar o atributo nome no objeto Curso
            curso_encontrado.nome = novo_nome
            print(f"Nome do curso alterado de '{nome_curso_antigo}' para '{novo_nome}'.")
            
        # Editar Duração
        while True:
            nova_duracao_str = input(f"Digite a NOVA duração em semestres (atual: {curso_encontrado.duracao_semestres}, ou deixe vazio para manter): ").strip()
            if not nova_duracao_str:
                break
            try:
                nova_duracao = int(nova_duracao_str)
                if nova_duracao > 0:
                    curso_encontrado.duracao_semestres = nova_duracao
                    print(f"Duração do curso '{curso_encontrado.nome}' atualizada para {nova_duracao} semestres.")
                    break
                else:
                    print("A duração deve ser um número positivo.")
            except ValueError:
                print("Por favor, digite um número inteiro ou deixe vazio.")
    else:
        print(f"Curso '{nome_curso_antigo}' não encontrado no Campus '{campus.nome}'.")

def excluir_curso():
    # Exclui um curso de um campus
    campus = selecionar_campus("Excluir")
    if not campus:
        return
        
    if not campus.cursos:
        print(f"O Campus '{campus.nome}' não possui cursos para excluir.")
        return

    print("\nCursos existentes neste campus:")
    for curso in campus.cursos:
        print(f"- {curso}")

    nome_curso = input("Digite o nome do Curso que deseja EXCLUIR: ").strip()
    
    # Chama o método que remove da lista
    if campus.remover_curso(nome_curso):
        print(f"Curso '{nome_curso}' excluído do Campus '{campus.nome}' com sucesso!")
    else:
        print(f"Curso '{nome_curso}' não encontrado no Campus '{campus.nome}'.")


def exibir_menu():
    # Exibe o menu de opções
    print("\n" + "="*40)
    print("Sistema de Gestão Universitária da UFC")
    print("="*40)
    print("\n--- Gerenciamento de Campus ---")
    print("1. Adicionar Campus")
    print("2. Visualizar campus")
    print("3. Editar Campus (Endereço)")
    print("4. Excluir Campus")
    print("\n--- Gerenciamento de Cursos ---")
    print("5. Adicionar Curso")
    print("6. Editar Curso (Nome/Duração)")
    print("7. Excluir Curso")
    print("0. Sair")
    print("="*40)

def main():
    # Função principal que executa o menu
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            adicionar_campus()
        elif escolha == '2':
            visualizar_campus()
        elif escolha == '3':
            editar_campus()
        elif escolha == '4':
            excluir_campus()
        elif escolha == '5':
            adicionar_curso()
        elif escolha == '6':
            editar_curso()
        elif escolha == '7':
            excluir_curso()
        elif escolha == '0':
            print("Obrigado por usar o sistema! Encerrando...")
            return exit()
        else:
            print("Opção inválida. Por favor, tente novamente.")
        main()



#  Inicialização com dados de exemplo (opcional)
print("\n" + "="*80)
exemplo=input('Deseja inicializar o sistema com campus e cursos de exemplo já cadastrados? (s/n) \n').lower
print('\n',"="*80,'\n')

if exemplo=='s'.lower:
    print('Exemplos adicionados com sucesso! Os seguintes exemplos foram adicionados:\n',"-"*70,'\n' \
    '- Campus do Pici - Fortaleza, Av. da Universidade, sn\n'
    '- Cursos: Direito e Medicina' \
    '','\n',"-"*70,\
    '\n- Campus do Benfica - Fortaleza, Av. da Universidade, sn' \
    '\n- Cursos: Engenharia de Software e Ciência de Dados\n')
    campus_1 = Campus("Campus do Pici - Fortaleza", "Av. da Universidade, sn")
    campus_2 = Campus("Campus do Benfica - Fortaleza", "Av. da Universidade, sn")

    campus_1.adicionar_curso(Curso("Direito", 10))
    campus_1.adicionar_curso(Curso("Medicina", 12))
    campus_2.adicionar_curso(Curso("Engenharia de Software", 8))
    campus_2.adicionar_curso(Curso("Ciência de Dados", 6))

    campus_list.append(campus_1)
    campus_list.append(campus_2)


elif exemplo=='n':
    print('Ok! o sistema iniciará sem nenhum campus ou curso cadastrado\n')

main()

