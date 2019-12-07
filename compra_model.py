import faust

class ItemCompra(faust.Record):
    produto: str
    qtd: int