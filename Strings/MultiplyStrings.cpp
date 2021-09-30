/*
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
For example,
given strings "12", "10", your answer should be “120”.

NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
*/
/*
Input_1 : 25 12
Output_1: 300

Input_2: 010 20
Output_2 : 200

*/

#include<bits/stdc++.h>
using namespace std;

string multiply(string A, string B) {
    if(A=="0" || B=="0")
        return string("0");
    int m = A.length(),n=B.length();
    vector<int> ans(m+n,0) ;
    for(int i = m-1;i>=0;i--){
        for(int j=n-1;j>=0;j--){
            ans[i+j+1] = ans[i+j+1]+((A[i]-'0')*(B[j]-'0'));
        }
    }
    int carry = 0;
    for(int i = m+n-1 ;i>=0;i--){
        ans[i]+=carry;
        carry = ans[i]/10;
        ans[i] = ans[i]%10 ; 
    }
    string final="";
    int i=0;
    while(ans[i]==0){
        i++;
    }
    for(int j=i;j<m+n;j++){
        final+= to_string(ans[j]);
    }
    return final;
}
int main(){
  string A,B;
  cin>>A>>B;
  string result = multiply(A,B);
  cout<<"Product of "<<A<<" and "<<B<<" is "<<result;
  return 0;
}
