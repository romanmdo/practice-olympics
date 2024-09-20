#include <iostream>
#include <vector>

using namespace std; 

int vectores()  
{   
    vector<int> fila1 {1, 2, 3, 4};
    vector<int> fila2 {5, 6, 7, 8};
    vector<int> fila3 {9, 10, 11, 12};

    vector<vector<int>> matriz = {fila1, fila2, fila3};

    int matriz_tamanio = matriz.size();
    int suma_elementos = 0;

    for (int i = 0; i < matriz_tamanio; i++)
    {
        for (int j = 0; j < matriz[i].size(); j++)
        {
            cout << "Elemento en [" << i << "][" << j << "]: " << matriz[i][j]<< endl; 
        }
        cout << endl;
    }

    return 0;
}

int main()
{
    vectores();
    return 0;
}
