public class SelectionSort{  
    public static void selectionSort(int[] arr){  
        for (int i = 0; i < arr.length - 1; i++)  
        {  
            int index = i;  
            for (int j = i + 1; j < arr.length; j++){  
                if (arr[j] < arr[index]){  
                    index = j; 
                }  
            }  
            int smallerNumber = arr[index];   
            arr[index] = arr[i];  
            arr[i] = smallerNumber;  
        }  
    }  
       
    public static void main(String a[]){  
        int[] arr1 = {9,14,3,2,43,11,58,22};  
      
          
     selectionSort(arr1);
         
          
        for(int i:arr1){  
            System.out.print(i+" ");  
        }  
    }  
}  
