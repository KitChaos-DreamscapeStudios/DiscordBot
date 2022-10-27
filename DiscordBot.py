import discord
from pynput.keyboard import Key, Controller
import random

keyboard = Controller()



Servers = {}
class MyClient(discord.Client):
    name = "Prysm#7280"
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global Messages
        global Absorbing
        global Servers
        global keyboard
        if not message.guild in Servers.keys():
            Servers[message.guild] = {"Absorbing": False, "Messages": [], "Exploding": False}
        if Servers[message.guild]["Absorbing"] == True and not ">" in message.content and Servers[message.guild]["Exploding"] == False:
            
            Servers[message.guild]["Messages"].append(str(message.author) + ": " +  message.content)
        if message.content.upper() == ">WORD BOMB":
            await message.channel.send("Absorbing Words...")
            Servers[message.guild]["Absorbing"] = True
            
        if message.content.upper() == ">EXPLODE":
            
            Servers[message.guild]["Absorbing"] = False
            await message.channel.send(f"BOOM! The bomb exploded with a force of {len(Servers[message.guild]['Messages'])} Messages!")
            Bomb = ""
            Servers[message.guild]["Exploding"] = True
            for i in Servers[message.guild]["Messages"]:
                Bomb += (i + "\n")
                
            await message.channel.send(Bomb)
            Servers[message.guild]["Messages"] = []
            Servers[message.guild]["Exploding"] = False
        if message.content.upper() == ">SERVER INFO":
            await message.channel.send(f"```Server: {message.guild.name}\nMembers: {message.guild.member_count}```")
        if message.content.upper() == ">DEBUG":
            print(Servers)
        if random.randint(0, 4) == 4:
            if 'o' in message.content or 'O' and not "Prysm#7280" in message.content and not str(message.author) == "Prysm#7280":
                OwO = message.content
                OwO = OwO.replace('O', 'OwO')
                OwO = OwO.replace('o', 'OwO')
               
                print(message.author)
                print(self.name)
                
                await message.delete()
                await message.channel.send(str(message.author) +": " "Sorry I meant " + OwO)
##        if message.content.upper() == ">HIJACK":
##            Word = "Hello World"
##
##            for i in Word:
##                client.keyboard.press(i)
##                client.keyboard.release(i)
        #print(message)
            
                
       
        #await channel.send("Hello World")
####intents = discord.Intents.default()
##intents.message_content = Trues

client = MyClient()
token = open("Token.txt", 'r')
client.run(token)

