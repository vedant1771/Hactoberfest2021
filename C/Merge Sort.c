#include<stdio.h>
int merge(int a[],int l,int mid,int h){
	
	int i=l,j=mid+1,k=l;
	int b[20];
	
	while(i<=mid&&j<=h){
		if(a[i]<a[j]){
			b[k++]=a[i++];
		}
		else
		   b[k++]=a[j++];
	}
	for(;i<=mid;i++)
		b[k++]=a[i];
	for(;j<=h;j++)
	    b[k++]=a[j];
	    
	for(i=l;i<=h;i++)
	a[i]=b[i];
}
	
int mergesort(int a[], int l, int h){
	if(l<h){
		 int mid;
		 mid=(l+h)/2;
		mergesort(a,l,mid);
		mergesort(a,mid+1,h);
		merge(a,l,mid,h);
	}
}


int main(){
	int a[20],n,i;
	printf("enter size you want for array :");
	scanf("%d",&n);
	
	printf(" enter elemets of array :");
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	
	mergesort(a,0,n-1);
    printf("sorted array :");
	for(i=0;i<n;i++){
		printf("\t%d",a[i]);
	}		
}
