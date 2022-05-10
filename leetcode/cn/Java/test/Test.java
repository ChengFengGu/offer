package test;
import _92_Reverse_Linked_List_II.*;
import algm.*;
import java.util.List;
public class Test {
    public static void main(String[] args){
        String str="[[\"[1,2,3,4,5]\",\"2\",\"4\"]]";
        String[][] arr = Util.parseStringArrArr(str);
      
        for(int i=0;i<arr.length;i++){
            String[] unitArgs=arr[i];
            Solution s=new Solution();
            ListNode arg0 = Util.parseListNode(unitArgs[0]);
            int arg1 = Util.parseInteger(unitArgs[1]);
            int arg2 = Util.parseInteger(unitArgs[2]);
            ListNode result=s.reverseBetween(arg0,arg1,arg2);
            String resultabc =Util.serializeListNode(result);
            System.out.print("resultabc"+Integer.toString(i)+":"+resultabc+"resultend");
        }
    }
}