import discord
import qrcode
from discord.ext import commands
from colorama import init, Fore
print(Fore.LIGHTBLUE_EX + '''
                                                                                              
  ####  #####      ####   ####  #####  ######    #####   ####   ####      ####  ###### #    # 
 #    # #    #    #    # #    # #    # #         #    # #      #    #    #    # #      ##   # 
 #    # #    #    #      #    # #    # #####     #    #  ####  #         #      #####  # #  # 
 #  # # #####     #      #    # #    # #         #    #      # #         #  ### #      #  # # 
 #   #  #   #     #    # #    # #    # #         #    # #    # #    #    #    # #      #   ## 
  ### # #    #     ####   ####  #####  ######    #####   ####   ####      ####  ###### #    # 
                                                                                              ''')
intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)
token = input(Fore.LIGHTCYAN_EX + "bot token: ")
def create_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")


link = input("url for create qr code: ")

@client.event
async def on_message(message):
    if message.content == '-qr':
        create_qr_code(link)
        await message.channel.send("free nitro here:")
        await message.channel.send(file=discord.File("qr_code.png"))


client.run(token)
