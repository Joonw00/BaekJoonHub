#include <iostream>
using namespace std;

int main(){
	int a,s;
	cin>>s;
	for(int i = 0;i<9;i++){
		cin>>a;
		s-=a;
	}
	cout<<s;
	return 0;
} 