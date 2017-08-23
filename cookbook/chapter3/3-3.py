
# 출력을 위한 숫자 서식화

x = 1234.56789

#  소수점 둘째자리
print(format(x, '0.2f'))
# 소수점 한자리 정확도로 문자 10개 기준 오른쪽에서 정렬
print(format(x, '>10.1f'))
# 소수점 한자리 정확도로 문자 10개 기준 왼쪽에서 정렬
print(format(x, '<10.1f'))

#가운데 정렬
print(format(x, '^10.1f'))
# 천단위 구분자
print(format(x, ','))
print(format(x, '0,.1f'))

print(format(-x, '0.1f'))

swap_separators = {ord('.'):',',ord(','):'.'}
print(format(x, ',').translate(swap_separators))

print('%0.2f'%x)
print('%-10.1f'%x)
