# importa os módulos / import the modules
import os
import discord
import json
import re
from colorama import Fore, init
# inicia o cliente / Start the client
client = discord.Client()
init()

def center(var: str, space: int = None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2

    return "\n".join((' ' * int(space)) + var for var in var.splitlines())
# printa a mensagem de início
@client.event
async def on_ready():
    os.system('feito pelo satushi')
    print("scanning/scaneando")
    with open('config.json', 'r') as f:
        config = json.load(f)

    serveur_count = 0
    channels_count = 0
    messages_count = 0
    dm_count = 0

    if config['type']['servers/servidores'].lower() == "yes":
        for guild in client.guilds:
            print(f"[{Fore.RED}SERVIDORES/Servers{Fore.RESET}] Scanning your servers / Escaneando o servidor " + guild.name+ " "*30)
            serveur_count += 1
            for channel in guild.text_channels:
                print(f"[{Fore.CYAN}CANAIS/Channels{Fore.RESET}] Scanning text channels / Escaneando os canais de texto " + channel.name + " "*30, end="\r")
                channels_count += 1
                try:
                    async for message in client.get_channel(channel.id).history(limit=99999):
                        messages_count += 1
                        for searchmessage in config['words/palavras']:
                            if searchmessage in message.content:
                                print(f"[{Fore.GREEN}MENSAGEM/Message{Fore.RESET}] Message Found: / Mensagem Encontrada: " + message.content)
                                open('achadosfound.txt', 'a+').write(f"{message.author.name}: {message.content}\n")

                        for regex in config['regex']:
                            if re.match(r"" + regex, message.content):
                                print(f"[{Fore.GREEN}MENSAGEM/Message{Fore.RESET}] Message Found: / Mensagem Encontrada: " + message.content)
                                open('achadosfound.txt', 'a+').write(f"{message.author.name}: {message.content}\n")
                except:
                    pass

    if config['type']['dm'].lower() == "yes":
        for prv_channel in client.private_channels:
            channels_count += 1
            dm_count += 1
            print(f"[{Fore.CYAN}CANAIS/Channels{Fore.RESET}] Scanning the DMs / Escaneando a DM: {str(prv_channel).replace('Direct Message with / Mensagem direta com ', '')}" + " "*30, end="\r")
            channel = client.get_channel(prv_channel.id)
            try:
                async for message in channel.history(limit=99999):
                    messages_count += 1
                    for searchmessage in config['words/palavras']:
                        if searchmessage in message.content:
                            print(f"[{Fore.GREEN}MENSAGEM/Message{Fore.RESET}] Message Found: / Mensagem Encontrada: " + message.content)
                            open('achadosfound.txt', 'a+').write(f"{message.author.name}: {message.content}\n")

                    for regex in config['regex']:
                        if re.match(r"" + regex, message.content):
                            print(f"[{Fore.GREEN}MENSAGEM/Message{Fore.RESET}] Message Found: / Mensagem Encontrada: " + message.content)
                            open('achadosfound.txt', 'a+').write(f"{message.author.name}: {message.content}\n")
            except:
                pass

    input(f"{Fore.RED+str(messages_count)+Fore.RESET} Mensagens foram escaneadas {Fore.RED+str(channels_count)+Fore.RESET} Grupos ({Fore.RED+str(serveur_count)+Fore.RESET} Servidores, {Fore.RED+str(dm_count)+Fore.RESET} DMs)")


client.run('token')
