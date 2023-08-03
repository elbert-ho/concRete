#include<iostream>
#include<string>
using namespace std;

int main() {
    freopen("/Users/Elbert/Desktop/R_Summer_2023/concRete/Misc/resulting_links.txt", "r", 
stdin);
    //freopen("deleg.out", "w", stdout);
    for(int i = 0; i < 192; i++) {
        string a;
        getline(cin, a, ',');
        //cin >> a;
        //cout << a << endl;
        a = "wget " + a;  
        //cout << a << endl;
        //char* char_array = a.c_str();
        system(a.c_str());
    }     

}
