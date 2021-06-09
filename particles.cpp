#include <iostream>
#include <math.h>

using namespace std;

class Particle {
   private:
    double t, x, y, vx, vy;
    double delta_t;
    double g = -9.81;

    void evolve()
    {
      while(y >= 0)
      {
        vx += 0.;
        vy += g*delta_t;

        x += vx*delta_t;
        y += vy*delta_t;

        t += delta_t;
      }
    }

   public:
    Particle(double v, double theta, double x0, double y0, double step=0.001)
    {
        
        vx = v*cos(theta*M_PI/180.);
        vy = v*sin(theta*M_PI/180.);
        x = x0;
        y = y0;
        t = 0.;
        delta_t = step;
    }

    double range()
    {
        if (t < delta_t) evolve();
        return x;
    }

    double time()
    {
      if (t < delta_t) evolve();
      return t;
    }
};

int main()
{
    Particle p1(100,45,0,0);
    Particle p2(10,60,0,0);

    cout << "Domet prve cestice jest: " << p1.range() << endl;
    cout << "Vrijeme leta prve cestice jest: " << p1.time() << endl;

    cout << "Domet druge cestice jest: " << p2.range() << endl;
    cout << "Vrijeme leta druge cestice: " << p2.time() << endl;

    return 0;
}