#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        int i=digits.size()-1;
        while(i>=0&&++digits[i]==10)
        {
            digits[i]=0;
            i--;
        }
            
        if(i==-1)
            digits.insert(digits.begin(),1);
       return digits;
    }
};

int main() {

    vector<int> arr = {1,2,9}; 
    vector<int> result;

    // cout << ch;
    // cin.get(str, 100);
    // cout << str;

   

    Solution solution = Solution();
    result = solution.plusOne(arr);
    
    for (int i=0; i<result.size(); i++) {
        cout << result[i];
    }

    cout << endl;

    return 0;
}