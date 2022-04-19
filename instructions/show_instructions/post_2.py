from aiohttp import web


async def post_2(request):
    return web.Response(text="Estas en el mismo endline (path2) pero en post")
