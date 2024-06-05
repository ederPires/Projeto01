# importa pacote
from fpdf import FPDF
import locale

projeto = input("Digite a descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")

valor_projeto = int(horas_previstas) * int(valor_hora)

# Configura a localização para Português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Função para formatar o número como moeda brasileira
def formatar_real(valor):
    return locale.currency(valor, grouping=True)

# Exemplo de uso
# numero = 2000
valor_projeto_formatado = formatar_real(valor_projeto)

# cria o pdf vazio
pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)

#coordenadas x e y + texto
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, valor_projeto_formatado)

print("Orçamento gerado com sucesso!")
pdf.output("Orçamento.pdf")
