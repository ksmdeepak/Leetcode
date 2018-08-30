/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int leaves=0;
    int height=-1;
    int flag=0;
    public void traverse(TreeNode root,int level){
        if(level==height-1 && flag==0){
            if(root.left!=null){
                leaves++;
            }
            else{
                flag=1;
                
            }
            if(root.right!=null){
                leaves++;
            }
            else{
                flag=1;
                
            }
            return;
        }
        if(flag==0){
            traverse(root.left,level+1);
            traverse(root.right,level+1);
        }
        else 
            return;
    }
    public int countNodes(TreeNode root) {
        if(root==null)
            return 0;
        TreeNode temp=root;
        int count=0;
        while(temp!=null){
            temp=temp.left;  
            height++;
            count = count + (int) Math.pow(2,height);
        }
        if(height==0)
            return 1;
        
        count=count-(int) Math.pow(2,height);
        
        traverse(root,0);
        return count+leaves;
    }
}