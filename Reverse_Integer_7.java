public class Reverse_Integer_7 {

    public static void main(String args[]){
        int x = Integer.parseInt(args[0]);
        String input = Integer.toString(x);
        int sign = 1;
        if(x<0){
            sign = -1;
            input = input.substring(1,input.length());
        }

        StringBuilder input1 = new StringBuilder();

        input1.append(input);

        input1 = input1.reverse();


        int solution =0;
        try {
            solution = Integer.parseInt(input1.toString());
        } catch (NumberFormatException e) {
            solution = 0;
        }
        solution = sign * solution;
        int limit = (int) Math.pow(2, 31);

        if (solution > limit - 1 || solution < -1*limit ){
            System.out.println(0);
        }

        else{
            System.out.println(solution);
        }
    }
}
