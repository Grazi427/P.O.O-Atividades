class Conta:

    def __init__(self, numero: int, titular: str, saldo_inicial: float = 0.0):
        if saldo_inicial < 0:
            print("O saldo inicial não pode ser negativo.")
        self._numero = numero
        self._titular = titular
        self._saldo = saldo_inicial

    def creditar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
            print("Transação bem-sucedida")
            return True
        else:
            print("Não foi possivel realizar a transação")
        return False

    def debitar(self, valor: float) -> bool:
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print("Transação bem-sucedida")
            return True
        else:
            print("Não foi possivel realizar a transação")
        return False

    def numero(self):
        return self._numero

    def titular(self):
        return self._titular

    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"Conta(Nº: {self._numero}, Titular: {self._titular}, Saldo: R$ {self._saldo:.2f})"
