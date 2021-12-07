#include<iostream>
#include<string>
#include <stdlib.h>
#include <stdio.h>
 
using namespace std;
int main(int argc, char *argv[]){

    cout << "Compare with the golden result:";

    char *input1 = *(argv + 1);
    char *input2 = *(argv + 2);


	string ans1,ans2;
	unsigned long int i;
    char c;

	FILE *temp1 = fopen(input1,"r");
	while(fscanf(temp1,"%c",&c)!=EOF){
        ans1+=c;
    }
	fclose(temp1);

    FILE *temp2 = fopen(input2,"r");
	while(fscanf(temp2, "%c",&c)!=EOF){
        ans2+=c;
    }
	fclose(temp2);

    //if size not equal 
	if(ans1.size()!=ans2.size()){
        cout<<"You shall not Pass XXX!!!\n";
        return 0;
    }

    //size equal but answer not equal
	for(i=0;i<ans1.size();i++){
        if(ans1[i]!=ans2[i]){
            cout<<"You shall not Pass XXX!!!\n";
            return 0;
        }
    }

    //equal file
	cout<<"Pass!!!\n";
	return 0;
}