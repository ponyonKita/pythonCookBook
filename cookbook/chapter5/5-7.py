

# 압축된 데이터 파일 읽고쓰기

import gzip
with gzip.open('somefilz.gz', 'rt') as f:
    text = f.read()

import bz2
with bz2.open('somefilz.gz', 'rt') as f:
    text = f.read()




import gzip
with gzip.open('somefilz.gz', 'wt') as f:
    f.write(text)

import bz2
with bz2.open('somefilz.gz', 'wt') as f:
    f.write(text)