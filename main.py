import tkinter as tk

# Create the main window
janela = tk.Tk()
janela.title("Calculator")
janela.geometry("300x400")
janela.configure(bg="#e0e0e0")

# Variable to store the input
expressao = ""

# A display to show the values
entrada_texto = tk.StringVar()
display = tk.Entry(janela, font=("Arial", 24), textvariable=entrada_texto, 
                   bd=10, insertwidth=4, width=14, justify='right', bg="#f0f0f0")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Calculator functions

# Add a digit to the expression
def adicionar_dig(digito):
  global expressao
  expressao += str(digito)
  entrada_texto.set(expressao)

# Clean the display  
def limpar_entrada():
  global expressao
  expressao = ""
  entrada_texto.set(expressao)

# Calculate the expression using the eval function, if an error occurs, show "Error"
def calcular():
  global expressao
  try:
    resultado = eval(expressao)
    expressao = str(resultado)
    entrada_texto.set(expressao)
  except:
    entrada_texto.set("Error")
    expressao = ""

# A index to store the buttons
botoes = [
  '1', '2', '3', '+',
  '4', '5', '6', '-',
  '7', '8', '9', '*',
  '0', '.', '=', '/'
]    

# Positionate the buttons in the grid

linha=1
coluna=0

for botao in botoes:
  if botao == '=':
    # Generate the equal button comparing the symbol on the index "botoes"
    tk.Button(janela, text=botao, padx=20, pady=20, font=("Arial", 12),
              command=calcular, bg="#ff9500", fg="white").grid(row=linha, column=coluna)
  else:
    if botao in '0123456789.':
      cor = "#d9d9d9"
    else:
      cor ="#ff9500"
    # Generate numeric buttons comparing the symbol on the index "botoes"  
    tk.Button(janela, text=botao, padx=20, pady=20, font=("Arial", 12),
                command=lambda b=botao: adicionar_dig(b), bg=cor).grid(row=linha, column=coluna)
      
  coluna += 1
  if coluna > 3:
    coluna = 0
    linha += 1

# The Clear button

tk.Button(janela, text="C", padx=20, pady=20, font=("Arial", 12),
          command=limpar_entrada, bg="#fc5a03", fg="white").grid(row=5, column=0, 
                                                                 columnspan=4, sticky="we")   
janela.mainloop()