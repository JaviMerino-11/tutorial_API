from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def saludo(request):
    return web.Response(text="Hola mundo")


@routes.put('/help')
async def ayuda(request):
    return web.Response(text="Welcome to the Help site")


app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
