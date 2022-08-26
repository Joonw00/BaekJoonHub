#include <iostream>
using namespace std;

int main(){
	int n,ans,temp;
	cin>>n;
	n = 1000-n;
	temp = n/500;
	ans = temp;
	n = n - 500*temp;

	temp = n/100;
	ans += temp;
	n = n - 100*temp;
	
	temp = n/50;
	ans +=temp;
	n = n - 50*temp;
	
	temp = n/10;
	ans+=temp;
	n = n - 10*temp;
	
	temp = n/5;
	ans+=temp;
	n = n - 5*temp;
	ans+=n;
	cout<<ans;
	return 0;
} 