import consts
import helper

Destination = 't'
Search = ''
File = ''

def run():
    global Destination, Search, File
    search_text = helper.remove_not_necessarily_symbols(Search.lower())
    try:
        source_text = open(File, 'r').read().lower()
    except BaseException as error:
        return consts.primary(error)
    translated_text = helper.remove_not_necessarily_symbols(source_text)
    search_numerate = []
    translated_numerate = []
    pos = 0
    for word in search_text.split():
        search_numerate.append((word, pos, pos + len(word) - 1))
        pos += len(word) + 1
    pos = 0
    for word in translated_text.split():
        translated_numerate.append((word, pos, pos + len(word) - 1))
        pos += len(word) + 1
    print(search_numerate)
    print(translated_numerate)


    return 'result'