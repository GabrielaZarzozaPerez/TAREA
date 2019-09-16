print("Introduce una palabra")
word = str(input())

alrevez_word = reversed(word)

if list(word) == list(alrevez_word):
   print("Es un palindromo")
else:
   print("No es un palindromo")
