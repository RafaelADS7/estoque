from tkinter import *
from tkinter import ttk
from tkinter import messagebox

lista_codigos = []

def pesquisar_codigo(entry_codigo, label_resultado):
    codigo = entry_codigo.get()
    texto_resultado = ""
    encontrado = False

    codigo = int(codigo)

    for item in lista_codigos:
        if item['codigo'] == codigo:
            nome = item['nome']
            tipo_unidade = item['tipo_unidade']
            quantidade = item['quantidade']
            valor = item['valor']

            texto_resultado = f'''
            Nome: {nome}
            Tipo da unidade: {tipo_unidade}
            Quantidade: {quantidade}
            Valor: {valor}
            '''
            encontrado = True
            break

    # Se o código não for encontrado
    if not encontrado:
        texto_resultado = "Código não encontrado"

    label_resultado.config(text=texto_resultado)


def dar_saida(entry_codigo, quantidade_saida):
    quantidade_saida = quantidade_saida.get()
    entry_codigo = entry_codigo.get()

    codigo = int(entry_codigo)
    quantidade_saida = int(quantidade_saida)

    for item in lista_codigos:
        if item['codigo'] == codigo:
            if int(item['quantidade']) >= quantidade_saida:
                item['quantidade'] = int(item['quantidade']) - quantidade_saida
                messagebox.showinfo("Sucesso", f"Saída de {quantidade_saida} unidades do produto {item['nome']} registrada com sucesso!")
            else:
                messagebox.showerror("Erro", "Quantidade insuficiente em estoque")


def tela_de_pesquisar():
    janela_pesquisa = Toplevel()
    janela_pesquisa.title('Janela de Pesquisa')
    janela_pesquisa.geometry('600x400')

    texto_tela_pequisa = Label(janela_pesquisa, text="TELA DE PESQUISA")
    texto_tela_pequisa.place(x=250, y=10)

    texto_codigo = Label(janela_pesquisa, text="Codigo")
    texto_codigo.place(x=35, y=50)

    entry_codigo = Entry(janela_pesquisa, width=60)
    entry_codigo.place(x=115, y=50)

    label_resultado = Label(janela_pesquisa, text="", wraplength=500)
    label_resultado.place(x=35, y=120)

    botao_pesquisa = Button(janela_pesquisa, text="Pesquisar código", width=15, height=-10, command=lambda: pesquisar_codigo(entry_codigo, label_resultado))
    botao_pesquisa.place(x=480, y=45)

    texto_resultado = Label(janela_pesquisa, )
    texto_resultado.place(x=35, y=260)

def tela_adicionar_quantidade():
    janela_adicionar = Toplevel()
    janela_adicionar.title('Adicionar Quantidade')
    janela_adicionar.geometry('600x400')

    def adicionar_quantidade():
        try:
            codigo = int(entry_codigo.get())
            quantidade_adicionada = int(entry_quantidade.get())
            for item in lista_codigos:
                if int(item['codigo']) == codigo:
                    item['quantidade'] += quantidade_adicionada
                    messagebox.showinfo("Sucesso", f"Adicionado {quantidade_adicionada} unidades ao produto {item['nome']} com sucesso!")
                    return
            messagebox.showerror("Erro", "Código não encontrado")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos")

    texto_tela_adicionar = Label(janela_adicionar, text="Adicionar Quantidade")
    texto_tela_adicionar.place(x=220, y=10)

    texto_codigo = Label(janela_adicionar, text="Código")
    texto_codigo.place(x=35, y=50)

    entry_codigo = Entry(janela_adicionar, width=60)
    entry_codigo.place(x=115, y=50)

    texto_quantidade = Label(janela_adicionar, text="Quantidade a Adicionar")
    texto_quantidade.place(x=35, y=100)

    entry_quantidade = Entry(janela_adicionar, width=60)
    entry_quantidade.place(x=200, y=100)

    botao_adicionar = Button(janela_adicionar, text="Adicionar", width=15, command=adicionar_quantidade)
    botao_adicionar.place(x=250, y=150)













