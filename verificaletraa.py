def verifica_letra_a(texto):
  texto_minusculo = texto.lower()
  contagem = texto_minusculo.count('a')
  if contagem > 0:
    return f"A letra aparece {contagem} vezes na string"
  else:
    return f"A letra a não aparece na string"


texto = input("Digite uma string: ")
resultado = verifica_letra_a(texto)
print(resultado)
