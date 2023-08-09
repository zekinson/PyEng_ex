# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
mode = dict()
mode['access'] = access_template
mode['trunk'] = trunk_template
mode_vlan = dict()
mode_vlan['access'] = 'Введите номер VLAN:'
mode_vlan['trunk'] = 'Введите разрешенные VLANы:'
inter = input('Введите режим работы интерфейса (access/trunk): ')
inter_tip = input('Введите тип и номер интерфейса: ')
vlan = input(mode_vlan[inter])
print()
print('interface', inter_tip)
for i in mode[inter]:
	print(i.replace('{}', vlan))
