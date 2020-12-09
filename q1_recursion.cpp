#include <iostream>
#include <vector>

using namespace std;

void recurse(const vector<int>& lst, int idx=0){

    // Increment before checking base cases
    if (++idx == lst.size()) return;

    // Elem in index "0" counts as elem "1"
    if (idx % 3 == 2){
        cout << lst[idx] << endl;
    }

    recurse(lst, idx);
}

int main(){
    // Setup
    vector<int> nums;
    for(int i = 1; i <= 9; i++){
        nums.push_back(i);
    }

    // The main attraction
    recurse(nums, 0);
    return 0;
}
