import asyncio
import time

from aiohttp import web


async def show_post_query(request):

    print('-')

    # for sync
    # time.sleep(1.0)

    # for async
    await asyncio.sleep(2.0)

    request_json = await request.json()
    text = request_json.get('query')
    print(text)
    return web.Response(text=text)

loop = asyncio.get_event_loop()
app = web.Application(loop=loop, debug=True)
app.router.add_route('POST', '/yo', show_post_query)
web.run_app(app, port=8081)
