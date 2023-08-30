import mysql.connector
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "nave",
)
#nome = input("Digite o nome")
#login = input("Digite a login")
#senha = input("Digite o senha")
cursor = conexao.cursor()

#comando = "select * from tb_login"
#comando = f'insert into tb_login(nome,login,senhmoniq) values("{nome}","{login}","{senha}")'

comando = "delete from tb_login where id=2"
cursor.execute(comando)

#resultado = cursor.fetchall()
conexao.commit()
#print(resultado)


print("Cadastrado")