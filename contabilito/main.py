from datetime import date
from domain.contabilidade import contabilidade as ctb

def main():
    debito = ctb.TipoPartida.DEBITO
    credito = ctb.TipoPartida.CREDITO

    conta_estoque = ctb.Conta('1', 'Estoque')
    conta_fornecedores = ctb.Conta('2', 'Fornecedor')

    compra_mercadoria = ctb.EventoEconomicoFactory("Compra de Mercadorias para Revenda")
    compra_mercadoria.registrar_modelo_partida(debito, conta_estoque)
    compra_mercadoria.registrar_modelo_partida(credito, conta_fornecedores)

    lcto = compra_mercadoria.contabilizar(date.today(), 15000)

    diario = ctb.Diario()
    diario.registra(lcto)

    print(diario)

if __name__ == "__main__":
    main()