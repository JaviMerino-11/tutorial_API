from aiohttp import web


async def post_1(request):
    return web.Response(text="Estas en el mismo endline (path1) pero en post")
