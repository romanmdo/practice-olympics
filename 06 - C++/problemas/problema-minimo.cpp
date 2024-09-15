#include <iostream>
#include <sstream>  
#include <string>

using namespace std;

int arreglo()
{   
    int arreglo[] = {1, 2, 3, 4, 5, 4 , 1 , 6};
    int arreglo_long = sizeof(arreglo) / sizeof(arreglo[0]);

    int minimo = arreglo[0];
    int maximo = arreglo[0];


    for (int i = 1; i < arreglo_long ; i++)
    {
        if (arreglo[i] < minimo)
        {
            minimo = arreglo[i];
        }
        else if (arreglo[i] > maximo)
        {
            maximo = arreglo[i];
        }
    }
    
    cout << "min: " << minimo << endl;
    cout << "max: " << maximo << endl;

    return 1;
}

int main() 
{
    arreglo();
    return 0;
}
