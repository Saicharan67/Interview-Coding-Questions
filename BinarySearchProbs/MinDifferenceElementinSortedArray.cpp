/*
Given an array of integers sorted in ascending order, and a target value, find the element in the array that has minimum difference with the target value.

Input: a[] = [2, 5, 10, 12, 15], target = 6
Output: 5
Explanation: The difference between the target value '6' and '5' is the minimum.

Input: a[] = [2, 5, 10, 12, 15], target = 8
Output: 10

Input: a[] = [2, 5, 10, 12, 15], target = 5
Output: 5

*/

#include <iostream>

using namespace std;

int solve(int arr[],int N,int target){
    
    if (target < arr[0]){
        return arr[0];
    }
          
    if (target > arr[N - 1])
        return arr[N - 1];

    int start = 0, end = N - 1;
    while (start <= end) {
        int mid = (start + end) / 2;

        if (target == arr[mid]) {
            return arr[mid];
        } else if (target < arr[mid]) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    /*
       At the end of the while loop, 
       a[start] is the ceiling of target (Smallest number greater than target), and 
       a[end] is the floor of target (Largest number smaller than target).
       
       Return the element whose difference with target is smaller
     */
    if ((arr[start] - target) < (target - arr[end]))
        return arr[start];
    return arr[end];
}
int main()
{
    int N,target; // N is size of array
    cin>>N>>target;
    int arr[N];
    for(int i=0;i<N;i++){
        cin>>arr[i];
    }
    int res = solve(arr,N,target);
    cout<<"The minimum difference element with "<<target<<" is "<<res<<endl;
    return 0;
}
