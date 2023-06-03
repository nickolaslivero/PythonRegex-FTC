#Aluno : Nickolas Javier Santos Livero - 2115310042
#Sistemas de Informação - FTC - Prof. Dr. Elloa B. Guedes

import re


try:
    entrada = input().split()
except EOFError:
    entrada = "false".split()


def verificar_nome():
    nome = entrada[0]
    match0 = re.search(r'[a-zA-Z]*([a-zA-Z0-9]+)', nome)
    contstr = 0
    contnum = 0
    if nome[:1].isalpha() and match0.group():
        for i in range(len(nome) + 1):
            if nome[i - 1:i].isalpha():
                contstr += 1
            if nome[i - 1:i].isnumeric():
                contnum += 1
        if contstr >= contnum:
            return "True"
        else:
            return "False"
    else:
        return "False"


def verificar_senha():
    senha = entrada[1]
    match1 = re.search(r'(([A-Z0-9]{1,2})\.([A-Z0-9]{1,2})\.([A-Z0-9]{1,2})\.([A-Z0-9]{1,2}))', senha)
    cont = 0
    if match1 != None:
        if senha == match1.group():
            senhalist = senha.split(".")
            for i in range(4):
                temp = senhalist[i]
                if (temp[:1]) == (temp[1:2]) or len(temp) != 2:
                    cont += 1
            if cont != 0:
                return "False"
            else:
                return "True"
    return "False"


def verificar_ip():
    cont = 0
    ip = entrada[2].split(".")
    ipcheck = entrada[2]
    match2 = re.search(r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', ipcheck)
    if match2 and ip[0].isdecimal() and ip[1].isdecimal() and ip[2].isdecimal() and ip[3].isdecimal() and len(ip) == 4:
        for i in ip:
            if int(i) > 255:
                cont += 1

        if cont != 0:
            return "False"

        else:
            return "True"
    else:
        return "False"


def verificar_email():
    email = entrada[3]
    match1 = re.search(r'[a-zA-Z][a-zA-Z0-9#\.]*@[a-z]+([\.][a-z]+)+', email)
    if match1 and email[:1].isalpha():
        return "True"
    else:
        return "False"


def verificar_transacao():
    transacao = entrada[4]
    if re.search(r'pull|push|stash|fork|pop', transacao) != None:
        return "True"
    else:
        return "False"


def verificar_rep():
    rep = entrada[5]
    match1 = re.search(r'[a-z0-9]+([_][a-z0-9]+)*', rep)
    if match1 != None:
        if rep == match1.group():
            return "True"
    return "False"


def verificar_hash():
    hash1 = entrada[6]
    match3 = re.search(r'[a-f0-9]*', hash1)

    if len(hash1) != 32:
        return "False"
    else:
        if hash1.isalnum() and match3.group() == hash1:
            return "True"
        else:
            return "False"


def main():
    # print(verificar_nome())
    # print(verificar_senha())
    # print(verificar_ip())
    # print(verificar_email())
    # print(verificar_transacao())
    # print(verificar_rep())
    # print(verificar_hash())

    final_cont = 0

    list1 = [verificar_nome(), verificar_senha(), verificar_ip(), verificar_email(), verificar_transacao(),
             verificar_rep(), verificar_hash()]

    # print()

    for i in range(len(list1)):
        if list1[i] != "False":
            pass
        else:
            final_cont += 1

    if final_cont != 0:
        print("False")

    else:
        print("True")


try:
    if len(entrada) == 7:
        main()
    else:
        print("False")
except IndexError:
    print("False")

'''''''''
1.Nome: OK
sempre iniciados por caracteres alfabéticos.
quantidade de caracteres numéricos não pode superar o número de caracteres alfabéticos. 
São válidos: elloa, jessicaLopes, ell04, el104h, elloaBGuedes, Elloa;

2. Senha: OK
são compostas de 4 pares de dígitos. 
podem ser letras de A até F e números de 0 a 9 e que são separados por ponto. 
duas letras não podem aparecer juntas e nenhum par de números pode ter dígitos iguais. 
Senhas válidas: 03.A5.2B.F8, 14.35.28.92

3. IP do autor: OK
É um número de 32 bits dividido em 4 octetos de bytes representados no formato decimal.
São de IPs válidos: 192.168.1.2, 127.0.0.1, 255.255.255.255;

4. E-mail do autor: OK
o início é feito com uma letra,um arroba, e pelo menos um ponto após o arroba. 
São válidos: ebgcosta@uea.edu.br, elloa.uea@gmail.com, c4rl0s@teste.com.au;

5. Tipo da transação: OK
pull, push, stash, fork e pop;

6. Repositório: OK
snake_case utilizando apenas letras minúsculas do alfabeto.
São válidos: projeto_ftc, pp1_ftc_uea, projetoftc;

7. Hash: 
32 dígitos formados por números de 0 a 9 ou caracteres de a até f em minúsculo.
'''''''''