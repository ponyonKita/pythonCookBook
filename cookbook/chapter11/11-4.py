# CIDR주소로 IP생성

# 여기서 표현하는 IP 주소를 모두생성
import ipaddress
net = ipaddress.ip_network('123.45.67/27') # CIDR네트워크
print(net)

print(net.num_addresses) # 배열로 접근가능

net2 = ipaddress.ip_interface('123.45.67/27')
print(net2.netmask)
print(net2.ip)


#네트워크 주소를 다루는 코드를 작성할때 유용함
# ip주소를 사용할땐 str로 변환해서 사용해야함

