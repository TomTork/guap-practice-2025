import consts
import helper

Destination = 't'
Search = ''
File = ''
Data = ''

def run() -> str:
    global Destination, Search, File, Data

    if not Search.strip():
        return consts.primary('Search pattern is empty!')

    result = []
    search_text = helper.remove_not_necessarily_symbols(Search.lower())
    source_text = Data.lower()

    translated_text = helper.remove_not_necessarily_symbols(source_text)
    search_numerate = []
    translated_numerate = []
    for word in search_text.split():
        search_numerate.append(word)
    pos = 0
    for word in translated_text.split():
        start_pos = source_text.find(word, pos)
        translated_numerate.append((word, start_pos))
        pos = start_pos + len(word)

    for i in range(len(translated_numerate)):
        ans_start_pos = -1
        ans_end_pos = -1
        for index in range((len(search_numerate))):
            if i + index >= len(translated_numerate):
                break
            state = check_run_levenshtein(translated_numerate[i + index][0], search_numerate[index])
            if -1 < state <= get_degree_of_error(search_numerate[index]):
                if index == 0:
                    ans_start_pos = translated_numerate[i + index][1]
                if index == len(search_numerate) - 1:
                    ans_end_pos = translated_numerate[i + index][1] + len(translated_numerate[i + index][0])
            else:
                break
        if ans_start_pos != -1 and ans_end_pos != -1:
            result.append((ans_start_pos, ans_end_pos, Data[ans_start_pos:ans_end_pos]))
    if Destination != 't':
        f = open(Destination, 'w', encoding='utf-8')
        f.write(str(result))
        return f'Saved to {Destination}'
    return str(result)


def check_run_levenshtein(s1, s2):
    if abs(len(s1) - len(s2) > 4):
        return -1
    return levenshtein_distance(s1, s2)


# Получить степень допустимой ошибки
def get_degree_of_error(s):
    if len(s) <= 2:
        return 0
    if len(s) <= 4:
        return 1
    if len(s) <= 6:
        return 2
    if len(s) <= 8:
        return 3
    return 4


# Расстояние Левенштейна
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    prev_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1, 1):
        curr_row = [i]
        for j, c2 in enumerate(s2, 1):
            curr_row.append(min(
                prev_row[j] + 1,  # Операция удаления
                curr_row[j - 1] + 1,  # Операция вставки
                prev_row[j - 1] + (0 if c1 == c2 else 1)  # Операция замены
            ))
        prev_row = curr_row
    return prev_row[-1]