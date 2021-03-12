while True:
    x1 = float(input('Unesi x1 koordinatu: '))
    y1 = float(input('Unesi y1 koordinatu: '))
    
    if x1 == str or y1 == str:
        print('Unos mora biti broj, a ne string!')
    else:
        break
while True:
    x2 = float(input('Unesi x2 koordinatu: '))
    y2 = float(input('Unesi y2 koordinatu: '))
    if x2 == str or y2 == str:
        print('Unos mora biti broj, a ne sting!')
    else:
        break
k = (y2 - y1) / (x2 - x1)
l = - k*x1 + y1

print('y = {} * x + {}'.format(k, l))