import discord
from discord.ext import commands
from discord.ui import View, Button, Select
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
prefixes = {}
def get_prefix(bot, message):
    return prefixes.get(message.guild.id, "!")
# Intents (requeridos para la API de Discord)
intents = discord.Intents.default()
intents.message_content = True

# Crear el bot con prefijo "!"
bot = commands.Bot(command_prefix=get_prefix, intents=intents)

# Evento cuando el bot está en línea
@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

# Comando simple: responder "Hola"
@bot.command()
async def hola(ctx):
    """Holi."""
    await ctx.send("Holi")
# Comando para iniciar un juego de bingo en donde basciamente te muestra los cartones iniciales, los finales y te dice quien es el ganador(revisar los archivos que tengan "bingo")
@bot.command()
async def bingo(ctx):
    """Juega bingo :3"""
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
    embed = discord.Embed(
        title="¡Bingo!",
        description="Aquí están los resultados del juego de Bingo:",
        color = discord.Color.green())
    embed.add_field(
        name = f"**jugadores: {', '.join(nombres)}**",
        value = f"```\n{output}\n```",
        inline = False
    )
    

    await ctx.send(embed=embed)
#comandos que responden con uin gif aleatorio de las opciones dadas(revisar opciones_yuumi y opciones_dav
@bot.command()
async def yuumi(ctx):
    await ctx.send(random.choice((opciones_yuumi)))
@bot.command()
async def kuroh(ctx):
    """kuroh gif."""
    await ctx.send("https://tenor.com/view/taraterrorful-tara-terrorful-cute-cute-cat-cat-gif-325998699308525328")
@bot.command() 
async def lauren(ctx):
    """lauren gif."""
    await ctx.send("https://tenor.com/view/death-stranding-kon-among-us-venti-genshin-impact-gif-19201377")
@bot.command()
async def pchan(ctx):
    """p-chan >.<"""
    await ctx.send("https://tenor.com/view/pchan-needy-streamer-overload-nso-pchan-plush-p-chan-gif-14379805615925328831")
@bot.command()
async def dav(ctx):
    """Muestra un gif aleatorio de Dav."""
    await ctx.send(random.choice((opciones_dav)))
#comando para "shipear" a dos personas, te da el porcentaje de compatibilidad y dependiendo del porcentaje te da un gif distinto
@bot.command()
async def shipeo(ctx):
    """Shipea a dos personas."""
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
                embed = discord.Embed(
                    title = "ni se acerquen",
                    color = discord.Color.blue()
                )
                embed.set_image(url="https://cdn.discordapp.com/attachments/1431445809517432935/1431446057354662001/XDDDD.gif?ex=68fd7187&is=68fc2007&hm=cc22520a7c71dc9900cda8576b3c57005a5b584efd850be04997a36b74886372&")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title = "busquen una habitacion",
                    color = discord.Color.red()
                )
                embed.set_image(url="https://cdn.discordapp.com/attachments/1431445809517432935/1431445869537792141/mizuki-akiyama.gif?ex=68fd715a&is=68fc1fda&hm=3f1ca77249c4c31edc97692d1c4c48b25f49f504ef54536c10b1f47f514bafe1&")
                await ctx.send(embed=embed)
            break
        else:
            await ctx.send("Por favor ingresa exactamente dos nombres separados por una coma")
@bot.command()
@commands.has_permissions(administrator=True)
async def prefijo(ctx, nuevo_prefijo):
    """Cambia el prefijo que usa el bot en el server."""
    prefixes[ctx.guild.id] = nuevo_prefijo
    await ctx.send(f"Prefijo cambiado a: {nuevo_prefijo}")
@bot.command()
async def comandos(ctx):
    """Muestra los comandos disponibles por categorias."""
    embed_inicial = discord.Embed(
        title = "Lista de comandos",
        description= "Selecciona la categoria que quieres ver",
        color=discord.Color.purple()

    ) 
    embed_juegos = discord.Embed(
        title = "comandos de juegos",
        description = f"""
        {prefixes.get(ctx.guild.id, '!')}bingo - {bingo.help}
        """,
        color = discord.Color.blue()
    )
    embed_juegos.set_thumbnail(url="https://cdn.discordapp.com/attachments/938242979313885256/1414309064850018375/qasecdxaucmf1.gif?ex=68fd0ff5&is=68fbbe75&hm=61db773f7e3ed62c2fa28d2ded3efd181db816f213e7b8e93651b7ecbe986b75&")
    select = Select(
        placeholder="Selecciona una categoria",
        options = [
            discord.SelectOption(label="Inicio", description="volver al inicio"),
            discord.SelectOption(label="Juegos", description="comandos de juegos")
        ]
    )
    async def select_callback(interaction):
        if select.values[0] == "Inicio":
            await interaction.response.edit_message(embed=embed_inicial)
        elif select.values[0] == "Juegos":
            await interaction.response.edit_message(embed=embed_juegos)
    embed_inicial.set_image(url="https://media.discordapp.net/attachments/1166114583828766843/1203732152223797328/image0.gif?ex=68fcf46d&is=68fba2ed&hm=dc6880ef7f1a999360f3b54490c336ba54092ace963882ebcd51a3539da79860&")
    select.callback = select_callback
    view = View()
    view.add_item(select)
    await ctx.send(embed=embed_inicial, view=view)  
# Ejecutar el bot (reemplaza con tu token)
bot.run("Token")