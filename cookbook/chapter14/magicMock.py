

from unittest.mock import MagicMock

m = MagicMock(return_value=10)
print(m(1,2, debug=True))

print(m.assert_called_with(1,2, debug=True))
#print(m.assert_called_with(1,2, test='wow'))

m.upper.return_value = 'HELLO'
print(m.upper('hello'))
assert m.upper.called
m.split.return_value= ['hello', 'world']
print(m.split('hello world'))
print(m.split.assert_called_with('hello world'))

print(m['blsh'])
print(m.__getitem__.called)
print(m.__getitem__.assert_called_with('blsh'))