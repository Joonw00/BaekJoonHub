#include <iostream>
using namespace std;
int main(){
	int pl,mi,tot,ans;
	tot = 0;
	ans = 0;
	for(int i = 0;i<4;i++){
		cin>>mi>>pl;
		tot +=pl-mi;
		if(tot>ans) ans = tot;
	}
	cout<<ans;
	return 0;
} 