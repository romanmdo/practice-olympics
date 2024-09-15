#include <iostream>
#include <sstream>  
#include <string>

using namespace std;

int arreglo()
{   
    string cadena;
    cout << "# Cadena: ";

    getline(cin, cadena);
    stringstream cadenaInt(cadena);
    
    int numero;
    int resultadoPar = 0;
    int resultadoImpar = 1;

    while (cadenaInt >> numero) 
    {
        if(numero % 2 == 0)
        {
            resultadoPar += numero;
        }
        else{
            resultadoImpar *= numero;
        }
    }

    cout << "# Suma Par: " << resultadoPar << endl;
    cout << "# Producto Impar: " << resultadoImpar << endl;

    return 1;
}

int main() 
{
    arreglo();
    return 0;
}
