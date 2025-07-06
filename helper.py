import re
import consts
import search

# Перевод длинной команды
def parser(raw) -> str:
    answer = []
    if len(raw) > 6:
        return consts.unknown(' '.join(raw))
    for i in range(len(raw) - 1):
        if i % 2 == 0:
            match raw[i]:
                case _ if raw[i] in consts.__f:
                    answer.append(save_path([raw[i], raw[i + 1]]))
                case _ if raw[i] in consts.__s:
                    answer.append(save_search([raw[i], raw[i + 1]]))
                case _ if raw[i] in consts.__d:
                    answer.append(save_destination([raw[i], raw[i + 1]]))
                case _:
                    return consts.unknown(' '.join(raw))
    return '\n'.join(answer)


def save_path(command):
    if len(command) == 1:
        f = input('Input path to file for search: ')
        search.File = f
        return consts.__path_to_file
    elif len(command) == 2:
        search.File = command[1]
        return consts.__path_to_file
    return consts.invalid(' '.join(command))


def save_search(command):
    if len(command) == 1:
        s = input('Input word or sentence string: ')
        search.Search = s
        return consts.__w_or_s
    elif len(command) == 2:
        search.Search = command[1]
        return consts.__w_or_s
    return consts.invalid(' '.join(command))


def save_destination(command):
    if len(command) == 1:
        d = input('Input destination path: ')
        search.Destination = d
        return consts.__destination
    elif len(command) == 2:
        search.Destination = command[1]
        return consts.__destination
    return consts.invalid(' '.join(command))


def remove_not_necessarily_symbols(text):
    return re.sub(r'(\s|!|\.|,|;|:|\?|\'|\"|<|>|/|\\|@|#|$|%|^|&|\*|\(|\)|`|~)+', ' ', text).strip()