import argparse
import asyncio
import time
import json

from aiohttp import ClientSession


async def debug_one_user_post_request(url, i):
    """
    DEBUG
    """
    data = json.dumps(
        {
            'query': 'gettoken',
            'auth_type': 'device',
            'device_id': 'fdsgfsd',
            'secret_key': '123qweQWE!@101#',
            'name': 'gsdgsdgsd',
            'gk_id': 'wehifbwefn',
            'gk_enable': False,
        }
    )

    async with ClientSession() as session:
        resp_start = time.time()
        async with session.post(url='http://0.0.0.0:8081/yo', data=data) as response:
            print(i, time.time() - resp_start, await response.text())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c',
        "--concurrent_users",
        help="define a number of concurrent users",
        type=int,
    )
    parser.add_argument(
        '-u',
        "--url",
        help="define a host: http://127.0.0.1:8080",
    )
    args = parser.parse_args()

    users_number = args.concurrent_users or 5
    url = args.url or 'http://0.0.0.0:8081'

    loop = asyncio.get_event_loop()
    coros = [asyncio.Task(debug_one_user_post_request(url, i)) for i in range(users_number)]
    loop.run_until_complete(asyncio.gather(*coros))
