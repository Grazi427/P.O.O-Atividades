import contas

class Banco:

    def __init__(self, nome: str, numero_banco: str, agencia: str):
        self._nome = nome
        self._numero_banco = numero_banco
        self._agencia = agencia
        self._contas = {} # Dicionário de contas {numero: conta}

    def nome(self) -> str:
        return self._nome
        
    def adicionar_conta(self, numero: int, titular: str, saldo_inicial: float = 0.0) -> contas.Conta:
        if numero in self._contas:
            # Retorna a conta existente (ou uma mensagem de erro, dependendo do design)
            print(f"Erro: Conta com número {numero} já existe.")
            return self._contas[numero]

        nova_conta = contas.Conta(numero, titular, saldo_inicial)
        self._contas[numero] = nova_conta
        return nova_conta

    def buscar_conta(self, numero: int):
        return self._contas.get(numero)

    def transferir(self, numero_origem: int, numero_destino: int, valor: float) -> bool:
        origem = self.buscar_conta(numero_origem)
        destino = self.buscar_conta(numero_destino)

        if not origem or not destino:
            print("Erro na transferência: Conta de origem ou destino não encontrada.")
            return False

        if valor <= 0:
            print("Erro na transferência: O valor deve ser positivo.")
            return False

        if origem.debitar(valor):
            destino.creditar(valor)
            print(
                f"Transferência de R$ {valor:.2f} de {origem.numero()} para {destino.numero()} realizada com sucesso no Banco {self._nome}.")
            return True
        else:
            print(f"Erro na transferência: Saldo insuficiente na conta {origem.numero()}.")
            return False

    def saldo_total(self):
        return sum(conta.saldo() for conta in self._contas.values())

    def creditar(self, numero_destino: int, valor: float) -> bool:
        destino = self.buscar_conta(numero_destino)

        if not destino:
            print("Erro na transferência: Conta de destino não encontrada.")
            return False

        if valor <= 0:
            print("Erro: Valor deve ser positivo para crédito.")
            return False
        destino.creditar(valor)
        print(f'Valor R$ {valor:.2f} creditado na conta {destino.numero()} com sucesso no Banco {self._nome}.')
        return True

    def debitar(self, numero_destino: int, valor: float) -> bool:
        destino = self.buscar_conta(numero_destino)

        if not destino:
            print("Erro na transferência: Conta de destino não encontrada.")
            return False

        if valor <= 0:
            print("Erro: Valor deve ser positivo para débito.")
            return False
        
        if destino.debitar(valor):
            print(f'Valor R$ {valor:.2f} debitado da conta {destino.numero()} com sucesso no Banco {self._nome}.')
            return True
        else:
            print(f"Erro no débito: Saldo insuficiente na conta {destino.numero()}.")
            return False


    def excluir_conta(self, numero: int):
        if numero in self._contas:
            saldo = self._contas[numero].saldo()
            if saldo != 0.0:
                print(f"Erro: Não é possível excluir a conta {numero}. Saldo pendente de R$ {saldo:.2f}.")
                return
            del self._contas[numero]
            print(f"Conta {numero} excluída com sucesso do Banco {self._nome}.")
        else:
            print(f"Erro: Conta {numero} não encontrada para exclusão no Banco {self._nome}.")

# --- Adição da Lista de Bancos (Dicionário) ---
# Usamos um dicionário para poder buscar um banco rapidamente pelo seu nome ou número.
# Chave: Nome do Banco | Valor: Instância da Classe Banco
bancos_registrados = {} 

def adicionar_banco(banco: Banco):
    # Adiciona uma instância de Banco ao dicionário global.
    if banco.nome() in bancos_registrados:
        print(f"Atenção: Banco '{banco.nome()}' já está registrado. Ignorando a adição.")
        return
    bancos_registrados[banco.nome()] = banco
    print(f"Banco '{banco.nome()}' registrado com sucesso.")

# --- Exemplo de Uso (Atualizado) ---

# 1. Criação e Registro dos Bancos
banco_ordem = Banco(nome="Ordo Realitas", numero_banco="800", agencia="0001")
adicionar_banco(banco_ordem)

banco_kaiser = Banco(nome="Kaiser Bank", numero_banco="999", agencia="0001")
adicionar_banco(banco_kaiser)

# 2. Adicionar Contas ao Banco 'Ordo Realitas'
print("\n--- Adicionando Contas ao Ordo Realitas ---")
conta101 = banco_ordem.adicionar_conta(numero=101, titular="Arthu Cervero", saldo_inicial=1000.00)
conta102 = banco_ordem.adicionar_conta(numero=102, titular="César oliveira Cohen", saldo_inicial=500.50)

# 3. Adicionar Contas ao Banco 'Kaiser Bank'
print("\n--- Adicionando Contas ao Kaiser Bank ---")
conta201 = banco_kaiser.adicionar_conta(numero=201, titular="Liz Weber", saldo_inicial=15000.00)
conta202 = banco_kaiser.adicionar_conta(numero=202, titular="Thiago Fritz", saldo_inicial=5000.00)

# 4. Mostrar Contas e Saldo Total por Banco
print("\n" + "=" * 50)
print(f"| {'RESUMO DOS BANCOS REGISTRADOS':^48} |")
print("=" * 50)

for nome, banco in bancos_registrados.items():
    print(f"| 🏦 Banco: {nome:<38} |")
    print(f"| Saldo Total: R$ {banco.saldo_total():<30.2f} |")
    print("-" * 50)

# 5. Testar Transferência Interna no Ordo Realitas
print("\n--- Teste de Transferência Interna (Ordo Realitas) ---")
banco_ordem.transferir(numero_origem=101, numero_destino=102, valor=300.00)
print(f"Saldo {banco_ordem.nome()} Conta 101: R$ {banco_ordem.buscar_conta(101).saldo():.2f}")
print(f"Saldo {banco_ordem.nome()} Conta 102: R$ {banco_ordem.buscar_conta(102).saldo():.2f}")

# 6. Testar Operações no Kaiser Bank
print("\n--- Teste de Crédito/Débito (Kaiser Bank) ---")
banco_kaiser.creditar(numero_destino=201, valor=500.00)
banco_kaiser.debitar(numero_destino=202, valor=1000.00)
print(f"Saldo {banco_kaiser.nome()} Conta 201: R$ {banco_kaiser.buscar_conta(201).saldo():.2f}")
print(f"Saldo {banco_kaiser.nome()} Conta 202: R$ {banco_kaiser.buscar_conta(202).saldo():.2f}")