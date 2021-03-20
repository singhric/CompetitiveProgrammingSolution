#include<iostream>
using namespace std;
class student{
	public:
		char name[10];
		int rollno;
		void putstu();
		void getstu();
};
void student :: putstu(){
	cout << "Enter the details" << endl;
			cout << "Name & Roll No.";
			cin >> name >> rollno;
}
void student :: getstu(){
			cout << "Name of student " << name << endl;
			cout << "Roll No. " << rollno << endl;
}
class sports{
	public:
		int part,nonpart;
		void putsport(){
			cout << "Enter the marks of participants" << endl;
			cin >> part ;
			cout << "Enter the marks of non participants" << endl;
			cin >> nonpart ;
		}
		void getsport(){
			cout << "Marks of paricipants" << part << endl;
			cout << "Marks of non paricipants" << nonpart << endl;
		}
};
class accounts : public student{
	public:
	int totalf, paidf;
	void putfee(){
		cout << "Enter the total & paid fees" << endl;
		cin >> totalf >> paidf;
	}
	void getfee(){
		cout << "Total fees" << totalf << endl;
		cout << " Paid fees" << paidf << endl;
	}
};
class marks : public student{
	public:
	int sub1,sub2,sub3;
	void putmrk(){
		cout << "Enter the number of the subjects";
		cin >> sub1 >> sub2 >> sub3;
	}
	void getmrk(){
		cout << "Marks of 1st subject " << sub1<<endl;
		cout << "Marks of 2nd subject " << sub2<<endl;
		cout << "Marks of 3rd subject " << sub3<<endl;
	}
};
class fees : public accounts {
	public:
	int pendingdues;
	void putdues(){
		cout << "Enter the pending dues";
		cin >> pendingdues;
	}
	void getdues(){
		cout << "Pending dues " << pendingdues << endl;
	}
};
class result : public fees, public marks, public sports{
	public:
		float per;
		void putresult(){
		//putstu();
		putsport();
		putdues();
		putmrk();
		per = (sub1 + sub2 + sub3 + part)/4;
		}
	void getresult(){
		//getstu();
		getsport();
		getdues();
		getmrk();
		cout<<"Percent = "<<per<<endl;
		cout<<"pending dues = "<<pendingdues<<endl;
	}
};
int main()
{
	student obj;
 	 result obj1; 
 	 obj.putstu();
 	 obj.getstu();
 	 obj1.putresult();
 	 obj1.getresult();
 	return 0;
}   	