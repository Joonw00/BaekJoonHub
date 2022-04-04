#include<iostream>
#include <stack>
using namespace std;

int Prece(char c){
	if(c == '*' || c == '/') return 2;
	if (c == '+' || c == '-') return 1;
	if ('A'<= c && c<='Z')return 0;
	else return -1;
} 

int main(){
	string str;
	int l;
	stack<char> s;
	cin>>str;
	l = str.length();
	for(int i =0; i<l;i++){
		if (str[i] == '('){
			s.push(str[i]);
			continue;
		}
		else if (str[i] == ')'){
			while(s.top() != '('){
			cout<<s.top();
			s.pop();
			}
			s.pop();
			continue;
		}
		
		switch(int p = Prece(str[i])){
			case 0:cout<<str[i];break;
			case 1: case 2:
				while(s.empty()==0&&Prece(s.top())>=p){
					cout<<s.top();
					s.pop();
				}
				s.push(str[i]); break;
		}
	}
	while(s.empty() == 0){
		cout<<s.top();
		s.pop();
	}
	return 0;
}