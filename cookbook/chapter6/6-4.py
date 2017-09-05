
# 매우큰 xml파일 증분 파싱하기

from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))

    # 뿌리요소 건너뛰기
    next(doc)


    tag_task =[]
    elem_task=[]

    for event, elem in doc:
        if event == 'start':
            tag_task.append(elem.tag)
        elif event == 'end':
            if tag_task == path_parts:
                yield elem
                elem_task[-2].remove(elem)

        try:
            tag_task.pop()
            elem_task.pop()
        except IndexError:
            pass
