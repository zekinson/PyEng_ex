# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

b = False
while b != True:
	ip = input('Введите IP-адрес в формате "10.0.1.1": ').split('.')
	ip_s = '.'.join(ip)
	a = False
	if ip_s.replace('.', '').isdigit():
		for i in ip:
			if i == '':
				a = True
				break
			if int(i) < 0 or int(i) > 255:
				a = True
				break
	else:
		a = True
	if ip_s.count('.') != 3 or  a:
		print('Неправильный IP-адрес')
	else:
		b = True

if int(ip[0]) >= 1 and int(ip[0]) <= 223:
	print('unicast')
elif int(ip[0]) >= 224 and int(ip[0]) <= 239:
	print('multicast')
elif ip_s == '255.255.255.255':
	print('local broadcast')
elif ip_s == '0.0.0.0':
	print('unassigned')
else:
	print('unused')
