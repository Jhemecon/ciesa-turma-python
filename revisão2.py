aluno = {"nome": "Jhemeson", "idade": 18, "email": "jhemesonconde2017@gmail.com"}

if (len(aluno.get("nome")) > 3):
    print ("Válido")

if (aluno.get("idade") >= 16):
    print ("Válido")

if ("@" in aluno.get("email")):
    print("Válido")

posicao = aluno.get("email").find(("@"))
sub_string = aluno.get("email")[posicao + 1:]

if ("." in sub_string):
    print ("Válido")