#include <iostream>
using namespace std;

int main(){
	int n,k,m,l;
	cin>>n>>k>>m;
	l = n*k - m;
	if(l>0) cout<<l;
	else cout<<0;
	return 0;
}