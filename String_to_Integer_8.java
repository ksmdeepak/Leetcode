public class String_to_Integer_8 {

    public int myAtoi(String str) {
        int starting =0 ;
        for (int i = 0, n = str.length(); i < n; i++) {
            char c = str.charAt(i);

            if(c!=' '){
                break;
            }
            starting++;
        }

        String input = str.substring(starting,str.length());

//        System.out.println(input);

        if(input.length()==0) return 0;

        int sign=1;
        char c = input.charAt(0);
        if(c=='+'){
            sign=1;
            input = input.substring(1,input.length());
        }
        else if(c=='-'){
            sign=-1;
            input = input.substring(1,input.length());
        }
        else if(!Character.isDigit(c)){
            return 0;
        }

        int end= input.length();

        for (int i = 0, n = input.length(); i < n; i++) {
            c = input.charAt(i);
            if (c==' ' || !Character.isDigit(c)){

                end= i;
                break;
            }
        }
        int output;
        try {
            if(end==0){
                return 0;
            }
            output = sign*Integer.parseInt(input.substring(0,end));
        } catch (NumberFormatException e) {
            if( sign==1)
                output = 2147483647;
            else
                output = -2147483648;
        }

        return output;

    }

    public static void main(String args[]){
        String input= args[0];
        String_to_Integer_8 obj = new String_to_Integer_8();
        System.out.println(obj.myAtoi(input));
    }

}
