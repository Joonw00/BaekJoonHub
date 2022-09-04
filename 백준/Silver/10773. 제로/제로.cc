#include <iostream>
#include <stack>
using namespace std;

int main(){
	int k,n,s = 0;
	cin>>k;
	stack<int> st;
	for(int i=0;i<k;i++){
		cin>>n;
		if(n == 0) st.pop();
		else st.push(n);
	}
	while(!st.empty()){
		s+=st.top();
		st.pop();
	}
	cout<<s;
	return 0;
} 