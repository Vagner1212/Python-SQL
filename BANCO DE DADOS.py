import mysql.connector

Dados = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="7788394142",
    database="livraria")
cursor = Dados.cursor()
tabela = ("INSERT INTO Livros"
          "(ID, Titulo, Autor, Editora, Ano_Publicacao, Num_Paginas, Disponibilidade)"
          "VALUES (%s, %s, %s, %s, %s, %s, %s )")
dados_Livraria = (
    ['1', 'Orçamento sem falhas', 'Nath Finanças', 'Intrínseca', '2020', '128', '0'],
    ['2', 'Minha Sombria Vanessa', 'Kate Elizabeth Russell', 'Intrínseca', '2020', '432', '1'],
    ['3', 'Recursão', 'Blake Crouch', 'Intrínseca', '2020', '320', '1'],
    ['4', 'M, o Filho do Século', 'Antonio Scurati', 'Intrínseca', '2020', '816', '1'],
    ['5', 'Oblivion Song: Entre Dois Mundos', 'Robert Kirkman', 'Intrínseca', '2020', '136', '0'],
    ['6', 'Não se humilha, não', 'Isabela Freitas', 'Intrínseca', '2020', '320', '1'],
    ['7', 'Os segredos que guardamos', 'Lara Prescott', 'Intrínseca', '2020', '368', '0'],
    ['8', 'Baby Shark!', 'Stevie Lewis', 'Intrínseca', '2020', '32', '1'],
    ['9', 'A Guerra Pela Uber', 'Mike Isaac', 'Intrínseca', '2020', '464', '1'],
    ['10', 'Cidade nas Trevas', 'Adam Christopher', 'Intrínseca', '2020', '384', '0'],
    ['11', 'Território Lovecraft', 'Matt Ruff', 'Intrínseca', '2020', '352', '1'],
    ['12', 'A última porta', 'Scott Cawthon', 'Intrínseca', '2020', '336', '1'],
    ['13', 'A Última Festa', 'Lucy Foley', 'Intrínseca', '2020', '304', '1'],
    ['14', 'Uma chance de lutar', 'Elizabeth Warren', 'Intrínseca', '2020', '400', '0'],
    ['15', 'Uma Dor Tão Doce', 'David Nicholls', 'Intrínseca', '2020', '384', '1'],
    ['16', 'DUPLICADO Este é o Mar', 'Mariana Enriquez', 'Intrínseca', '2020', '176', '0'],
    ['17', 'A Última Festa', 'Lucy Foley', 'Intrínseca', '2020', '304', '1'],
    ['18', 'Coragem', 'Raina Telgemeier', 'Intrínseca', '2020', '224', '1'],
    ['19', 'A Convenção das Aves', 'Ransom Riggs', 'Intrínseca', '2020', '320', '0'],
    ['20', 'Como o Cérebro Cria', 'David Eagleman', 'Intrínseca', '2020', '304', '1'])



cursor.executemany(tabela, dados_Livraria)
Dados.commit()
cursor.close()
Dados.close()
