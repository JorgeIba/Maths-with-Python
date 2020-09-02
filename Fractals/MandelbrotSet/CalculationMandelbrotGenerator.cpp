#include <bits/stdc++.h>
#define lli long long int
using namespace std;

int MendelbrotCalc(lli x, lli y, complex<double> c,lli exponente, lli maxIterations)
{
    complex<double> z = {0,0};
    for(int n=0; n<maxIterations; n++)
    {
        z = pow(z,exponente) + c;
        if(abs(z) >= 2)
        {
            return n;
        }
        n++;
    }
    return maxIterations;
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    
    int width, height, exponent; cin>>width>>height>>exponent;
    vector<float> valuesX(width);
    vector<float> valuesY(height);
    for(int i=0; i<width; i++)
    {
        cin>>valuesX[i];
    }
    for(int i=0; i<height; i++)
    {
        cin>>valuesY[i];
    }

    for(int i = 0; i<width; i++)
    {
        for(int j = 0; j<height; j++)
        {
            complex<double> c = {valuesX[i], valuesY[j]};
            cout<<i<<" "<<j<<" "<<MendelbrotCalc(i, j, c, exponent, 100)<<endl;
        }
    }


    return 0;
}