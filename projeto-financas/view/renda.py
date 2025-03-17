# gerenciador_renda.py
class GerenciadorDeRenda:
    def __init__(self):
        self.receitas = []
        self.despesas = []

    def adicionar_receita(self, descricao, valor):  # Atualizado
        self.receitas.append({"descricao": descricao, "valor": valor})
        print(f"Receita adicionada: {descricao} - R${valor:.2f}\n")

    def adicionar_despesa(self, descricao, valor):  # Atualizado
        self.despesas.append({"descricao": descricao, "valor": valor})
        print(f"Despesa adicionada: {descricao} - R${valor:.2f}\n")

    def calcular_total_receitas(self):
        return sum([receita['valor'] for receita in self.receitas])

    def calcular_total_despesas(self):
        return sum([despesa['valor'] for despesa in self.despesas])

    def calcular_saldo(self):
        total_receitas = self.calcular_total_receitas()
        total_despesas = self.calcular_total_despesas()
        return total_receitas - total_despesas

    def gerar_relatorio(self):
        print("\n--- Relatório Financeiro ---")
        print("Receitas:")
        for receita in self.receitas:
            print(f"{receita['descricao']}: R${receita['valor']:.2f}")
        
        print("\nDespesas:")
        for despesa in self.despesas:
            print(f"{despesa['descricao']}: R${despesa['valor']:.2f}")
        
        saldo = self.calcular_saldo()
        print(f"\nSaldo final: R${saldo:.2f}")
        
        if saldo >= 0:
            print("Parabéns! Você está com superávit.")
        else:
            print("Atenção! Você está com déficit.")
