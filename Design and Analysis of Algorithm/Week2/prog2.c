#include <stdio.h>
//Merge sort

void merge(int arr[], int low, int mid, int high){
    int i = low;
    int j = mid+1;
    int k = 0;

    int temp [high-low+1];

    while(i<= mid && j <= high){
        if (arr[i]<= arr[j])
            temp[k++] = arr[i++];
        else    
            temp[k++] = arr[j++];
    }
    while (i<=mid)
        temp[k++] = arr[i++];

    while (j<= high)
        temp[k++] = arr[j++];
    
    for (int g = 0; g < k; g++)
        arr[low + g] = temp[g];
    
    
}

void mergeSort(int arr[], int low, int high){
    if(low < high){
        int mid = (low+high)/2;
        mergeSort(arr,low,mid);
        mergeSort(arr,mid+1,high);
        merge(arr,low,mid,high);
    }
}

void print_result(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {28, 12, 15, 13, 25};
    int n = sizeof(arr) / sizeof(arr[0]);
     mergeSort(arr, 0, n - 1);   
    print_result(arr, n);       
    return 0;
}