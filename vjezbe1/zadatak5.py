def nacrtaj_graf(x1, y1, x2, y2):
    x = [x1, x2]
    y = [y1, y2]
    plt.plot(x, y)
    p = input('Zelite li graf ispisati odmah ili u pdf-u? Ako zelite odmah unesite rijec odmah, a ako zelite u pdf-u unesite PDF!')
    if p == 'odmah':
        plt.show()
    elif p == 'PDF':
        ime = input('Unesite ime pod kojim zelite pohraniti svoj pdf: ')
        plt.savefig(f'{ime}.pdf')
import matplotlib
import matplotlib.pyplot as plt

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
plt.xlabel('x')
plt.ylabel('y')
plt.title('Pravac kroz dvije tocke')

nacrtaj_graf(x1, y1, x2, y2)