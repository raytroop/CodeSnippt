// Definition for singly-linked list.
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(long x) : val(x), next(NULL) {}
};
 
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* p = &dummy;
        int cn = 0;
        int val = 0;
        while(l1 || l2){
            val = cn + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
            cn = val / 10;
            val = val % 10;
            p->next = new ListNode(val);
            p = p->next;
            if(l1)
                l1 = l1->next;
            if(l2)
                l2 = l2->next;
        }

        if(cn){
            p->next = new ListNode(cn);
            p = p->next;
        }

        return dummy.next;
    }
};

int main(){
    vector<int> l1_vals{9};
    vector<int> l2_vals{1,9,9,9,9,9,9,9,9,9};
    ListNode* l1 = new ListNode(9);
    int n = l2_vals.size();
    // cout << n << endl;
    ListNode* l2 = new ListNode(1);
    ListNode* flag=l2;
    ListNode* temp(nullptr);

    for(int i=1; i< n; i++){
        temp = new ListNode(l2_vals[i]);
        flag->next = temp;
        flag = temp;
    }
    flag = l2;
    int val;
    // do{
    //     val = flag->val;
    //     cout << val << endl;
    // } while(flag = flag->next);
    
    Solution solver;
    ListNode* re = solver.addTwoNumbers(l1, l2);

    flag = re;
    do{
        val = flag->val;
        cout << val << endl;
    } while(flag = flag->next);
    return 0;

}