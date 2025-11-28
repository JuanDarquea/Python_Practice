str = 'X-DSPAM-Confidence: 0.8475'

ipor = str.find(':')
print(str)
print(ipor)

piece = str[ipor+2:]
print(piece)

value = float(piece)
print(value)
print(value + 9.1525)