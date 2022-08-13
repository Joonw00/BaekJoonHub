#include <iostream>
using namespace std;
int main(){
	int a,b,c,d,winner,score,temp;
	score = 0;
	for(int i = 1;i<6;i++){
		cin>>a>>b>>c>>d;
		temp = a+b+c+d;
		if(temp>score){
			winner = i;
			score = temp;
		}
	}
	cout<<winner<<" "<<score;
	return 0;
} 