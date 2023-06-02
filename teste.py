import PySimpleGUI as sg
import mysql.connector
import pandas as pd

sg.theme('DarkAmber')

# Cria o layout com a imagem de fundo e os outros elementos da tela de login
layout_login = [
    [sg.Image(filename='######', pad=((56, 0), (10, 0)))],
    [sg.Text('Usuário', pad=((10, 0), (10, 20))), sg.Input(key='-USER-', size=(20, 30))],
    [sg.Text('Senha', pad=((10, 0), (10, 20))), sg.Input(key='-PASS-', password_char='*', size=(20, 50))],
    [sg.Text('')],
    [sg.Button('Entrar', size=(10, 2)), sg.Button('Cancelar', size=(10, 2))]
]

# Cria a janela de login
window_login = sg.Window('Bem Vindo ao Python', layout_login, element_justification='c', size=(500, 400))

# Loop de eventos da tela de login
while True:
    event, values = window_login.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    if event == 'Entrar':
        # Verifica se as credenciais de login estão corretas
        if values['-USER-'] == 'vagner' and values['-PASS-'] == '7788':
            sg.popup('Login realizado com sucesso!')
            # Fecha a janela de login
            window_login.close()

            # Cria a conexão com o banco de dados
            db = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="7788394142",
                database="brasileirao"
            )

            # Carrega as informações da tabela 'artistas' em um DataFrame
            df = pd.read_sql('SELECT * FROM tabela', con=db)

            # Fecha a conexão com o banco de dados
            db.close()

            # Cria a janela principal com a tabela de artistas
            sg.theme('DarkAmber')
            layout_main = [
                [sg.Text('Bem-vindo ao banco de dados BANDAS DE ROCK!', font=('Helvetica', 18))],
                [sg.Text('', size=(1, 3))],  # espaço extra
                [sg.Table(values=df.values.tolist(), headings=df.columns.tolist(), auto_size_columns=False,
                          col_widths=[10 for _ in range(len(df.columns))],
                          justification='center',
                          num_rows=min(25, len(df))  # define o número máximo de linhas exibidas na tabela
                          )],
                [sg.Text('', size=(1, 3))],  # espaço extra
                [sg.Button('Sair', size=(10, 2))]
            ]

            window_main = sg.Window('Banda de Rock', layout_main, element_justification='c', size=(600, 500))

            # Loop de eventos da página principal
            while True:
                event, values = window_main.read()
                if event == sg.WIN_CLOSED or event == 'Sair':
                    break

            # Fecha a janela da página principal
            window_main.close()
            break
        else:
            sg.popup('Usuário ou senha incorretos')

# Fecha a janela de login
window_login.close()
