from aiohttp import web
from instructions.show_instructions.get_1 import get_1
from instructions.show_instructions.get_2 import get_2
from instructions.show_instructions.post_1 import post_1
from instructions.show_instructions.post_2 import post_2



app = web.Application()
app.add_routes(
    [
        web.get('/path1', get_1),
        web.post('/path1', post_1),
        web.get('/path2', get_2),
        web.post('/path2', post_2)
    ]
)

if __name__ == '__main__':
    web.run_app(app)
