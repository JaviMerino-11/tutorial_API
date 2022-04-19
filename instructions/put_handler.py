from aiohttp import web


async def put_handler(request):
    return web.Response(text="Bienvenido a la pagina de put!!!")
