from aiohttp import web


async def get_1(request):
    return web.Response(text="Estas en el mismo endline (path1) pero en get")
