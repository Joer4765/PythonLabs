def get_input(text) -> str:
    return text.get('1.0', 'end-1c')


def output(text_obj, text):
    text_obj['state'] = 'normal'
    text_obj.replace('1.0', 'end', text)
    text_obj['state'] = 'disabled'


def arr2text(arr: list) -> str:
    return ' '.join(map(str, arr))


def text2matrix(text: str) -> list:
    return [[int(i) for i in row.split()] for row in text.split('\n')]

