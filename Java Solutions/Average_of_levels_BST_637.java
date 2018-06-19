
public class Average_of_levels_BST_637 {

    List<Double> averages = new ArrayList<Double>();

    public List<Double> averageOfLevels(TreeNode root) {
        Queue<TreeNode> q1 = new LinkedList<>();
        Queue<TreeNode> q2 = new LinkedList<>();
        q1.add(root);
        double total=0;
        while(!(q1.size()==0 && q2.size()==0 )){
            if(q1.size()!=0 ){
                int size= q1.size();
                while(q1.size()!=0){
                    TreeNode temp = q1.peek();
                    if(temp.left!=null)
                        q2.add(temp.left);
                    if(temp.right!=null)
                        q2.add(temp.right);
                    total = total + temp.val;
                    q1.remove();
                }
                averages.add(total/size);
                total=0;
            }
            else if(q2.size()!=0){
                int size= q2.size();
                while(q2.size()!=0){
                    TreeNode temp = q2.peek();
                    if(temp.left!=null)
                        q1.add(temp.left);
                    if(temp.right!=null)
                        q1.add(temp.right);
                    total = total + temp.val;
                    q2.remove();
                }
                averages.add(total/size);
                total=0;

            }

        }
        return averages;

    }

}
