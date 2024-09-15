#include <iostream>
#include <cmath>

using namespace std; 

int kosaraju(float p, int c, int g)  
{   
    float proteGramos = 27;
    float proteCalorias = 105;

    float bananas = p / proteGramos;
    float bananaCeil= ceil(bananas); // Redondeamos las bananas

    float bananasFin = proteCalorias * bananaCeil;

    /* CARBOHIDRATOS (ATUNES) */ 
    int carbGramos = 30; // Carbos que aporta 1 Atun
    int carbCalorias = 120; // Cal que aporta 1 Atun
    
    int atunes = c / carbGramos; // Cantidad de atunes consumida
    int atunFin = carbCalorias * atunes; // Calorias de atunes final
    
    /* GRASAS (ACEITE) */ 
    int grasaGramos = 1;
    int grasaCalorias = 9;

    int aceites = g / grasaGramos; 
    int aceitesFin = grasaCalorias * aceites;

    int calDiarias = bananasFin + atunFin + aceitesFin; // Suma de las calorias totales
    
    cout << calDiarias << endl;

    return 0;
}

int main()
{
    kosaraju(88, 90, 50);
    return 0;
}

