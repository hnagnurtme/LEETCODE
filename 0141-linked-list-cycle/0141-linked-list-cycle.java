/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> li = new HashSet<>();
        while( head != null){
            if( li.contains(head)){
                return true;
            }

            li.add(head);
            head = head.next;
        }

        return false;
        
    }
}