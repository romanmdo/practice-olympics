#include <iostream>
#include <vector>

using namespace std; 

int vectores()  
{   
    vector<int> numeros {1, 2, 3, 4, 5, 6}; // Inicializar vector 
    int numero_user = 0;

    cout << "Ingresa un numero: ";
    cin >> numero_user;
    numeros.push_back(numero_user); // Metodo para agregar un elemento al final del vector

    int vector_tamanio = numeros.size();
    
    for (int i = 0; i < vector_tamanio; i++)
    {
        cout << numeros[i] << endl;
    }

    cout << "Direccion de memoria: " << &numero_user << endl; 
}

int main()
{
    vectores();
    return 0;
}

