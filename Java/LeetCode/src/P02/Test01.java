package P02;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

public class Test01 {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(),tail = head;
        int carry = 0;
        while (l1 != null || l2 != null){
            int n1 = l1 != null ? l1.val:0;
            int n2 = l2 != null? l2.val:0;
            int sum = n1+n2+carry;

            tail.next = new ListNode(sum%10);
            tail = tail.next;

            if(l1 != null){
                l1 =  l1.next;
            }
            if(l2 != null){
                l2 =  l2.next;
            }

            carry = (sum)/10;
        }
        if(carry != 0){
            tail.next = new ListNode(carry);
            tail = tail.next;
        }
        return  head.next;
    }

    public static void main(String[] args) {
//        [2,4,3]

        ListNode l1 = new  ListNode(2,new ListNode(4,new ListNode(3)));
        ListNode l2 = new  ListNode(5,new ListNode(6,new ListNode(4)));
        ListNode result = Test01.addTwoNumbers(l1,l2);
        while (result != null){
            System.out.print(result.val+",");
            result = result.next;
        }
    }
}
