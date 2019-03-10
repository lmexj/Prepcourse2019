#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:56:39 2019

@author: anna

PrepCourse
"""

import pandas as pd
INPUT = '/home/anna/Dokumente/PrepCourse/gencode.v19.annotation.gtf'
OUTPUT = '/home/anna/Dokumente/PrepCourse/test'
gtf = pd.read_csv(INPUT, sep = '\t', skiprows=5, header=None)

gencodeBED = gtf.loc[gtf[2] == 'gene']

gencodeBED.loc[gencodeBED[6] == '+', 'start' ] = gencodeBED[3] -501
gencodeBED.loc[gencodeBED[6] == '+', 'end' ] = gencodeBED[3] +99
gencodeBED.loc[gencodeBED[6] == '-', 'start' ] = gencodeBED[4] +499
gencodeBED.loc[gencodeBED[6] == '-', 'end' ] = gencodeBED[4] -101

new = gencodeBED[8].str.split(" ", expand = True) 
gencodeBED['name'] = new[9].str.replace('\"','').str.replace(';','') + '_' + new[1].str.replace('\"','').str.replace(';','')

final = gencodeBED[[0, 'start', 'end', 'name', 5, 6]]

final.to_csv(OUTPUT, sep = '\t', header=False, index=False)

