import discord
from discord.ext import commands
import main_bingo
import sys  
import io
import juego_bingo
import time
import random
from opciones_yuumi import opciones_yuumi
import asyncio
import os
from opciones_dav import opciones_dav

# Intents (requeridos para la API de Discord)
intents = discord.Intents.default()
intents.message_content = True

# Crear el bot con prefijo "!"
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento cuando el bot está en línea
@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

# Comando simple: responder "Hola"
@bot.command()
async def hola(ctx):
    await ctx.send("Holi")
# Comando para iniciar un juego de bingo en donde basciamente te muestra los cartones iniciales, los finales y te dice quien es el ganador(revisar los archivos que tengan "bingo")
@bot.command()
async def bingo(ctx):
    await ctx.send("🎲 Iniciando juego de Bingo...")
    await ctx.send("Por favor, ingresa los nombres de los jugadores separados por coma (ejemplo: Ana, Juan, Pedro):")
        # Espera un mensaje del mismo usuario que escribió el comando
    try:
        msg = await bot.wait_for(
            "message",
            timeout=30.0,  # 30 segundos para responder
            check=lambda m: m.author == ctx.author and m.channel == ctx.channel
        )
    except asyncio.TimeoutError:
        await ctx.send("No recibí respuesta inténtalo de nuevo")
        return
    nombres = [n.strip() for n in msg.content.split(",")]
    await ctx.send(f"✅ Jugadores registrados: {', '.join(nombres)}")

        # Aquí puedes pasar los nombres a tu lógica de bingo
    if len(nombres) < 2:
            await ctx.send("❌ Se necesitan al menos 2 jugadores para iniciar el juego.")
    else:
            await ctx.send("🎲 Iniciando juego de Bingo...")

    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    juego = juego_bingo.JuegoBingo(nombres)
    juego.iniciar_juego()
    sys.stdout = old_stdout
    output = buffer.getvalue()
    buffer.close()

    # Discord solo permite 2000 caracteres
    if len(output) > 1900:
        output = output[:1900] + "\n... (output truncado)"

    await ctx.send(f"📜 Resultado del Bingo:\n```\n{output}\n```")
#comandos que responden con uin gif aleatorio de las opciones dadas(revisar opciones_yuumi y opciones_dav
@bot.command()
async def yuumi(ctx):
    await ctx.send(random.choice((opciones_yuumi)))
@bot.command()
async def kuroh(ctx):
    await ctx.send("https://tenor.com/view/taraterrorful-tara-terrorful-cute-cute-cat-cat-gif-325998699308525328")
@bot.command() 
async def lauren(ctx):
    await ctx.send("https://tenor.com/view/death-stranding-kon-among-us-venti-genshin-impact-gif-19201377")
@bot.command()
async def pchan(ctx):
    await ctx.send("https://tenor.com/view/pchan-needy-streamer-overload-nso-pchan-plush-p-chan-gif-14379805615925328831")
@bot.command()
async def dav(ctx):
    await ctx.send(random.choice((opciones_dav)))
#comando para "shipear" a dos personas, te da el porcentaje de compatibilidad y dependiendo del porcentaje te da un gif distinto
@bot.command()
async def shipeo(ctx):
    await ctx.send("ingresa los nombres de las dos personas que quieres shipear separados por una coma")
    while True:    
        try:
            msg1 = await bot.wait_for(
            "message",
            timeout=30.0,  # 30 segundos para responder
            check=lambda m: m.author == ctx.author and m.channel == ctx.channel
        )
        except asyncio.TimeoutError:
            await ctx.send("No recibí respuesta inténtalo de nuevo")
            return
        nombres = [n.strip() for n in msg1.content.split(",")]
        if len(nombres) == 2:
            prob = random.randint(0, 100)
            await ctx.send(f"{nombres[0]} y {nombres[1]} tienen un {prob}% de compatibilidad")
            if prob < 50:
                await ctx.send("https://tenor.com/view/sad-wolf-furry-lone-wolf-cringe-gif-26450517")
            else:
                await ctx.send("https://tenor.com/view/my-beloved-you-are-you-are-my-beloved-2gays-kissing-valentines-gif-20399132")
            break
        else:
            await ctx.send("Por favor ingresa exactamente dos nombres separados por una coma")
# Ejecutar el bot (reemplaza con tu token)
bot.run("Tu_Token_Aqui")