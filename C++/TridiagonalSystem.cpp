#include "windows.h"
#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;
void gotoxy(int x, int y)
{
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}
float a[10][10], w[10], d[10], zeta[10], x[10], b[10];
int main() {
    int n, i, j, k, l, m, ver = 10, hor = 9;
    cout << "\n\n\tTRIDIAGONAL SYSTEM OF EQUATIONS";
    cout << "\n\t=================================";
    cout << "\n\n\tSIZE OF MATRIX: ";
    cin >> n;
    cout << "\n\tENTER THE VALUES: ";
    for (i = 1; i < n; i++)
    {
        j = i + 1;
        gotoxy(hor, ver); cin >> a[i][i]; hor += 6;
        gotoxy(hor, ver);
      cin >> a[i][j]; ver++; hor = 9 + 6 * (i - 1);
        gotoxy(hor, ver);
        cin >> a[j][i]; hor += 6;
    }
    gotoxy(hor, ver); cin >> a[i][i];
    hor += 4; ver = 10;
    for (j = 0; j <= n; j++) {
        gotoxy(hor, ver);
        cout << "= ";cin >> b[j];
        ver++;
    }
    w[1] = a[1][1];
    zeta[1] = b[1] / w[1];
    for (j = 1; j <= n - 1; j++) {
        k = j + 1;
        d[j] = a[j][k] / w[j];
        w[k] = a[k][k] - a[k][j] * d[j];
        zeta[k] = (b[k] - a[k][j] * zeta[j]) / w[k];
    }
    x[n] = zeta[n];
    for (l = 1; l <= n - 1; l++) {
        m = n - l;
        x[m] = zeta[m] - x[m + 1] * d[m];
    }
    for (m = 1; m <= n; m++) {
        cout << "\n\t X" << m << "= " << x[m];
    }
    _getch();
    return 0;
}


