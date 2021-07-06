#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
   int minSetSize(vector<int>& arr) {
      unordered_map <int, int> m;
      int n = arr.size();
      for(int i = 0; i < n; i++){
         m[arr[i]]++;
      }
      vector <int> temp;
      unordered_map <int, int> :: iterator it = m.begin();
      int sz = n;
      int ret = 0;
      while(it != m.end()){
         temp.push_back(it->second);
         it++;
      }
      sort(temp.rbegin(), temp.rend());
      for(int i = 0; i < temp.size(); i++){
         if(sz <= n / 2)break;
         ret++;
         sz -= temp[i];
      }
      return ret;
   }
};
main(){
   vector<int> v = {3,3,3,3,5,5,5,2,2,7};
   Solution ob;
   cout << (ob.minSetSize(v));
}
