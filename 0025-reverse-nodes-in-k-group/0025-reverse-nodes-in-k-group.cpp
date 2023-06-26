class Solution {
    
    void reverse(ListNode *start, ListNode *end){
        ListNode *prev = NULL, *curr = start, *fwd = NULL;
        
        while(prev != end){
            fwd = curr -> next;
            curr -> next = prev;
            prev = curr;
            curr = fwd;
        }
    }
    
    ListNode* calculateEnd(int k, ListNode *start){
        int jumps = k - 1;
        ListNode *start1 = start;
        while(jumps--){
            start = start -> next;
            
            if(start == NULL){   /* size of sub-linkedlist is less than k */
                return start1;
            }
        }
        return start;
    }
    
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        
        if(head == NULL || head->next == NULL || k == 1){
            return head;
        }
        ListNode *start = head, *end = head, *ptr = NULL, *newHead = NULL;
        
        end = calculateEnd(k, start);
        newHead = end;
        
        ListNode *temp = end->next;
        reverse(start, end);
      
        
        while(temp != NULL){  
            ptr = start;
            start = temp;
            end = calculateEnd(k, start);            
            if(start == end){    /* when we reach the last sub-linkedlist which has size less than k */
                ptr->next = start;
                break;
            }  
            temp = end->next;
            reverse(start, end);
            ptr->next = end;
        }
        
        return newHead;
       
    }
};