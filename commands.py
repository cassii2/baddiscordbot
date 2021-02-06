import logging
import discord
import random

commandDictionary = {}


class Commands:
    async def rollDice(self, args, message):
        num = 0
        add = 0
        numArgs = len(args)

        if numArgs == 0:
            await message.channel.send('Incorrect format')
            return

        if numArgs > 3 or (numArgs > 2 and args[1] != '+'):
            await message.channel.send('Incorrect format')
            return
        if numArgs >= 1:
            if args[0][0] == 'd' and args[0][1:].isnumeric():
                num = int(args[0][1:])
            elif args[0].isnumeric():
                num = int(args[0])
            elif not args[0].isnumeric():
                await message.channel.send('Incorrect format')
                return
        if numArgs == 3 and args[1] == '+':
            numArgs -= 1
            args[1] = '+{}'.format(args[2])
        if numArgs == 2 and args[1][0] == '+':
            args[1] = args[1][1:]
            if args[1].isnumeric():
                add = int(args[1])
            else:
                await message.channel.send('Incorrect format')
                return

        if num <= 0:
            await message.channel.send('Please choose a number higher than 0!')
            return
        num = random.randrange(1, num + 1) + add
        await message.channel.send(num)

    async def ping(self, args, message):
        await message.channel.send('Pong!')


class Parser:
    async def parse(self, command, message):
        commandList = command.split(' ')
        await commandDictionary[commandList[0]](commandList[1:], message)
        return


commands = Commands()
parser = Parser()
parse = parser.parse

commandDictionary['roll'] = commands.rollDice
commandDictionary['ping'] = commands.ping
