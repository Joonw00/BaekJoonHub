#include <iostream>
using namespace std;
int main(){
	int a,b,c,d,e,bg,drink;
	cin>>a;
	cin>>b;
	cin>>c;
	cin>>d;
	cin>>e;
	bg = min(a,b);
	bg = min(bg,c);
	drink = min(d,e);
	cout<<bg+drink-50;
	return 0;
} 