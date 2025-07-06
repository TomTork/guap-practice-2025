import consts
import helper
import search
import shlex

print(consts.__help)

while consts.__run:
    command = shlex.split(input('——> '))
    match command[0]:
        case 'run':
            print(search.run())
        case '-F':
            print(search.File)
        case '-S':
            print(search.Search)
        case '-D':
            print(search.Destination)
        case _ if command[0] in consts.__q:
            print('Exiting...')
            consts.__run = False
        case _ if command[0] in consts.__h:
            print(consts.__help)
        case _ if command[0] in consts.__f and len(command) <= 2:
            print(helper.save_path(command))
        case _ if command[0] in consts.__s and len(command) <= 2:
            print(helper.save_search(command))
        case _ if command[0] in consts.__d and len(command) <= 2:
            print(helper.save_destination(command))
        case _:
            print(helper.parser(command))