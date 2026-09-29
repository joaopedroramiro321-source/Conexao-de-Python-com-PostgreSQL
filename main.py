from conecao import conexao, encerrar_conexao

def main():
    conection = conexao()

    cursor = conection.cursor()
    cursor.execute('SELECT * FROM saidas')

    rows = cursor.fetchall()

    print(rows)

    encerrar_conexao(conection)

if __name__ == '__main__':
    main()