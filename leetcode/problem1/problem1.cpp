#include <iostream>
#include <vector>
// #include <unordered_map>

using namespace std;

class Solution 
{
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            // unordered_map<int, int> m;
            // vector<int> res;

            vector<int>& res = nums;

            for (vector<int>::const_iterator iter = res.cbegin(); iter != res.cend(); iter++)
            {
                cout << (*iter) << endl;
            }

            return res;
        }
};

int main(int argc, char const *argv[])
{
    int arr[] = {2, 7, 11, 15};
    int target = 9;
    vector<int> nums(arr, arr + sizeof(arr));

    Solution solution = Solution();
    vector<int> result = solution.twoSum(nums, target);

    cout << result.back() << ' ' << result.front() << endl;

    return 0;
}