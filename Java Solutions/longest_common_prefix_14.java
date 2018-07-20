class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length==0)
            return "";
        int pos =0;
        while(true){
            if(!(pos<strs[0].length())){
                    return strs[0].substring(0,pos);
            } 
            char c = strs[0].charAt(pos);
            int flag=0;
            for(int i=0;i<strs.length;i++){
                if(!(pos<strs[i].length())){
                    flag=1;
                    break;
                }       
                if(strs[i].charAt(pos)!=c){
                    flag=1;
                    break;
                }
                    
            }
            if(flag==1){
                if(pos==0)
                    return "";
                else
                    return strs[0].substring(0,pos);
            }
            else
                pos++;
        }
        
        
    }
}