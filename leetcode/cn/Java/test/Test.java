package test;
import _66_Plus_One.*;
import algm.*;
import java.util.List;
public class Test {
    public static void main(String[] args){
        String str="[[\"[1,2,3]\"],[\"[4,3,2,1]\"],[\"[9]\"]]";
        String[][] arr = Util.parseStringArrArr(str);
      
        for(int i=0;i<arr.length;i++){
            String[] unitArgs=arr[i];
            Solution s=new Solution();
            int[] arg0 = Util.parseIntegerArr(unitArgs[0]);
            int[] result=s.plusOne(arg0);
            String resultabc =Util.serializeIntegerArr(result);
            System.out.print("resultabc"+Integer.toString(i)+":"+resultabc+"resultend");
        }
    }
}