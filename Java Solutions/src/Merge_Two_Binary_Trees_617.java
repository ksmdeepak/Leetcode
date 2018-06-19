

class Merge_Two_Binary_Trees_617 {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {

        if(t1!=null && t2!=null){
            t1.val=t1.val+t2.val;
        }
        else if(t1==null && t2!=null){
            t1= new TreeNode(t2.val);
            t1.left = t2.left;
            t1.right = t2.right;
            t2.val=0;
            t2.left=null;
            t2.right=null;


        }
        else if(t1!=null && t2==null){
            t2 = new TreeNode(0);
            t2.left=null;
            t2.right=null;
        }
        else{
            return null;
        }
        t1.left=mergeTrees(t1.left,t2.left);
        t1.right=mergeTrees(t1.right,t2.right);

        return t1;

    }
}