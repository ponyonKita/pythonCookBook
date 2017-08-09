
# 임의 순환체 요소 나누기



recoad = ('dave', 'dave@email.com', '34345-2344', '1234-1234')
name, email, *phoneNumbers = recoad
print(phoneNumbers)


records = [('foo', 1,2), ('bar', 'hello'), ('foo',1,2)]


def do_foo(x,y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag =='foo':
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)


line = 'nobody:8:-2:2:Unprivileged User:/var/empty:/use/line/bin/false'
uname, *fields, homedir, sh = line.split(':')

print(uname)
print(homedir)
print(sh)

record = ('ac', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)
print(*_)

items = [1,2,3,4,5,6]
def sum(items):
    head, *tail = items
    print('tail', *tail)
    return head + sum(tail) if tail else head

print(sum(items))