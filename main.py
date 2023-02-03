import mysql.connector

# Conectando ao banco de dados
mydb = mysql.connector.connect(
  host="host_name",
  user="user_name",
  password="password",
  database="database_name"
)

# Criando um cursor para executar comandos SQL
mycursor = mydb.cursor()

# Inserindo dados na tabela
sql = "INSERT INTO table_name (col1, col2, col3) VALUES (%s, %s, %s)"
val = ("value1", "value2", "value3")
mycursor.execute(sql, val)

# Efetuando o commit para salvar a alteração no banco de dados
mydb.commit()

# Exibindo uma mensagem de confirmação
print(mycursor.rowcount, "registro(s) inserido(s) com sucesso.")