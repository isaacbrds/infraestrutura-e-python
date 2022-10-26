from scapy.all import *

resposta = sr1(IP(dst="10.30.1.254")/ICMP()/"XXXXXXXXXXX", timeout=3)

if resposta is not None:
  print('Resposta')
  print(resposta.src)
  print(resposta.dst)
else: 
  print('Falhou')