#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Function to swap two elements */
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

/* Partition function */
int partition(int arr[], int low, int high) {
    int pivot = arr[low];
    int i = low+1;
    int j = high;
    int temp;
    do{
        while(arr[i]<pivot)
            i++;
        while(arr[j] > pivot)
            j--;
        if (i<j){
            swap(&arr[i], &arr[j]);
        }
    }while(i<j);

    swap(&arr[low], &arr[j]);

    return j;
}

/* Quick Sort function */
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

/* Main function */
int main() {
    int arr[] = {38, 27, 43, 3, 9, 82, 10};
    int n = sizeof(arr) / sizeof(arr[0]);

    clock_t start_t, end_t;
    start_t = clock();

    quickSort(arr, 0, n - 1);

    end_t = clock();

    printf("Sorted array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    double time_taken = ((double)(end_t - start_t)) / CLOCKS_PER_SEC;
    printf("Time taken by QuickSort: %f seconds\n", time_taken);

    /*
    Time Complexity:
    Worst Case   : O(n^2)   (poor pivot selection)
    Best Case    : O(n log n) (balanced partitions)
    Average Case : O(n log n)
    */

    return 0;
}
