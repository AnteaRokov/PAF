#include <iostream>
#include <algorithm>

void definirano(float polje[], int N)
{
  for( int i = 0; i < N; i++)
  {
    std::cout << polje[i] << " ";
  }
  std::cout << std::endl;
}

void definirano_a_b(float polje[], int N, float a, float b)
{
  for( int i = 0; i < N; i++)
  {
    if(polje[i]>= a && polje[i]<=b) std::cout << polje[i] << " ";
  }
  std::cout << std::endl;
}

void swap(float polje[], int i, int j)
{
  float temp;
  temp = polje[i];
  polje[i] = polje[j];
  polje[j] = temp;
}

int main() {

  float polje[13] = {1, 2, 3, 4, 5, 6, 0, -1, -2, -3, -4, -5, -6};
  definirano(polje, 13);

  definirano_a_b(polje, 13, 0., 13.);

  std::sort(std::begin(polje), std::end(polje));
  definirano(polje, 13);

  std::reverse(std::begin(polje), std::end(polje));
  definirano(polje, 13);

  swap(std::begin(polje), 0, 1);
  definirano(polje, 13);

  return 0;
}