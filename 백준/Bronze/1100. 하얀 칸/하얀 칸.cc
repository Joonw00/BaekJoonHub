#include <iostream>

using namespace std;

int main(){
	int ans = 0;
	char chess[8][9];
	for(int i=0;i<8;i++){
		cin>>chess[i];
	}
	for(int i=0;i<8;i++){
		for(int j=0;j<8;j++){
			if((j+i)%2 == 0 && chess[i][j] == 'F') ans+=1;
		}
	}
	cout<<ans;
	return 0;
} 