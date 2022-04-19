from aiohttp import web


async def get_2(request):
    return web.Response(text="Estas en el mismo endline (path2) pero en get")
