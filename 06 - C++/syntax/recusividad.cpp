#include <iostream>
using namespace std;

// Función recursiva para calcular el factorial de un número
int factorial(int n) {
    // Caso base
    if (n == 0 || n == 1) {
        return 1;
    }
    // Llamada recursiva
    return n * factorial(n - 1);
}

int main() {
    int num;
    cout << "Introduce un número: ";
    cin >> num;

    cout << "El factorial de " << num << " es: " << factorial(num) << endl;
    return 0;
}
