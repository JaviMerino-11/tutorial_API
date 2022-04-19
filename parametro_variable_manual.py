from aiohttp import web


async def saludo(request):
    return web.Response(text='Bienvenido, {}'.format(request.match_info['name']))


async def cola(request):
    return web.Response(text='Pa ti mi cola, {}'.format(request.match_info['cola']))


app = web.Application()
app.add_routes(
    [
        web.get('/{name}', saludo),
        web.put('/{cola}', cola)
    ]
)

if __name__ == '__main__':
    web.run_app(app)

# El nombre que pongamos después de / será lo que nos devuelva el servidor -- Si pongo /javi -- Bienvenido, Javi y así
# con el valor que pongamos.
