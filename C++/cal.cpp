#include <iostream>
#include <string>
using namespace std;
int m_days[12]={31,28,31,30,31,30,31,31,30,31,30,31};
string month[12]={"January","February","March","April","May","June","July","August","September","October","November"," December"};
int day;
struct node{
    int date;
    node * next=NULL;
    node * down=NULL;
};

void initcal(node*);
node * celcal(node *,int);
void storemonth(node *,int);
int firstday(int);
void neatprint(node *,int);

int main(){   
    node *c=new node();
    node *p=c;
    int year,d,i;
    cout<<"Enter the year and the day on 1st jan[from 0 to 6(sunday=0)]"<<endl;
    cin>>year>>d;
    day=d;
    
    if(year%4==0){
        m_days[1]=29;
    }
    initcal(c);
    p=p->next;
    for(i=0;i<12;i++){
        storemonth(c,i);
    }

     for(i=0;i<12;i++){
        neatprint(c,i);
        cout<<endl;
     }
    return 0;
}
void initcal(node *c){
    node *ptr[21];
    int i,j;
    node *p=c;
    
    ptr[0]=p;
    p->date=0;
    //cout<<"0,0  ";
    for(i=1;i<21;i++){
        p=new node();
        ptr[i]=p;
        p->date=0;
        ptr[i-1]->next=p;
        //cout<<"0,"<<i<<" ";
        
    }//cout<<endl;
    for(i=0;i<19;i++){
        p=new node();
        p->date=0;
        ptr[0]->down=p;
        ptr[0]=p;
       // cout<<i+1<<",0  ";
        for(j=1;j<21;j++){
            p=new node();
            p->date=0;
            ptr[j]->down=p;
            ptr[j-1]->next=p;
            ptr[j]=p;
            //cout<<i+1<<","<<j<<"  ";
        }
        //cout<<endl;
    }
}
node * celcal(node * c,int m){
    int i,h,v;
    node *x=c;
    h=m%3;
    v=(m-h)/3;
    for(i=0;i<7*h;i++){
        x=x->next;
    }
    for(i=0;i<5*v;i++){
        x=x->down;
    }
    return x;
    
}
void storemonth(node* n1,int m){
    n1=celcal(n1,m);
    node* n2=n1;
    node* n3=n1;
    int d=1,i,j;
    for(i=0;i<5;i++){
        n2=n2->down;
        for(j=0;j<7;j++){
            if(d<=m_days[m]){
                
                if(j==day){
                    
                    n1->date=d++;
                    day=(day+1)%7;
                    
                } 
            n1=n1->next;       
            } 
        
            
        }
    n1=n2;        
    }d--;
    if(d<m_days[m]){
        for(i=0;i<m_days[m]-d;i++){
            n3->date=d+1+i;
            
            n3=n3->next;
            day=(day+1)%7;
        }
    }
    
}
void neatprint(node *n,int m){
    int i,j;
    cout<<"     "<<month[m]<<endl;
    cout<<"Su Mo Tu We Th Fr Sa"<<endl;
    n=celcal(n,m);
    node *n2=n;
    n2=n;
    for(i=0;i<5;i++){
        n2=n2->down;
        for(j=0;j<7;j++){
            if(n->date==0)
            cout<<"   ";
            else if(n->date<10)
            cout<<n->date<<"  ";
            else
            cout<<n->date<<" ";
            n=n->next;
        }cout<<endl;
        n=n2;
    }
    
}













