import sys
from lib.text import normalize, tokenize, count_freq, top_n

def main():

    line = sys.stdin.read() #Читает весь ввод до конца файла. Сtrl+Z+Enter для прерывания ввода
    
    norm_line = tokenize(line)
    uniq_line = len(set(norm_line))
    dict = count_freq(norm_line)
    top5 = top_n(dict, 5)


    print('Всего слов:', len(norm_line))
    print('Уникальных слов:', uniq_line)
    print('Топ-5:')
    for i in top5:
        print( f'{i[0]}:{i[1]}') 

if 1 == 1:
    main() #вызов функции



