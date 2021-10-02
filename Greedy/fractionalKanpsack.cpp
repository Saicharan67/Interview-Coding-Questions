#include<bits/stdc++.h>
using namespace std;

struct Item{
    int value;
    int weight;
};

bool sortByFirst(const pair<double, Item> &a, const pair<double, Item> &b)
    {
            return a.first > b.first;
    }
double fractionalKnapsack(int W, Item arr[], int n)
    {
       vector<pair<double, Item>> elements;
       double ratio = 0;
       
       for(int i = 0; i < n; i++){
            ratio = (double)arr[i].value/(double)arr[i].weight;
            elements.push_back(make_pair(ratio, arr[i]));
       }
       
       sort(elements.begin(), elements.end(), sortByFirst);
       double max_profit = 0;
       int cur_weight = 0;
       for(int i = 0; i < n; i++){
           if(elements[i].second.weight + cur_weight <= W){
               max_profit += (double)elements[i].second.value;
               cur_weight += (double)elements[i].second.weight;
           }
           else{
               int remain = W - cur_weight;
               max_profit += (double)elements[i].second.value*((double)remain/(double)elements[i].second.weight);
               break;
           }
       }
       
       return max_profit;
    }


int main(){
    int n, w;
    cin >> n >> w;

    Item arr[n];
	for(int i=0;i<n;i++){
			cin>>arr[i].value>>arr[i].weight;
	}

    cout << fractionalKnapsack(w, arr, n);
    return 0;
}