# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def dvoih(a):
	a = str(bin(a)[2:])
	while len(a) != 8:
		a = '0' + a
	return a


def des(a):
	a = list(a)
	a.reverse()
	des = 0
	st = 0
	for i in a:
		if i == '0':
			st += 1
			continue
		des += int(i) * 2 ** st
		st += 1 
	return(str(des))


def vevod(a, b):
	print(a[0].ljust(8), a[1].ljust(8), a[2].ljust(8), a[3], sep='  ')
	print(b[0], b[1], b[2], b[3], sep='  ')


ip = input('Введите IP-сети: ')
net = ip.split('/')[0].split('.')
mask = ip.split('/')[1]
# Network
print('Network:')
net_2 = [dvoih(int(num)) for num in net]
vevod(net, net_2)
print()
# Mask
print('Mask:')
print('/' + mask)
mask = int(mask)
mask_str = '1' * mask + '0' * (32 - mask)
mask_list = [mask_str[i * 8: (i + 1) * 8] for i in range(4)]
mask_list_des = [des(i) for i in mask_list]
vevod(mask_list_des, mask_list)