# COMECO JANELA DE CADASTRO
def tela_cadastro():
    janela_cadastro = Toplevel()
    janela_cadastro.title('Janela de Cadastro')

    def cadastrar_codigo():
        nome = entry_nome.get() 
        tipo_unidade = selecionar_tipo_unidade.get()
        quantidade = entry_quantidade.get()
        valor = entry_valor.get()
        codigo = len(lista_codigos) + 1

        novo_item = {
            "nome": nome,
            "tipo_unidade": tipo_unidade,
            "quantidade": int(quantidade),
            "valor": valor,
            "codigo": int(codigo),
        }

        lista_codigos.append(novo_item)
        print(lista_codigos)
        messagebox.showinfo("Sucesso", f"Produto cadastrado com sucesso!")

    janela_cadastro.title("Tela cadastro")
    janela_cadastro.geometry('600x400')

    lista_tipos = ["Galão", "Caixa", "Unidade", "Saco"]

    texto_tela_cadastro = Label(janela_cadastro, text="TELA DE CADASTRO")
    texto_tela_cadastro.place(x=250, y=10)

    # comeca NOME
    texto_nome = Label(janela_cadastro, text="Nome")
    texto_nome.place(x=35, y=50)

    entry_nome = Entry(janela_cadastro, width=75)
    entry_nome.place(x=115, y=50)
    # TERMINA NOME

    # COMECA TIPO DA UNIDADE
    texto_tipo_unidade = Label(janela_cadastro, text="Tipo da unidade")
    texto_tipo_unidade.place(x=15, y=80)

    selecionar_tipo_unidade = ttk.Combobox(janela_cadastro, values=lista_tipos, width=72)
    selecionar_tipo_unidade.place(x=115, y=80)
    # TERMINA TIPO DA UNIDADE

    # quantidade de itens na unidade+_
    texto_quantidade = Label(janela_cadastro, text="Quant. de itens")
    texto_quantidade.place(x=15, y=110)

    entry_quantidade = Entry(janela_cadastro, width=75)
    entry_quantidade.place(x=115, y=110)
    # quantidade de itens na unidade

    # COMECA VALOR
    texto_valor = Label(janela_cadastro, text="Valor")
    texto_valor.place(x=35, y=140)

    entry_valor = Entry(janela_cadastro, width=75)
    entry_valor.place(x=115, y=140)
    # TEWRMINA VALOR

    # comeco botao
    botao = Button(janela_cadastro, text="Criar código", command=cadastrar_codigo)
    botao.place(x=280, y=180)
    # termiando botao

    print(lista_codigos)

# TERMINO JANELA DE CADASTRO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!







# COMEÇO JANELA DE SAIDA
def tela_saida():
    janela_saida = Toplevel()
    janela_saida.title('Janela de Saída')
    janela_saida.geometry('600x400')

    texto_tela_saida = Label(janela_saida, text="TELA DE SAÍDA")
    texto_tela_saida.place(x=250, y=10)

    texto_codigo = Label(janela_saida, text="Codigo")
    texto_codigo.place(x=35, y=50)

    entry_codigo = Entry(janela_saida, width=60)
    entry_codigo.place(x=115, y=50)

    texto_quantidade = Label(janela_saida, text="Quantidade de Saída")
    texto_quantidade.place(x=35, y=100)

    quantidade_saida = Entry(janela_saida, width=60)
    quantidade_saida.place(x=200, y=100)

    botao_saida = Button(janela_saida, text="Registrar Saída", width=15, command=lambda: dar_saida(entry_codigo, quantidade_saida))
    botao_saida.place(x=250, y=150)

# TERMINO JANELA DE SAIDA













# COMEÇO JANELA DE RELATORIO
def tela_relatorio():
    janela_relatorio = Toplevel()
    janela_relatorio.title('Relatório de Estoque')
    janela_relatorio.geometry('600x400')

    texto_tela_relatorio = Label(janela_relatorio, text="RELATÓRIO DE ESTOQUE")
    texto_tela_relatorio.place(x=220, y=10)

    relatorio_text = Text(janela_relatorio, width=70, height=20)
    relatorio_text.place(x=20, y=50)

    if not lista_codigos:
        relatorio_text.insert(END, "Nenhum item registrado no estoque.\n")
        return

    relatorio_text.insert(END, "Código  | Nome |  Tipo da Unidade | Quantidade | Valor\n")
    relatorio_text.insert(END, "-" * 70 + "\n")

    for item in lista_codigos:
        codigo = item['codigo']
        nome = item['nome']
        tipo_unidade = item['tipo_unidade']
        quantidade = item['quantidade']
        valor = item['valor']
        relatorio_text.insert(END, f"{codigo:^6} | {nome:^15} | {tipo_unidade:^15} | {quantidade:^10} | {valor:^10}\n")

# TERMINO JANELA DE RELATORIO












janela_home = Tk()
janela_home.title('Projeto Gerenciador de estoque')
janela_home.geometry('600x400')

botao_cadastro = Button(janela_home, text='Cadastro', width=10, height=2, command=tela_cadastro)
botao_cadastro.place(x=360)

botao_pesquisa = Button(janela_home, text='Pesquisa', width=10, height=2, command=tela_de_pesquisar)
botao_pesquisa.place(x=440)

botao_saida = Button(janela_home, text='Saída', width=10, height=2, command=tela_saida)
botao_saida.place(x=520)

botao_relatorios = Button(janela_home, text='Relatórios', width=10, height=2, command=tela_relatorio)
botao_relatorios.place(x=280)

nome_gerenciador = Label(janela_home, text='Software', font=("Arial", 18))
nome_gerenciador.place(x=140, y=190)

# Código para adicionar um botão para a tela de adicionar quantidade na janela principal
botao_adicionar_quantidade = Button(janela_home, text='entrada', width=10, height=2, command=tela_adicionar_quantidade)
botao_adicionar_quantidade.place(x=200,)

#botao_entrada = Button(janela_home, text='entrada', width=10, height=2,command=tela_entrada)
#botao_entrada.place(x=200, y=0)

janela_home.mainloop()