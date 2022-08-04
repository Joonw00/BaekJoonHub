#include <iostream>

using namespace std;
int main(){
	int a,b,c,d,s;
	for(int i = 0;i<3;i++){
		cin>>a>>b>>c>>d;
		s = a+b+c+d;
		if(s == 0) cout<<"D"<<endl;
		else if(s == 1)cout<<"C"<<endl;
		else if(s == 2)cout<<"B"<<endl;
		else if(s == 3)cout<<"A"<<endl;
		else if(s == 4)cout<<"E"<<endl;
	}
	return 0;
}