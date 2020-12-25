#include<bits/stdc++.h>
#define lli long long int
#define pb push_back
#define in insert
#define mp make_pair
#define pii pair<int,int>
#define piil pair<lli,lli>
#define ff first
#define ss second
#define all(x) x.begin(),x.end()
#define clr(x) memset(x,0,sizeof(x))
#define fo(i,n) for(int i=0;i<n;i++)
#define fo1(i,n) for(int i=1;i<=n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORN(i,a,b) for(int i=a;i>=b;i--)
#define b_pop(x)  __builtin_popcount(x)
#define fast ios_base::sync_with_stdio(0);cin.tie(0);cout.tie()
#define deb(x) cout<<#x<<"="<<x<<"\n"//debugging
#define OJ \
    freopen("input.txt", "r", stdin); \
    freopen("output.txt", "w", stdout);


using namespace std;
const int MX=(int)(2e5)+5;
int darr[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
int arr[MX];
vector<int>graph[MX];

//GCD portion (without Euclids)

template<typename T>
T GCD(T a,T b){
    if(b==0)return a;
    else return GCD(b,a%b);
}


//adding a graph template
void ipgraph(int n,int m){

    int u,v;
    fo1(i,m){
        cin>>u>>v;
        graph[u].pb(v);
        graph[v].pb(u);
    }
}





//problem solver
void solve(){
    
}


int main(){ 
   
    // OJ;

    fast;

    int t;
    // cin>>t;
    t=1;

    while(t--){
        solve();

    }
    
    return 0;
}



