from aiohttp import web
from instructions.arithmetic_functions.basic_ones import *


class Handler:

    def __init__(self):
        pass

    async def sumatorio_json(self, request):
        data = {'Resultado': sumatorio(5, 10)}
        return web.json_response(data)

    async def productorio_json(self, request):
        data = {'Resultado': productorio(10, 10)}
        return web.json_response(data)


handler = Handler()
app = web.Application()
app.add_routes(
    [
        web.get('/intro', handler.sumatorio_json),
        web.put('/intro', handler.productorio_json)
    ]
)

if __name__ == '__main__':
    web.run_app(app)
