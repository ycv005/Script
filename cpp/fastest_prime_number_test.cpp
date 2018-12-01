#include<iostream>
using namespace std;
bool isPrime(int n)
{
    if (n <= 1)  return false;
    if (n <= 3)  return true;

    if (n%2 == 0 || n%3 == 0) return false;

    for (int i=5; i*i<=n; i=i+6)
        if (n%i == 0 || n%(i+2) == 0)
           return false;

    return true;
}
int main(){
    long long n;
    cin>>n;
    if(isPrime(n)){
        cout<<"It is a Prime no";
    }
    else{
        cout<<"It is not a Prime no.";
    }
return 0;
}
