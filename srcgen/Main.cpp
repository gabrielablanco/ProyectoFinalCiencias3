#include <iostream>

using namespace std;

int fibonacci(int x){
	if(x > 2)
		return fibonacci(x-1) + fibonacci(x-2);
	else if(x==2 || x==1)
		return 1;
	else if (x==0)
		return 0;
}

int Main(){
 
	int num;
	for (num=0; num<=20; num++)){
		cout << fibonacci(num) << " " << endl;
	}
	return 0;
}
