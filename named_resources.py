from aiohttp import web



routes = web.RouteTableDef()


@routes.get('/root', name='root')
async def handler(request):
    return web.Response(text='Whats up?')


url = request.app.router['user-info'].url_for(user='john_doe')
url_with_qs = url.with_query("a=b")
assert url_with_qs == '/john_doe/info?a=b'

app = web.Application()

app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
