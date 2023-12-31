# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный
поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ip = "192.168.3.1"
ip = ip.split('.')
kod_list = []
for i in ip:
	i = int(i)
	kod = []
	while i != 1:
		kod.append(str(i % 2))
		i //= 2
	kod.append('1')
	kod.reverse()
	while len(kod) != 8:
		kod.insert(0, '0')
	kod_list.append(''.join(kod))
kod = kod_list
print(ip[0].ljust(10) + ip[1].ljust(10) + ip[2].ljust(10) + ip[3])
print(kod[0] +'  ' + kod[1] +'  ' + kod[2] +'  ' + kod[3])
