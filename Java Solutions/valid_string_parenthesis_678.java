class Solution {
    public boolean checkValidString(String s) {
        Stack<Integer> left = new Stack<>();
        Stack<Integer> star = new Stack<>();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='(')
                left.push(i);
            else if (s.charAt(i)=='*')
                star.push(i);
            else{
                if(left.size()==0 && star.size()==0)
                    return false;
                else if (left.size()!=0)
                    left.pop();
                else
                    star.pop();
            }
        }
        if(left.size()==0)
            return true;
        else{
            while(left.size()!=0 && star.size()!=0){
                if(left.pop()>star.pop())
                    return false;
            }
            if(left.size()==0)
                return true;
            else
                return false;
        }
}
}