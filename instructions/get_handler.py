from aiohttp import web


async def get_handler(request):
    return web.Response(text="Bienvenido a la pagina de get!!!!")
