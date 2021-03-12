from PyQt5 import uic, QtWidgets
import sqlite3

def gravar():
    conn = sqlite3.connect('db/cadastro.db')
    c = conn.cursor()
    
    nome = tela.input_nome.text()
    cpf = tela.input_cpf.text()
    idade = int(tela.input_idade.text())
    id_departamento = int(tela.input_id_departamento.text())

    c.execute(f"INSERT INTO cliente(nome, cpf, idade, id_departamento) VALUES ('{nome}', '{cpf}', {idade}, {id_departamento});")

    conn.commit()
    conn.close()
    confirmacao.show()

def mostrar():
    conn = sqlite3.connect('db/cadastro.db')
    c = conn.cursor()
    dados = c.execute("SELECT * FROM cliente").fetchall()
    
    tela.tableWidget.setRowCount(len(dados))
    tela.tableWidget.setColumnCount(4)

    tela.tableWidget.verticalHeader().setVisible(False)

    for i in range(0, len(dados)):
        for j in range(0, 4):
            tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))

    conn.close()

app = QtWidgets.QApplication([])

tela = uic.loadUi('UI/tela.ui')
confirmacao = uic.loadUi('UI/confirmacao.ui')

tela.tableWidget.setColumnWidth(0, 350)
tela.tableWidget.setColumnWidth(1, 100)
tela.tableWidget.setColumnWidth(2, 50)
tela.tableWidget.setColumnWidth(3, 100)

tela.bt_gravar.clicked.connect(gravar)
tela.bt_atualizar.clicked.connect(mostrar)

tela.show()
app.exec()
