import mysql.connector
from mysql.connector import errorcode

print("@ connecting... ")

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='****',
        password='****'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(err)

cursor = conn.cursor()


cursor.execute("CREATE DATABASE IF NOT EXISTS `jogoteca`;")


cursor.execute("USE `jogoteca`;")

TABLES = {}

TABLES['Jogos'] = ('''
    CREATE TABLE IF NOT EXISTS `Jogos` ( 
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `nome` varchar(50) NOT NULL,
    `categoria` varchar(40) NOT NULL,
    `console` varchar(20) NOT NULL,
    PRIMARY KEY(`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')

TABLES['Usuarios'] = ('''
    CREATE TABLE IF NOT EXISTS `Usuarios` (
    `nome` varchar(20) NOT NULL,
    `nickname` varchar(8) NOT NULL,
    `senha` varchar(100) NOT NULL,
    PRIMARY KEY(`nickname`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')


for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('@@ Creating Table... {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        print('@@ Creating Table... OK')


