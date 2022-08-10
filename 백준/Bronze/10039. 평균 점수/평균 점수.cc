#include <iostream>
using namespace std;
int main(){
	int inp,ans;
	ans = 0;
	for(int i =0;i<5;i++){
		cin>>inp;
		if(inp<40) ans+=40;
		else ans+=inp;
	}
	cout<<ans/5;
	return 0;
} 