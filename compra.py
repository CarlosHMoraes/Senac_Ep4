import faust
import json
from datetime import timedelta
from random import randrange

class ItemCompra(faust.Record, serializer='json'):
    produto: str
    qtd: int
    valor: float

app = faust.App(
    'compras',
    broker='kafka://kafka:9092'
)

compra_topic = app.topic('comprasE', value_type=ItemCompra)
rs_table = app.Table('rsE', default=int).hopping(60,120, expires=timedelta(minutes=10), key_index=True)
qtd_table = app.Table('qtdE', default=int).tumbling(timedelta(minutes=2),expires=timedelta(hours=1))

@app.agent(compra_topic)
async def contar_rs_qtd_venda(info):
    async for compra in info:
        dados = json.loads(compra)
        rs_table['valor_1min'] += (dados.valor * dados.qtd)
        qtd_table['qtd_2_min'] += dados.qtd

#@app.timer(interval=1.0)
#async def exemplo_compra(app):
#    await contar_rs_qtd_venda.send(
#        value=ItemCompra(produto='arroz',qtd=randrange,valor='5.75')
#    )

#@app.timer(2.0, on_leader=True)
#async def comprar():
#    valor = ItemCompra(produto='feijao',qtd=randrange,valor='4.29')
#    await contar_rs_qtd_venda.send(value=valor)

#if __name__ == '__main__':
#    app.main()   

@app.page('/rs_1_min/{page}')
@app.table_route(table=rs_table, match_info='page')
async def get_rs(web, request, page):
    return web.json({
        page: rs_table[page],
    })

@app.page('/qtd_2_min/{page}')
@app.table_route(table=qtd_table, match_info='page')
async def get_qtd(web, request, page):
    return web.json({
        page: qtd_table[page],
    })

