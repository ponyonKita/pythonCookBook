
#유니테스트에서 객체 패치
# 특정 파라미터와 함께 호출 되었는지 선택한 속성에 접근했는지
from unittest.mock import patch
import example

# 데코레이터로 패치
@patch('example.func')
def test1(x, mock_func):
    example.func(x)
    mock_func.assert_called_with(x)


# 콘텍스트 매니저로 패치
with patch('example.func') as mock_func:
    example.func(x)
    mock_func.assert_called_with(x)


# 수동패치
p = patch('example.func')
mock_func = p.start()
example.func(x)
mock_func.assert_called_with(x)
p.stop()



# 여러가지 객체 패치

@patch('example.func1')
@patch('example.func2')
@patch('example.func3')
def test1(mock1, mock2, mock3):
    pass


def test2():
    with patch('example.patch1') as mock1, patch('example.patch2') as mock2, patch('example.patch3') as mock3:
        example.func(x)
        mock_func.assert_called_with(x)


x = 42
with patch('__main__'.x):
    print(x)


with patch('__main__'.x, 'patched_value'):
    print(x)

