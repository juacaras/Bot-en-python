import discord
from discord.ext import commands
import main_bingo
import sys  
import io
import juego_bingo
import time
import random
from opciones_yuumi import opciones_yuumi

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
    await ctx.send("¡Hola! 👋 Soy tu bot en Discord.")
@bot.command()
async def bingo(ctx):
    await ctx.send("🎲 Iniciando juego de Bingo...")
    await ctx.send("Por favor, ingresa los nombres de los jugadores separados por coma (ejemplo: Ana, Juan, Pedro):")
        # Espera un mensaje del mismo usuario que escribió el comando
    msg = await bot.wait_for(
            "message",
            timeout=60.0,  # 60 segundos para responder
            check=lambda m: m.author == ctx.author and m.channel == ctx.channel
        )
        
        # Procesar los nombres
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
# Ejecutar el bot (reemplaza con tu token)
bot.run("token_aqui")

