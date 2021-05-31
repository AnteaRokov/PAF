#include <iostream>
#include <math.h>


bool kruznica(float x1, float y1, float r, float x2, float y2) //x2,y2 oznacavaju koordinate tocke 
{
  bool pozicija_tocke;
  float udaljenost = sqrt((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1));

  if (udaljenost < r) 
  pozicija_tocke = true;
  
  else 
  pozicija_tocke = false;

  return pozicija_tocke;
}

int main() {

  std::cout << kruznica(0,0,10,2,3) << std::endl;

  return 0;
}