


public class Trim_BST_669 {


        public boolean checkBoundaryConditions(int val, int L,int R){
            if(val>=L && val<=R)
                return true;
            else
                return false;
        }
        public TreeNode trimBST(TreeNode root, int L, int R) {
            if(root==null) return null;

            root.left = trimBST(root.left,L,R);
            root.right = trimBST(root.right,L,R);

            if(checkBoundaryConditions(root.val,L,R)){
                return root;
            }

            else{
                if(root.val<=R && root.right!=null && checkBoundaryConditions(root.right.val,L,R) )
                    return root.right;
                else if(root.val>=L && root.left!=null && checkBoundaryConditions(root.left.val,L,R) )
                    return root.left;
                else
                    return null;
            }
        }

}
