#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
import io
import os
from PbBot.utils.utils import humanbytes
from PbBot import Delete_after_duration
import speedtest
from datetime import datetime


class Speed(commands.Cog):

    def __init__(self, client):
        self.client = client

    # todo learn to await speedtest - its blocking code
    @commands.command(name='speed', description='Server speedtesting utility (Takes some time so be patient)',
                      aliases=['fast', 'speedtest'], brief='.speed | .fast | .speedtest gets you the Internet speed of'\
                                                           ' server (It is however a blocking code and will take a second.')
    async def speed(self, ctx):
        msg = await ctx.send("Calculating the Internet speed!")
        print("Starting speedtest!!")
        start = datetime.now()
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        response = s.results.dict()
        download_speed = response.get("download")
        upload_speed = response.get("upload")
        ping_time = response.get("ping")
        client_infos = response.get("client")
        i_s_p = client_infos.get("isp")
        i_s_p_rating = client_infos.get("isprating")
        await msg.edit(content='SpeedTest completed in {} seconds\nPing: {}\nDownload: {}\nUpload: {}\nInternet Service Provider: {}\nISP Rating: {}'.format(
                ms, ping_time, humanbytes(download_speed), humanbytes(upload_speed), i_s_p, i_s_p_rating), delete_after=Delete_after_duration)
        await ctx.send(f'{ctx.message.author}Speedtest done!', delete_after=2.0)
        await ctx.message.delete()
    # @commands.command() #for commands
    # @commands.Cog.listener #for event listener


def setup(client):
    client.add_cog(Speed(client))
