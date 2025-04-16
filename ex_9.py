primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))
media = (primeira_nota + segunda_nota + terceira_nota)/3

if media >= 7:
    print(f"Sua média foi {media} e você foi aprovado!")
elif (media < 7) and (media > 5):
    print(f"Sua média foi {media} e você ficou de recuperação!")
else:
    print(f"Sua média foi {media} e você foi reprovado!")