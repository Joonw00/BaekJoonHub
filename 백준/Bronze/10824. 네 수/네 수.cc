#include <iostream>
#include <string>
using namespace std;

int main() {
  int a,b,c,d;
  cin>>a>>b>>c>>d;
  string s1 = to_string(a)+to_string(b);
  string s2 = to_string(c)+to_string(d);
  long long an1 = stoll(s1);
  long long an2 = stoll(s2);
  cout<<an1+an2;
  return 0;
}