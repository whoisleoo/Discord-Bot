import requests
import discord
import pdf2image
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default();
intents.message_content = True;

bot = commands.Bot(command_prefix='!', intents=intents);
        #Link do PDF de todos os ensalamentos.
url = "https://guarapuava.camporeal.edu.br/content/uploads/2025/04/Ensalamentos_-PRE-PROVAS-noturno-03.04-e-04.04.2025-1.pdf";



@bot.event
async def on_ready():
    print(f'☑️ Bot conectado como {bot.user}');
    sincronizado = await bot.tree.sync();
    print(f'👨‍💻 {len(sincronizado)} comandos registrados.');

@bot.tree.command(name="horarios", description="📋 ver o ensalamento de cada curso")       
@app_commands.describe(curso="Cursos Disponiveis (engsoft, biomed, direito)")
async def horarios(interaction: discord.Interaction, curso: str = None):
    await interaction.response.defer();
    response = requests.get(url, stream=True);

    if response.status_code == 200:
        with open('ensalamento.pdf', 'wb') as f:
            f.write(response.content);
    else:
        await interaction.followup.send(f'O PDF provavelmente está desatualizado. ERROR: {response.status_code}');
        return;

    images = pdf2image.convert_from_bytes(response.content);

    #Lista dos cursos representando a página do PDF.
    paginaCursos = {
        "engsoft" : 6,
        "biomed" : 1,
        "direito" : 2
    }

    if curso is None:
        await interaction.followup.send("⚠️ Digite ** /horarios <seu curso> ** para verificar os horários.");
        return;

    curso = curso.lower();

    if curso in paginaCursos:
        pagina = paginaCursos[curso];
        image_path = f"horarios_{curso}.png";
        images[pagina].save(image_path, "PNG");

        await interaction.followup.send(f"**🕒 Segue o hórario para {curso.upper()}:**", file=discord.File(image_path));
    else:
        await interaction.followup.send("**❌ Curso não foi encontrado.**");

        
bot.run('');