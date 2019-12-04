#include <iostream>
#include <stdlib.h>
#include <unistd.h>

using namespace std;

struct Data
{
	double x;
	double y;
};

double u_cal(double u, int n)
{
	double temp = u;
	for (int i = 1; i < n; i++)
		temp *= (u - i);
	return (temp);
}

long long int fact(int n)
{
	long long f = 1.;
	for (int i = 2; i <= n; i++)
		f *= i;
	return (f);
}

int main(void)
{
	const int n = 4;
	Data f[n] = 
	{
	 { 0, 2 },
	 { 1, 3 },
	 { 2, 12 },
	 { 3, -1 }
	};
	double y[n][n];
	for (int i = 0; i < n; i++)
		y[i][0] = f[i].y;
	for (int i = 1; i < n; i++)	
		for (int j = 0; j < n - i; j++)
			y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
	double x1 = 0, x2 = 6, dx = 0.5;
	cout.width(20); cout << "X"; cout.width(20); cout << "Y" << endl;
	for (double x = x1; x <= x2; x += dx)
	{
		double sum = y[0][0];
		double u = (x - f[0].x) / (f[1].x - f[0].x);
		for (int i = 1; i < n; i++) 
			sum += (u_cal(u, i) * y[0][i]) / fact(i);
		cout.width(20); cout.precision(14); cout << x;
		cout.width(20); cout.precision(14); cout << sum << endl;
	}
	pause();
	return (0);
}
