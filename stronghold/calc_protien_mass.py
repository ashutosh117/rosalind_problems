#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:47:07 2020

@author: t1
"""

PROTIEN_MASS = {}
with open('sample_data/monoisotopic_mass_table.txt') as f:
    for line in f.readlines():
        prot,weight = line.split()[0],float(line.split()[1])
        if prot not in PROTIEN_MASS:
            PROTIEN_MASS[prot] = weight
            
def getProtienMass(prot_str):
    weight = 0
    for prot in prot_str:
        weight += PROTIEN_MASS[prot]
        
    return weight

prot_str = 'VRAQDFKQNGGTETLYWPMSPYGISVAQDDLNGPDNRDDFPFPHIIRRWNRYWLGDWMDHFQQENANISKQLRGQATDINGCICYLGGEMWWERDAEIFLDEFRSMPNCQMWLLSRDAGTTALCDIMHWSGSGETCMCQYGQINSVRARTCFPGMESTLVANEPLGHECPHTVNRYCVMHGCQTGRLWFFWMEWLRPDVTEYYFCQESCTQDWGKCQLNREEKRDPGFECKMEWKHRWLLTHSRHHAISYDLKQSADRHQYWASHQNSNVFDVDTSKWYTVWPCVNCPACVFNPLCYYFLITCHDTVIKRMPPPFGKKGRMITSFDMMVYSQSSNYGTRVFHRGRCYVMCAWWQKSAWSISKDFCWTAGIEPWHLCPNRHVCIYKFTWRFNAFQMKNMPNTGHCTSNCGYHKSTHLKQKPDRQIRWQVMCWQYGYCQYEAELVMMKPGHMNKEHLIGSKYNWQGTVESCRVENRQMTYSHSACYGQLASKWRVYGDTILKMNFFSIMEVTGRALPKQTNGADCYGISLLLAPSTIYKYPSQMLQTEANYKMVKIYDTHRLCKYPQHITLLEEAGRFTAVAGNYNDTWMGRVSMCFKYFMRDACNFLMHATQMVGYAITCWVHQPRRDKNCCLFVLMPYMTASWNQWYYVVMQKHNVTRAALGGKWKLYCNLHFNLYQGMGTAMYPKRWWQEYDLYHNVQILMRYCPPYMWPMPKCRYRWAPICYIGLIRLTMYIMARYCLPHPHAMLDNDESLQTTWNCEHDTPVKEYVIWRCYNQMSIDKNVDKADPESCTLDVHPFRKIQCESGKDFFDKALPVDIVHMQRQFVEMCQYELYGGINNFHQEHENNKEDNNGHCYVRCWHLEPHRNSGTKHCVWEHYHMASITHAYHHEPWYNWYNRWISYFWLVSLSEPGIQYESPNLLDWTYPITSTFEQPDECGCTRKPDSEFVSVGCVGTEYQFSKMVDYKGTGIWWHGVLIKADYSRGKDHFTFNVTNF'
print('{:.4f}'.format(getProtienMass(prot_str)))