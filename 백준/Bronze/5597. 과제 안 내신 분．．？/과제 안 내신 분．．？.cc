#include <iostream>
using namespace std;

int main(){
	int temp,ck[31];
	for(int i = 0;i<31;i++){
		ck[i] = 0;
	}
	for(int i = 0;i<28;i++){
		cin>>temp;
		ck[temp] = 1;
	}
	
	for(int i = 1;i<31;i++){
		if(ck[i] == 0){
			cout<<i<<endl;
		}
	}
	return 0;
} 