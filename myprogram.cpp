#include <iostream>
#include <particle.h>

using namespace std;

int main()
{
    Particle p1(100,45,0,0);
    Particle p2(10,60,0,0);

    cout << "Domet prve cestice jest: " << p1.range() << endl;
    cout << "Vrijeme leta prve cestice jest: " << p1.time() << endl;

    cout << "Domet druge cestice jest: " << p2.range() << endl;
    cout << "Vrijeme leta druge cestice jest: " << p2.time() << endl;

    return 0;
}