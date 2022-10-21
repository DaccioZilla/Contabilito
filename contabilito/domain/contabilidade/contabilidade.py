from dataclasses import dataclass
from enum import Enum
from datetime import date
from abc import ABC, abstractmethod
from typing import List, Tuple

class TipoPartida(Enum):
    DEBITO = 0
    CREDITO = 1

@dataclass
class Conta:
    codigo: str
    descricao: str

@dataclass
class Partida:
    tipo: TipoPartida
    conta: Conta
    valor: float

@dataclass
class Lancamento:
    data: date
    partidas: List[Partida]
    historico: str

class Diario:
    def __init__(self):
        self.registros: List[Lancamento] = []

    def registra(self, lancamento: Lancamento):
        self.registros.append(lancamento)

    def __repr__(self):
        lista_partidas = [f'{"DATA":^12}{"Tipo":^10}{"Conta":^37}{"Historico":^50}{"Valor":^20}']
        for lancamento in self.registros:
            for partida in lancamento.partidas:
                texto_partida = f'{lancamento.data.day:02}/{lancamento.data.month:02}/{lancamento.data.year:<6}{partida.tipo.name:<10}{partida.conta.codigo:>10} - {partida.conta.descricao:<25}{lancamento.historico:<50}{partida.valor:>20,.2f}'
                lista_partidas.append(texto_partida)
        return '\n'.join(lista_partidas)


class EventoEconomicoFactory:

    def __init__(self, nome_evento:str):
        self.nome = nome_evento
        self.modelos_partida: List[Tuple[TipoPartida, Conta]] = []

    def registrar_modelo_partida(self, tipo_partida: TipoPartida , conta: Conta):
        self.modelos_partida.append((tipo_partida, conta))

    def remover_modelo_partida(self, modelo_partida_registrado):
        if modelo_partida_registrado in self.modelos_partida:
            self.modelo_partida.remove(partida_registrada)

    def registrar_varios_modelos_partida(self, modelos_partida: List[Tuple[TipoPartida, Conta]]):
        self.modelos_partida.extend(modelos_partida)

    def remover_varios_modelos_partida(self, modelos_partida: List[Tuple[TipoPartida, Conta]]):
        for modelo in modelos_partida:
            self.remover_modelo_partida(modelo)

    def contabilizar(self, data: date, valor):
        partidas = [Partida(tipo, conta, valor) for tipo, conta in self.modelos_partida]
        return Lancamento(data, partidas, self.nome)



        

