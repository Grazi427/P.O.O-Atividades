import contas
class Banco:

    def __init__(self, nome: str, numero_banco: str, agencia: str):
        self._nome = nome
        self._numero_banco = numero_banco
        self._agencia = agencia
        self._contas = {}

    def adicionar_conta(self, numero: int, titular: str, saldo_inicial: float = 0.0) -> contas.Conta:
        if numero in self._contas:
            return (f"Erro: Conta com número {numero} já existe.")

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
                f"Transferência de R$ {valor:.2f} de {origem.numero()} para {destino.numero()} realizada com sucesso.")
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
        print('valor creditado a conta com sucesso')
        return True

    def debitar(self, numero_destino: int, valor: float) -> bool:
        destino = self.buscar_conta(numero_destino)

        if not destino:
            print("Erro na transferência: Conta de destino não encontrada.")
            return False

        if valor <= 0:
            print("Erro: Valor deve ser positivo para débito.")
            return False
        destino.debitar(valor)
        print('valor debitado da conta com sucesso')
        return True

    def excluir_conta(self, numero: int):
        if numero in self._contas:
            saldo = self._contas[numero].saldo()
            if saldo != 0.0:
                print(f"Erro: Não é possível excluir a conta {numero}. Saldo pendente de R$ {saldo:.2f}.")
                return
            del self._contas[numero]
            print(f"Conta {numero} excluída com sucesso.")
        else:
            print(f"Erro: Conta {numero} não encontrada para exclusão.")

# --- Exemplo de Uso ---

# 1. Criação do Banco
meu_banco = Banco(nome="Ordo Realitas", numero_banco="800", agencia="0001")

# 2. Adicionar Contas
conta101 = meu_banco.adicionar_conta(numero=101, titular="Arthu Cervero", saldo_inicial=1000.00)
conta102 = meu_banco.adicionar_conta(numero=102, titular="César oliveira Cohen", saldo_inicial=500.50)
conta103 = meu_banco.adicionar_conta(numero=103, titular="Joui Jouki", saldo_inicial=20000.00)

# 3. Mostrar contas
print("-" * 30)
print(f"Banco: {meu_banco._nome} | Agência: {meu_banco._agencia}")
print(f"Saldo da Conta 101: R$ {conta101.saldo():.2f}")
print(f"Saldo da Conta 102: R$ {conta102.saldo():.2f}")
print(f"Saldo da Conta 103: R$ {conta103.saldo():.2f}")
print("-" * 30)

# 4. Testar Operações na Conta
# conta101.creditar(200.00)
# conta102.debitar(50.00)
# print(f"Novo Saldo 101: R$ {conta101.saldo():.2f}")
# print(f"Novo Saldo 102: R$ {conta102.saldo():.2f}")
# print("-" * 30)

# 5. Testar Transferência
# meu_banco.transferir(numero_origem=101, numero_destino=102, valor=300.00)
# print(f"Saldo 101 após Transferência: R$ {conta101.saldo():.2f}")
# print(f"Saldo 102 após Transferência: R$ {conta102.saldo():.2f}")
# print("-" * 30)

# 6. Testar Saldo Total
# total = meu_banco.saldo_total()
# print(f"Saldo Total do Banco: R$ {total:.2f}")
# print("-" * 30)

# 7. Testar Busca e Exclusão
# conta_busca = meu_banco.buscar_conta(101)
# if conta_busca:
#     print(f"Conta encontrada: {conta_busca}")

# Excluir conta 102 (que tem saldo) - Deve falhar
# meu_banco.excluir_conta(102)

# Transferir o restante da 101 para zerar a 101
# restante = conta101.saldo()
# meu_banco.transferir(101, 102, restante)

# Excluir conta 101 (agora zerada)
# meu_banco.excluir_conta(101)
# print("-" * 30)

# 8. Saldo Total após exclusões
# total_apos_exclusao = meu_banco.saldo_total()
# print(f"Saldo Total do Banco após exclusões: R$ {total_apos_exclusao:.2f}")