#include<iostream>
#include<string>
 
using namespace std;
int main(int argc, char *argv[]){

    cout << "Compare with the golden result:";

    char *input1 = *(argv + 1);
    char *input2 = *(argv + 2);


	string t,ans,ans2;
	unsigned long int i;
    char c;

	freopen(input1,"r",stdin);
	while(scanf("%c",&c)!=EOF){
        ans+=c;
    }
	fclose(stdin);

	freopen(input2,"r",stdin);
	while(scanf("%c",&c)!=EOF){
        ans2+=c;
    }
	fclose(stdin);

	if(ans.size()!=ans2.size()){
        cout<<"You shall not Pass XXX!!!\n";
        return 0;
    }

	for(i=0;i<ans.size();i++){
        if(ans[i]!=ans2[i]){
            cout<<"You shall not Pass XXX!!!\n";
            return 0;
        }
    }

	cout<<"Pass!!!\n";
	return 0;
}