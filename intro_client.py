#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-01-03 11:34:31
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://localhost:4134") as websocket:
        await websocket.send("Hello world")
        while True:
            print(await websocket.recv())


asyncio.run(hello())

