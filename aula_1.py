def write_names():
    with open('names.txt', 'a', encoding="UTF-8") as file:
        while True:
            name = input('\nNome: ')
            idade = int(input('Idade: '))
            sexo = input('Sexo: ')
            phone = int(input('Phone: '))
            file.write(f'{name}|{idade}|{sexo}|{phone}\n')
            escape = int(input('Deseja sair? digite 0: '))
            if escape == 0:
                break


def read_names():
    with open('names.txt', 'r', encoding="UTF-8") as file:
        people = file.read()
        for person in people.split('\n'):
            print(person)


def main():
    if __name__ == '__main__':
        write_names()
        read_names()

main()
