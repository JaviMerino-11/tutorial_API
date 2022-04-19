from aiohttp import web


async def saludo(request):
    return web.Response(text="Hola mundo")


async def ayuda(request):
    return web.Response(text="Bienvenido a la zona de ayuda")


app = web.Application()
app.add_routes([
    web.get('/', saludo),
    web.put('/help', ayuda)
]

)

if __name__ == '__main__':
    web.run_app(app)
