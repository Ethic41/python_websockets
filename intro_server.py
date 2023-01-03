#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-01-03 11:41:35
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


import asyncio
import websockets


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
        while True:
            await websocket.send(input())


async def main():
    async with websockets.serve(echo, "localhost", 4134):
        await asyncio.Future()


asyncio.run(main())
