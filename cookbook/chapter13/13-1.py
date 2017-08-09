#리다이렉션, 파이프 입력파일을 통한 스크립트 입력받기

# /Users/bhkim/pythonCookBook/cookbook/passwd.txt
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        #print(line, end='')
        print(line, end='')




# python3 ./13-1.py /etc/passwd