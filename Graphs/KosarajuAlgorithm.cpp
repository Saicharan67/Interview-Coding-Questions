#include <bits/stdc++.h>
using namespace std;

class KA
{
	public:
	//Function to find number of strongly connected components in the graph.
	void DFS(int v, vector<int> adj[], vector<bool>& visited, stack<int>& s){
	    
	    visited[v] = true;
	    for(int i : adj[v]){
	        
	        if(!visited[i]){
	            DFS(i, adj, visited, s);
	        }
	        
	    }
	    s.push(v);
	}
	void DFS2(int v, vector<int> adj[], vector<bool>& visited){
	    
	    visited[v] = true;
	    for(int i : adj[v]){
	        
	        if(!visited[i]){
	            DFS2(i, adj, visited);
	        }
	        
	    }
	}
	vector<int>* getReverse(int V, vector<int> adj[]){
	    vector<int>* reverse = new vector<int>[V];
	    
	    for(int i = 0; i < V; i++){
	        
	        for(int j : adj[i]){
	            reverse[j].push_back(i);
	        }
	    }
	    
	    return reverse;
	}
	
    int kosaraju(int V, vector<int> adj[])
    {        
        vector<bool> visited(V, false);
        stack<int> vertex;
        
        for(int i = 0; i < V; i++){
            if(!visited[i])
                DFS(i, adj, visited, vertex);
        }
        
        vector<bool> visited2(V, false);
        vector<int>* rev = getReverse(V, adj);
        int count = 0;
        
        
        while(!vertex.empty()){
            
            int v = vertex.top();
            vertex.pop();
            if(!visited2[v]){
                DFS2(v, rev, visited2);
                count++;
            }
        }
        
        return count;
            
                
    }
};


int main() {

    int vertex, edge;
    cin >> vertex >> edge;

    vector<int> adj[vertex];

    for(int i = 0; i < edge; i++){
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    KA obj;

    cout << obj.kosaraju(vertex, adj) << endl;
    return 0;
}
