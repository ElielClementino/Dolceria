# Dolceria
[Dolceria Giff](gifProjeto.gif)
### Feito usando como template [huogerac/djavue](https://github.com/huogerac/djavue)

## [Link para o vídeo](https://www.loom.com/share/0e1a43407c5f4090a6fea76bd7a681f2)
## O que é e motivação  

É um projet fullstack com a intenção de construir um site web completo. Eu gosto muito da gastronomia, em especial a confeitaria e minha irmã é formada em gastrônomia e tem um sonho de abrir uma loja de doces, e a gente sempre brincou sobre eu fazer o site e tudo mais, então surgiu esse projeto e eu pensei, porquê não tentar ? mesmo que obviamente só o básico, tentei aplicar o que eu imaginaria que o site teria como fluxo.

## Setup do projeto
Mudar a .env-example para .env

docker compose build 

docker compose up

para acessar o site basta colocar na url http://localhost/

## Ajudinha
-- Caso esteja com os containers do nginx/frontend/postgres rodando e o django fora do container, com python manage.py runserver --  

Para poder facilitar o setup do projeto usando o banco adicionei no root do projeto o arquivo "dump.json"  

Ele tem alguns produtos cadastrados, basta rodar no terminal o seguinte comando para jogar esses arquivos no seu banco de dados.  

    python manage.py loaddata dump.json  


-- Caso esteja rodando todos os ambientes com docker(nginx/frontend/backend/postgres)--

Você irá precisar acessar o container do backend
rodando o comando docker ps, você vai ter os ids dos containers que estão rodando, basta pegar o id do container do backend e rodar o seguinte comando no terminal:

    docker exec -it IDDOCONTAINER bash  

Assim que você entrar no container basta rodar o comando:

    python manage.py loaddata dump.json  

## Criando conta de administrador

Você irá ter que acessar o container do backend da mesma forma descrita acima e rodar o seguinte comando:  

    python manage.py createsuperuser  

 após criar o usuário basta fazer login utilizando a senha e o login que foi definido na criação do super user
