import pprint
s = input() 

counttrace = {}

def Frequency_analytic(s):
  for char in s:
    if char in counttrace:
      counttrace[char] += 1
    else:
      counttrace[char] = 1
  pprint.pprint(counttrace) == print(pprint.pformat(counttrace))

Frequency_analytic(s)  
