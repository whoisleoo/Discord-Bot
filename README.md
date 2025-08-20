
# // 👨‍💻 Discord Bot

Um bot criado em python que puxa o PDF de ensalamento das aulas da faculdade Campo Real e as envia pelo Discord atraves do comando "/horarios".




# Como Usar

Primeiramente, é necessário criar um bot no discord, você pode fazer isso pelo       

Discord Developer Portal:
[![Dev Portal](https://img.shields.io/badge/discord-000?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/developers/applications)

* **Após a criação, entre na aba "BOT" e copie o link do Token, e cole dentro do código "bot.run('')".**

* **Dentro da aba "OAuth2" selecione as categorias "bot" "applications_command" e "Administrator".**                                                                                                                                   
Feito isso, o link para invite do bot será criado, copie e cole ele em seu navegador e selecione seu servidor.

Antes de iniciar seu código, é necessário as seguintes bibliotecas:

* **pip install requests**
* **pip install discord**
* **pip install pdf2image**

Se mesmo assim, o código encontrar um erro sugiro que instale o **poppler**.
Você pode estar instalando ele [aqui](https://github.com/oschwartz10612/poppler-windows/releases).
Não esqueça de colocar o poppler no seu **PATH**.

Feito isso, inicie o **bot.py**.

**Pronto!**  ✔️  
Teste utilizando o comando **"/horarios".**


# Updates

* **Foi criado um sistema que puxa a Data e aplica no PDF, não é 100% preciso já que infelizmente o programa é dependente das atualizações diarias do PDF.**

**Lista dos cursos disponiveis para pesquisa:**
- [X] Bio Medicina 
- [X] Engenharia de Software 
- [X] Direito
- [X] Psicologia
- [X] Fisioterapia 
- [ ] Engenharia Mecanica 
- [ ] Arquitetura 
- [ ] Administração
- [ ] Enfermagem

*obs: a ideia pra esse projeto vai pro meu amigo Gabriel.*
