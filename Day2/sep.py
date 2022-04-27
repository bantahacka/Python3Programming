#! /usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print("-" * len(Belgium))
Belgium = Belgium.replace(',', ':')
print(Belgium)
belg_split = Belgium.split(':')
print("Population of Belgium + Brussels:", int(belg_split[1]) + int(belg_split[3]))
print("-" * len(Belgium))