import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
import time
import colorsys
import sys
import subprocess
import os
import json
import traceback
import random
from random import choice
import request


start_time = time.time()


bot = commands.Bot('a!')
print (discord.__version__)
chat_filter = ("pnc", "pau no cu", "fdp", "filho da puta", "filha da puta","arrombado", "teste")
bot.remove_command("help")
bypass_list = []
COLOUR = 0xFFFF00
COR = 0x00ff00
amounts = {}
marry = {}
@bot.event
async def on_ready():
	while True:
		await bot.change_presence(game=discord.Game(name='Divulgue O Servidor Para Seus Amigos!', type=3))
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='para ' + str(len(set(bot.get_all_members())))+ ' Dlcs!👥', type=1))
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='Kunai Nos Invasores'))
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='Musica com o Hokage', type=2))
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='Seja Staff Basta entrar em contato com o Hokage', type=1))
		await asyncio.sleep(30)








    

@bot.command(pass_context=True)
async def soma(ctx, n1: str=None, n2: str=None):
	resultado = n1 + n2
	await bot.say(resultado)

@bot.event
async def on_member_join(member):
	emoji = get(bot.get_all_emojis(), name='PinguWithGun')
	canal = bot.get_channel("559509000790605830")
	regras = bot.get_channel("535415004401369096")
	registro = bot.get_channel("544255099078180890")
	msg = "{} Seja bem vindo ao **{}** Leia as {} e va em {} para receber suas tags! {}".format(member.mention, message.server.name, regras.mention, registro.mention, emoji)
	await bot.send_message(canal, msg) 
	




	
@bot.event
async def on_member_remove(member):
   canal = bot.get_channel("535466617006456833")
   msg = "{} Vai nas sombras".format(member.name)
   await bot.send_message(canal, msg)		





    
