import os
import re
import consts
import search
from bs4 import BeautifulSoup  # Библиотека для считывания html
import fitz  # Чтение из pdf
from docx import Document  # Чтение docx
import textract  # Чтение doc

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
        try:
            search.Data = read_file(f)  # Сохраняем значение
            search.File = f
            return consts.__path_to_file
        except BaseException as error:
            return consts.primary(error)
    elif len(command) == 2:
        search.File = command[1]
        try:
            search.Data = read_file(command[1])  # Сохраняем значение
        except BaseException as error:
            return consts.primary(error)
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


def read_html(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
        return soup.get_text()


def read_pdf(path: str) -> str:
    doc = fitz.open(path)
    text = ''
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        text += page.get_text("text") + '\n'
    return text


def read_txt(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def read_docx(path: str) -> str:
    doc = Document(path)
    return '\n'.join(p.text for p in doc.paragraphs if p.text.strip())


def read_doc(path: str) -> str:
    return textract.process(path).decode('utf-8')


def read_file(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    match ext:
        case '.docx':
            return read_docx(path)
        case '.doc':
            return read_doc(path)
        case '.pdf':
            return read_pdf(path)
        case '.html' | '.htm':
            return read_html(path)
        case _:
            return read_txt(path)