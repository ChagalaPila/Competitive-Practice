# -*- coding: utf-8 -*-
"""Common Prefixes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/145vaew5Clc7ro-PyJDpoFOiFuStckOlg
"""

val = 97
for _ in range(int(input())):
  n = int(input())
  s = [chr(val)] * 60
  l = list(map(int,input().split()))
  print("".join(s))
  for i in l:
    if s[i] == chr(val + 1):
      s[i] = chr(val)
    else: 
      s[i] = chr(val + 1)
    print("".join(s))
  if val >= 120:
    val = 97
