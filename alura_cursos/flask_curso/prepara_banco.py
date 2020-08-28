import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    port = 3306,
    password="xxxxx",
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()

cursor.execute('create database if not exists jogoteca')
cursor.execute('use jogoteca')
cursor.execute("""create table if not exists jogo(
                id int(11) not null auto_increment,
                nome varchar(50) collate utf8_bin not null,
                categoria varchar(40) collate utf8_bin not null,
                console varchar(20) not null,
                primary key (id)
                )engine=innodb default charset=utf8 collate=utf8_bin"""
               )
cursor.execute("""create table if not exists usuario (
                id varchar(8) primary key not null,
                nome varchar(20) not null,
                senha varchar(8) not null
                )"""
               )

# inserindo usuarios

cursor.executemany(
    'INSERT INTO jogoteca.usuario (id, nome, senha) VALUES (%s, %s, %s)',
    [
        ('luan', 'Luan Marques', 'flask'),
        ('nico', 'Nico', '7a1'),
        ('danilo', 'Danilo', 'vegas'),
        ('david', 'david', '1234')
    ])

cursor.execute('select * from jogoteca.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.executemany(
    'INSERT INTO jogoteca.jogo (nome, categoria, console) VALUES (%s, %s, %s)',
    [
        ('God of War 4', 'Acao', 'PS4'),
        ('NBA 2k18', 'Esporte', 'Xbox One'),
        ('Rayman Legends', 'Indie', 'PS4'),
        ('Super Mario RPG', 'RPG', 'SNES'),
        ('Super Mario Kart', 'Corrida', 'SNES'),
        ('Fire Emblem Echoes', 'Estrategia', '3DS'),
    ])

cursor.execute('select * from jogoteca.jogo')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito
conexao.commit()
conexao.close()