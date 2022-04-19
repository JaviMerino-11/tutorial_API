from aiohttp import web
from instructions.get_handler import get_handler
from instructions.put_handler import put_handler

routes = web.RouteTableDef()


@routes.get('/')
async def saludo_get(request):
    return get_handler


@routes.put('/put')
async def saludo_put(request):
    return put_handler


app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
