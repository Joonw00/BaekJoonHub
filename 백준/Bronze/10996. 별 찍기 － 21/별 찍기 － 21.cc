#include <iostream>
using namespace std;

int main(){
	int n;
	cin>>n;
	for(int i = 0; i<2*n; i++){
		if(i%2 == 0){ // 첫줄 
			for(int j = 0; j<n;j++){
				if(j%2 == 0) cout<<'*';
				else cout<<" ";
			}
			cout<<endl;
		}
		else{
			for(int j = 0;j<n;j++){
				if(j%2 == 0) cout<<" ";
				else cout<<"*";
			}
			cout<<endl;
		}
	}
	return 0;
} 