@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title="Pong!", description='Meu Ping {}ms.'.format(round((t2-t1)*1000)), color=0x76FF03)
	embed.set_footer(text ='Comando pedido por: {} | Hashirama Senju 🔪 Oficial'.format(ctx.message.author.name))
	await bot.say(embed=embed)
	print('comando ping digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))


			
@bot.command(pass_context=True)
async def servers(ctx):
	servers = list(bot.servers)
	await bot.say("Estou conectado em " + str(len(bot.servers)) + " servers:")
	for x in range(len(servers)):
		await bot.say(" "+servers[x-1].name)

@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None, *, motivo: str = None):
	if not member:
		return await bot.say('Você não especificou o usuário. Exemplo: ``a!ban <@usuário> <motivo>``')
	if not motivo:
		return await bot.say('Você não especificou o motivo. Exemplo: ``a!ban <@usuário> <motivo>``')
	else:
		await bot.ban(member)
		embed = discord.Embed(title='Ação | Ban', description='{} usuário banido com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
		embed.add_field(name='Executor', value=ctx.message.author)
		embed.add_field(name='Usuário', value=member.name)
		embed.add_field(name='Motivo', value=motivo)
		embed.set_footer(text='Comando Realizado Por: {}| Bot Oficial Hashirama Senju 🔪★'.format(ctx.message.author.name))
		await bot.say(embed=embed)
		embedpv = discord.Embed(title='Você foi banido!'.format(ctx.message.author.mention), color=0xff0Ab)
		embedpv.add_field(name='Autor', value=ctx.message.author)
		embedpv.add_field(name='servidor em que foi banido', value=ctx.message.server.name)
		embedpv.add_field(name='Motivo', value=motivo)
		embedpv.set_thumbnail(url=ctx.message.server.icon_url)
		await bot.send_message(member, embed=embedpv)
		print('comando ban digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
							
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User=None, *, motivo: str = None):

	if not user:
		return await bot.say('Você não especificou o usuário. Exemplo: ``a!kick <@usuário> <motivo>``')
	if not motivo:
		return await bot.say('Você não especificou o motivo. Exemplo: ``a!kick <@usuário> <motivo>``')
	else:
		await bot.kick(user)
		embed = discord.Embed(title='Ação | Kick!', description='{} usuário expulso com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
		embed.add_field(name='Autor', value=ctx.message.author)
		embed.add_field(name='usuário', value=member.name)
		embed.add_field(name='Id', value=member.id)
		embed.add_field(name='Motivo', value=motivo)
		embed.set_footer(text='Comando Realizado Por: {}| Bot Oficial Hashirama Senju 🔪★'.format(ctx.message.author.name))
		await bot.say(embed=embed)
		embedpv = discord.Embed(title='Ação | Kick'.format(ctx.message.author.mention), color=0xff0Ab)
		embedpv.add_field(name='Executor', value=ctx.message.author)
		embedpv.add_field(name='servidor em que foi expulso', value=ctx.message.server.name)
		embedpv.add_field(name='Motivo', value=motivo)
		embedpv.set_thumbnail(url=ctx.message.server.icon_url)
		await bot.send_message(member, embed=embedpv)
	print('comando kick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
		
	
@bot.command(pass_context=True)
async def votar(ctx, *, mensagem: str= None):
	if not mensagem:
		return await bot.say('Você precisa falar algo para votar')
	else:
			vote = await bot.say(embed=discord.Embed(color=0xff0000, description=mensagem))
			await bot.add_reaction(vote, "✅")
			await bot.add_reaction(vote, "❌")
	print('comando votar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
	

			
					
	
	
@bot.command(pass_context=True)
async def perfil(ctx, user: discord.User):
    user = user or ctx.message.author
    embed = discord.Embed(title="perfil de {}".format(ctx.message.author.name), description="Reflexão: Hoje n tem reflexão :(", color=0x00ff00)
    embed.add_field(name="Nome", value=user.name, inline=True)
    embed.add_field(name="ID do usuário", value=user.id, inline=True)
    embed.add_field(name="Status do usuário", value=user.status, inline=True)
    embed.add_field(name="Melhor cargo", value=user.top_role)
    embed.add_field(name="entrou no servidor", value=user.joined_at)
    embed.set_footer(text ='Comando pedido por: {} | Hashirama Senju 🔪 Oficial'.format(ctx.message.author.name))
    await bot.say(embed=embed)
    print('comando perfil digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	

	
@bot.command(pass_context=True)
async def serverinfo(ctx):
	embed = discord.Embed(name="{}' serverinfo".format(ctx.message.server.name), description="a!ajuda para ver meus comandos!.", color=0x00fA00)
	embed.add_field(name="📄Nome do servidor", value=ctx.message.server.name, inline=True)
	embed.add_field(name = '👑 Dono', value = str(ctx.message.server.owner) + '\n' + ctx.message.server.owner.id);
	embed.add_field(name="💻ID do servidor", value=ctx.message.server.id, inline=True)
	embed.add_field(name="🎓Total de roles", value=len(ctx.message.server.roles), inline=True)
	embed.add_field(name="👥Quantidade de Membros", value=len(ctx.message.server.members))
	embed.add_field(name='🌎 Região', value=ctx.message.server.region)
	embed.add_field(name='👮Role Top1', value=ctx.message.server.role_hierarchy[0])
	embed.set_footer(text ='Comando pedido por: {} | Hashirama Senju 🔪 Oficial'.format(ctx.message.author.name))
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.say(embed=embed)
	print('comando serverinfo digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User):
    user = user or ctx.message.author
    hugemb = discord.Embed(title='Avatar de {}'.format(user.name), color=0x6A1B9A)
    hugemb.set_image(url=user.avatar_url)
    hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju 🔪 Oficial'.format(ctx.message.author.name))
    await bot.say(embed=hugemb)
    print('comando avatar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def a(ctx):

	embed1 =discord.Embed(
	title="Olá! Ninja Da Aldeia Da Folha, Bem-vindo ao nosso registro reaja abaixo com emojis,  de acordo com seu gênero etc!",
	color=COR)
	embed1.add_field(name="Qual Seu Gênero?", value="Masculino - 👨\n"
	"Feminino - 👩")
	embed1.add_field(name="Qual sua Idade?", value="+18 - 😈\n"
	"-18 - 👶")
	embed1.add_field(name="Você é Hétero ou LGBT?", value="Hétero - 🏃\n"
	"LGBT - 🌈")
	embed1.add_field(name="Qual seus Status de Relacionamento?", value="Solteiro - 🚶\n"
	"Iludido - 😪\n"
	"Casado - 💍\n"
	"Namorando - 😍\n"
	"Clique no ✅ para confirmar seu registro",)
	botmsg = await bot.say(embed=embed1)

	await bot.add_reaction(botmsg, "👨")
	await bot.add_reaction(botmsg, "👩")
	await bot.add_reaction(botmsg, "😈")
	await bot.add_reaction(botmsg, "👶")
	await bot.add_reaction(botmsg, "🏃")
	await bot.add_reaction(botmsg, "🌈")
	await bot.add_reaction(botmsg, "🚶")
	await bot.add_reaction(botmsg, "😪")
	await bot.add_reaction(botmsg, "💍")
	await bot.add_reaction(botmsg, "😍")
	await bot.add_reaction(botmsg, "✅")
					
	global msg_id 
	msg_id = botmsg.id
	
	global msg_user
	msg_user = message.author
@bot.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    
    
    if reaction.emoji == "👨" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『👨』Masculino", msg.server.roles)
     await bot.add_roles(user, role)
     print("add")
    if reaction.emoji == "👩" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『👩』Feminino", msg.server.roles)
     await bot.add_roles(user, role)
     print("add")

    if reaction.emoji == "✅" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『☠』Ninja", msg.server.roles)
     await bot.add_roles(user, role)
     print("add") 	
    if reaction.emoji == "👶" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『🔞』-18", msg.server.roles)
     await bot.add_roles(user, role)
     print("add")
    if reaction.emoji == "😈" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『🔥』+18", msg.server.roles)
     await bot.add_roles(user, role)
     print("add")     
    if reaction.emoji == "🏃" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『🔥』Hétero", msg.server.roles)
     await bot.add_roles(user, role)     
     print('add')
    if reaction.emoji == "🌈" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『🌈』LGBT", msg.server.roles)
     await bot.add_roles(user, role)
    if reaction.emoji == "🚶" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『🏃』Solteiro(a)", msg.server.roles)
     await bot.add_roles(user, role)     
     print('add')
    if reaction.emoji == "😍" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『😍』Namorando", msg.server.roles)
     await bot.add_roles(user, role)
     

    if reaction.emoji == "😪" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『😪』Iludido", msg.server.roles)
     await bot.add_roles(user, role)
     print("add")
    if reaction.emoji == "💍" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『💍』Casado", msg.server.roles)
     await bot.add_roles(user, role)
     print("add") 	
     
@bot.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "👨" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『👨』Masculino", msg.server.roles)
     await bot.remove_roles(user, role)
     print("add")
    if reaction.emoji == "👩" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『👩』Feminino", msg.server.roles)
     await bot.remove_roles(user, role)
     print("add")

    
     print('add')
    if reaction.emoji == "👶" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『🔞』-18", msg.server.roles)
     await bot.remove_roles(user, role)
     print("add")
    if reaction.emoji == "😈" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『🔥』+18", msg.server.roles)
     await bot.remove_roles(user, role)
     print("add")     
    if reaction.emoji == "🏃" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『🔥』Hétero", msg.server.roles)
     await bot.remove_roles(user, role)
     print('add')
    if reaction.emoji == "🌈" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『🌈』LGBT", msg.server.roles)
     await bot.removes_roles(user, role)
    if reaction.emoji == "🚶" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『🏃』Solteiro(a)", msg.server.roles)
     await bot.remove_roles(user, role)
     print('add')
     
    if reaction.emoji == "😍" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『😍』Namorando", msg.server.roles)
     await bot.remove_roles(user, role)
     

    if reaction.emoji == "😪" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『😪』Iludido", msg.server.roles)
     await bot.remove_roles(user, role)
     print("add")
    if reaction.emoji == "💍" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "『💍』Casado", msg.server.roles)
     await bot.remove_roles(user, role)
     print("add") 	        
          
@bot.command(pass_context=True)
async def kiss(ctx, user: discord.User=None):
    if not user:
        return await bot.say("Você Não Marcou Um Usuário Para Beijar")
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/533253217883258890/tumblr_mie2frAdXc1rfj82jo2_500.gif','https://cdn.discordapp.com/attachments/514045065929162764/533253218860269577/86d4a046c8a32a28341353fc95bedc82.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494353694097438/feliz-aniversario-6224237-140820161718.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Beijo! ❤',  description='**{}** recebeu um beijo de **{}**! Casal Fofo! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)
        print('comando kiss digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	

	
@bot.command(pass_context=True)
async def kepiada(ctx):
	a = 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589504/Piada_mulher_de_tpm_cafe.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589505/images_6.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589506/images_4.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537711026177/o_rapaz_apaixonado_diz_a_sua_amada.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538214604810/images_5.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538214604812/ladrao-em-casa-3684XBr1G1DBAQ.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538734567424/Passa_Passa_Passa.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538734567425/na_delegacia_seu_delegado_meu_marido_saiu_de_casa.jpg'
	hug = random.choice(a)
	hugemb = discord.Embed(title='Piadas', color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju 🔪 Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando kepiada digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
@bot.command(pass_context=True)
async def report(ctx, user: discord.User, *, motiv: str=None, limit: int=1):
	if not motiv:
		return await bot.say('{} Você Não especificou motivo do reporte')
	async for msg in bot.logs_from(ctx.message.channel, limit=1):
            try:
                await bot.delete_message (msg)
            except:
                pass
                embed = discord.Embed(title="usuário reportado", description="seu reporte foi enviado com sucesso! caso for aprovado o usuário reportado sera punido".format(ctx.message.author.mention), color=0x00ff00)
                await bot.say(embed=embed)
                await asyncio.sleep(2)
	canal = bot.get_channel("535829555189907469")
	horario = datetime.datetime.now().strftime("%H:%M:%S")	
	ms = discord.Embed(title='usuário reportado', color=0x00ff00)
	
	ms.add_field(name="Autor", value=ctx.message.author.name, inline=True)
	ms.add_field(name="usuário reportado", value=user, inline=True)
	ms.add_field(name="Hora", value=horario, inline=True)
	ms.add_field(name="Motivo", value=motiv, inline=True)
	await bot.send_message(canal, embed=ms)	
			
@bot.command(pass_context=True)
async def meme(ctx):
	a = 'https://cdn.discordapp.com/attachments/514045065929162764/539763086895349760/images_9.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763086895349761/cara-mano-tatuei-o-nome-da-minha-namora-e-ela-20426746.png', 'https://cdn.discordapp.com/attachments/514045065929162764/539763087474032640/images_7.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763087474032641/images_10.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763088002383883/images_11.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763088455630855/3d6dcd431d328b82ac2bc8edf5f754ee--kawaii.jpg'
	hug = random.choice(a)
	hugemb = discord.Embed(title='SO MEME DE QUALIDADE MONSTRA', color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju 🔪 Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando meme digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

	

	
@bot.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await bot.change_nickname(user, nickname)
    emb = discord.Embed(title='Apelido alterado')
    emb.add_field(name='usuário', value =user.name)
    emb.add_field(name='Autor', value =ctx.message.author.name)
    await bot.say(embed=emb)
    print('comando setnick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def avisar(ctx, member: discord.Member, *, content: str):
	embed = discord.Embed(description='{} foi avisado com sucesso! por {}'.format(member.mention, ctx.message.author.mention), color=0x7a00bb)
	await bot.send_message(member, content)
	await bot.say(embed=embed)



	
			
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.add_roles(member, role)
    embed = discord.Embed(description=' ✅Role Adicionada com sucesso!', color=0x00ff00)
    await bot.say(embed=embed)
    print('comando addrole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
  
    
@bot.command(pass_context=True)
async def falar(ctx, *, arg):
	await bot.say(arg)
	print('comando falar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
@commands.has_permissions(gerence_res=True)
async def removerole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.remove_roles(member, role)
    embed = discord.Embed(description=' 👮Role removida com sucesso', color=0xff0000)
    await bot.say(embed=embed)
    print('comando removerole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def slap(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539494352112713760/giphy.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494352112713760/giphy.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Tapa!',  description=':scream:| **{}** Deu Um tapa em **{}**! Que Tapa!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando slap digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def brigar(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539516094273290240/300px-DarkCureFight.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733424185802763/source.gif'
	

	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='BRIGA!',  description=':scream:| **{}** Brigou com **{}**!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando brigar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))	
	
@bot.command(pass_context=True)
async def dance(ctx, user: discord.User=None):
	if not user:
		return await bot('Você precisa mencionar algum usuário')
	else:
		list = 'https://cdn.discordapp.com/attachments/514045065929162764/539516095900418104/fanfiction-naruto-ao-seu-lado-2635515231020140950.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539516093593550868/ed8964dd9fb2f90e5eb4b19c577bec74.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539516093593550869/Akatsuki28.gif'
		hug = random.choice(list)
		hugemb = discord.Embed(title='Dançando!',  description=':man_dancing:| **{}** Esta dançando com **{}**! Passinho dos Maloka 😎'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
		hugemb.set_image(url=hug)
		hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju Oficial'.format(ctx.message.author.name))
		await bot.say(embed=hugemb)
		
	print('comando ping digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
		

@bot.command(pass_context=True)
async def matar(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539733424185802762/b19b70f5c546ec7c67c2f0b4e61c21f743a5acaf_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733902097645568/tumblr_m6rerquar01qd4f2uo1_500.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Assasino!',  description='👮☎| **{}** Matou **{}**! ASSASINO!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	

	
	
@bot.command(pass_context=True)
async def atack(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539494351030452238/tumblr_mzh5vtuEIC1rm4wgqo4_r2_500.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494352926277633/01_Rikka.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494350053310475/G4dfvA5.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733423418376194/large.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Atack!',  description='💥| **{}** Atacou **{}**! Como ousas me atacar!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def suicidio(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533344634576044052/tumblr_nee9xjzaxR1r3rdh2o1_500-1.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533344635247001602/47892bb88afc132a3afb775988208240.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Suicidio 💔',  description='**{}** se suicidou!'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju 🔪 Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def voadora(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539733422621589504/giphy_6.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733422621589504/giphy_6.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Voadora',  description='**{}** Deu uma voadora em **{}** EITA!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju 🔪 Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def deathnote(ctx, user: discord.User=None, nu1: str=None):
    if not user:
        return await bot.say("{} Você não definiu seu amigo para matar.".format(ctx.message.author.mention))
    if not nu1:
        return await bot.say('{} Defina O Motivo'.format(ctx.message.author.mention))
    else:
        list = 'https://cdn.discordapp.com/attachments/514045065929162764/534806488531599380/14ae937e622c452bc45e509ed43c8e38a410fc0b_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533615190273425409/67dc6ce11c0ebe1c723983f18d7f68a8b0d11887_hq.gif'
        hug = random.choice(list)
        hugemb = discord.Embed(title='Death Note 💀',  description='**{}** escreveu o nome de **{}** em seu Death Note'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
        hugemb.set_image(url=hug)
        hugemb.set_footer(text='Bot Oficial Hashirama Senju')
        await bot.say(embed=hugemb)
        await asyncio.sleep(5)
        hugemb = discord.Embed(title='Death Note 💔',  description='**{}** morreu de **{}** depois de ter seu nome escrito no Death Note de **{}**'.format(user.name, nu1, ctx.message.author.name), color=0xA7ffbb)
        hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju Oficial'.format(ctx.message.author.name))
        await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def hug(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/531090629715951629/532667673943736351/action.gif','https://cdn.discordapp.com/attachments/531090629715951629/532672938596368393/action.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494351555002379/tumblr_mdi1l8AaDi1rcm8d4o1_500.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Abraço ❤',  description='**{}** Ele(a) recebeu um abraço de **{}**!! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0x00ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Hashirama Senju🔪 Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)  
	
@bot.command()
async def flipcoin():
	list = 'tapa na **CARA**', 'Rei perdeu a **COROA**'
	await bot.say(random.choice(list))
	
			
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voicemute(ctx, member: discord.Member):
    await bot.server_voice_state(member,mute=True)
    emb = discord.Embed(title='Usuário mutado voz', description='{} foi mutado com sucesso.'.format(member.mention), color=0xE57373)
    emb.set_footer(text ='Comando Realizado Por: {}| Bot Oficial Hashirama Senju ★'.format(ctx.message.author.name))
    await bot.say(embed=emb)	

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voiceunmute(ctx, member: discord.Member):
    await bot.server_voice_state(member,mute=False)
    emb = discord.Embed(title='Usuário desmutado voz', description='{} foi desmutado com sucesso.'.format(member.mention), color=0xE57373)
    emb.set_footer(text ='Comando Realizado Por: {}| Bot Oficial Hashirama Senju ★'.format(ctx.message.author.name))
    await bot.say(embed=emb)	
		
				
@bot.command(pass_context=True)
async def unmute(ctx, member: discord.User=None):
	if not member:
		return await bot.say('Você não especificou o usuário para aprender a falar. Exemplo: ``a!unmute @usuário``')
	else:
		role = discord.utils.get(member.server.roles, name="Silenciado")
		await bot.remove_roles(member, role)
		embed = discord.Embed(title='usuário aprendeu a falar novamente!', color=0xff0Ab)
		embed.add_field(name='Autor', value=ctx.message.author)
		embed.add_field(name='usuário', value=member.name)
		embed.add_field(name='Id', value=member.id)
		embed.set_footer(text='Comando Realizado Por: {}| Bot Oficial Hashirama Senju ★'.format(ctx.message.author.name))
		await bot.say(embed=embed)
		embedpv = discord.Embed(title='Você aprendeu a falar novamente!'.format(ctx.message.author.mention), color=0xff0Ab)
		embedpv.add_field(name='Autor', value=ctx.message.author)
		embedpv.add_field(name='servidor em que aprendeu a falar', value=ctx.message.server.name)
		embedpv.set_thumbnail(url=ctx.message.server.icon_url)
		await bot.send_message(member, embed=embedpv)
		print('comando kick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))



@bot.command(pass_context=True)
async def mute(ctx, member: discord.User, motivo: str=None):
    if not member:
        return await bot.say("Você Não Especificou Um Usuário Para Mutar")
    if not motivo:
        return await bot.say('Você não especificou o motivo. Exemplo: ``a!mute <@usuário> <motivo>``')
    else:
        role = discord.utils.get(member.server.roles, name="Silenciado")
        await bot.add_roles(member, role)
        embed = discord.Embed(title='usuário mutado!', description='{} usuário mutado com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
        embed.add_field(name='Autor', value=ctx.message.author)
        embed.add_field(name='usuário', value=member.name)
        embed.add_field(name='Id', value=member.id)
        embed.add_field(name='Motivo', value=motivo)
        embed.set_footer(text='Comando Realizado Por: {}| Bot Oficial Hashirama Senju ★'.format(ctx.message.author.name))
        await bot.say(embed=embed)
        embedpv = discord.Embed(title='Você foi mutado!'.format(ctx.message.author.mention), color=0xff0Ab)
        embedpv.add_field(name='Autor', value=ctx.message.author)
        embedpv.add_field(name='servidor em que foi mutado', value=ctx.message.server.name)
        embedpv.add_field(name='Motivo', value=motivo)
        embedpv.set_thumbnail(url=ctx.message.server.icon_url)
        await bot.send_message(member, embed=embedpv)
        print('comando kick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int=100):
    async for msg in bot.logs_from(ctx.message.channel, limit=limit):
            try:
                await bot.delete_message (msg)
            except:
                pass
    await bot.say ("Chat Limpo por {}".format(ctx.message.author.mention))
    print('comando clear digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def setcargo(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.add_roles(member, role)
    embed = discord.Embed(description=' ✅Role Adicionada com sucesso!', color=0x00ff00)
    await bot.say(embed=embed)
    print('comando addrole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))	


@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def removercargo(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.remove_roles(member, role)
    embed = discord.Embed(description=' 👮Role removida com sucesso', color=0xff0000)
    await bot.say(embed=embed)
    print('comando removerole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    
   
    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Ajuda')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'a!modajuda ',value ='Comandos de moderação Ex: ban,kick e clear etc...',inline = False)
    embed.add_field(name = 'a!diversaoajuda ',value ='Comandos de diversão e que todos podem usar! Ex: kiss,hug e deathnote.',inline = False)
    embed.set_footer(text='comando realizado por {}| Bot Oficial Hashirama Senju'.format(ctx.message.author.name))
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando help digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))    
    
    
@bot.command(pass_context = True)
async def ajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    
   
    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Ajuda')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'a!modajuda ',value ='Comandos de moderação Ex: ban,kick e clear etc...',inline = False)
    embed.add_field(name = 'a!diversaoajuda ',value ='Comandos de diversão e que todos podem usar! Ex: kiss,hug e deathnote.',inline = False)
    embed.set_footer(text='comando realizado por {}| Bot Oficial Hashirama Senju 🔪'.format(ctx.message.author.name))
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando ajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
@bot.command(pass_context = True)
async def modajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Comandos Moderação Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'a!kick ',value ='como usar ``a!kick @usuário`` Expulsa o usuário marcado',inline = False)
    embed.add_field(name = 'a!ban ',value ='Como usar ``a!ban @usuário`` bane o usuário marcado',inline = False)
    embed.add_field(name = 'a!addcargo ',value ='Como usar ``a!addrole @role @usuário`` adiciona um determinado cargo ao usuário marcado',inline = False)
    embed.add_field(name = 'a!removerole',value ='Como usar ``a!removercargo @role @usuário`` remove um determinado cargo do usuário marcado ',inline = False)
    embed.add_field(name = 'a!clear',value ='Como usar ``a!clear`` apaga as mensagens do canal de texto atual ',inline = False)
    embed.add_field(name = 'a!avisar',value ='Como usar ``a!avisar @usuário`` avisa um usuário no PV ',inline = False)


    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando modajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
@bot.command(pass_context=True)
async def pergunta(ctx, *, pergunta: str = None):
    if not pergunta:
        return await bot.say("Você precisa perguntar alguma coisa.")
    else:
        resposta = choice(['Sim', 'Não', 'Talvez', 'Nunca', 'Claro'])
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(name="Pergunta:", value='{}'.format(pergunta), inline=False)
        embed.add_field(name="Resposta:", value=resposta, inline=False)
        await bot.say(embed=embed)
        print('comando roleta digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    
    
   
   
@bot.command(pass_context=True)
async def diversaoajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = 'a!dance ',value ='Como usar ``a!dance`` dance com algum usuário',inline = False)
    embed.add_field(name = 'a!kiss ',value ='Como usar ``a!kiss @usuário`` O amor esta no ar! beije determinado usuário!',inline = False)
    embed.add_field(name = 'a!hug ',value ='Como usar ``a!abraçar @usuário`` abrace seu/sua melhor amigo(a).',inline = False)
    embed.add_field(name = 'a!flipcoin ',value ='Como usar ``a!flipcoin`` Cara ou coroa?',inline = False)
    embed.add_field(name = 'a!deathnote ',value ='Como usar ``a!deathnote @usuário`` Escreva o nome de determinado usuário em seu Death Note ',inline = False)
    embed.add_field(name = 'a!avatar ',value ='Como usar ``a!avatar @usuário`` Veja o avatar do usuário',inline = False)
    embed.add_field(name="a!meme", value="como usar ``a!meme`` que tal ver alguns memes?!", inline=False)
    embed.add_field(name="a!ping", value="como usar ``a!ping`` Veja meu tempo de resposta!", inline=False)
    embed.add_field(name="a!userinfo", value="como usar ``a!userinfo @usuário`` Veja o perfil de um determinado usuário!", inline=True)
    embed.add_field(name="a!voadora", value="como usar ``a!voadora @usuário`` de uma voadora em alguem!", inline=True)
    embed.add_field(name="a!brigar", value="como usar ``a!brigar @usuário`` Use esse comando se alguem estiver merecendo apanhar!", inline=True)  	
    embed.add_field(name="a!matar", value="como usar ``a!matar @usuário`` Use esse comando se alguem estiver merecendo!", inline=True)
    embed.add_field(name="a!slap", value="como usar ``a!slap @usuário`` Use esse comando se alguem estiver merecendo levar uns tapa cabuloso", inline=True)
    embed.add_field(name="a!falar", value="como usar ``a!falar <msg>`` Faça eu falae alguma coisa!", inline=True)
    embed.add_field(name="a!suicidio", value="como usar ``a!suicidio`` suicidio💔", inline=True)
    embed.add_field(name="a!kepiada", value="como usar ``a!kepiada`` Que tal uma piada?!", inline=True)
    embed.add_field(name="a!atack", value="como usar ``a!atack @usuário`` use este comando para atacar alguem!", inline=True)
    embed.add_field(name="a!chorar", value="como usar ``a!chorar`` Chorar faz bem para os olhos...", inline=True)
    embed.add_field(name="a!votar", value="como usar ``a!votar`` Faça uma votação em seu servidor", inline=True)
    embed.add_field(name="a!pergunta", value="como usar ``s!pergunta`` me faça uma pergunta!", inline=True)
    embed.add_field(name="a!shippar", value="como usar ``s!shippar <user> <user>`` Veja Se Um Casal Daria certo!", inline=True)
        
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando diversaoajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))  
      
@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if message.content.lower().startswith('a!shippar'):
		try:
			nome = message.mentions[0].name
			nome2 = message.mentions[1].name
			nome3 = len(nome2)
			nome4 = nome3 - 4
			nome5 = nome[0:4]
			nome6 = nome2[nome4:nome3]
			nome7 = nome5 + nome6
			pessoa = message.author.name
			porcentagem = random.randint(10, 100)
			voce = message.author.mention
			voce1= message.author.name
			shippar = discord.Embed(title='Será que essa "Shippada" vai ser o Futuro?',
			description='**O(a) {} Shippou {} com {}! \n {} % de chance de ser VERDADE.\n Junção dos nomes: {}** '.format(voce,message.mentions[0].mention,message.mentions[1].mention,porcentagem, nome7), color=COLOUR,
			timestamp=datetime.datetime.utcnow())
			shippar.set_image(url="https://media.giphy.com/media/eBb2guj7V5I5M5lL3t/giphy.gif")
			shippar.set_author(name=pessoa, icon_url=message.author.avatar_url)
			shippar.set_thumbnail(url='https://i.imgur.com/743dfAe.png')
			shippar.set_footer(text='comando realizado por {} | Hashirama Senju Oficial'.format(voce1))
			await bot.send_message(message.channel, embed=shippar)
		except IndexError:
			await bot.send_message(message.channel, "{} Você não mencionou dois usuarios".format(message.author.mention))
@bot.command(pass_context=True)
async def chorar(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943338/tumblr_mchb17x02w1r5patso2_500.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943336/0319d0c4d6ce1750c2fc7b3c5d383723db18d37dr1-500-284_00.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648034643972/86a31db739b7f40d576c90f1ff9329ab254958f0_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913647610757130/cfd934eac0f14d3f43284b16ec0a902b.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Chorar...',  description='😭| **{}** Esta chorando...'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | Hashirama Senju Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando chorar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))    
	

bot.run(str(os.environ.get('BOT_TOKEN')))


