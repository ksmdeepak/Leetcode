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
    List<List<Integer>> output = new ArrayList<List<Integer>>();
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if(root==null)
            return output;
        Stack<TreeNode> s1 = new Stack();
        Stack<TreeNode> s2 = new Stack();
        s1.add(root);
        
        while(!(s1.size()==0 && s2.size()==0)){
            List<Integer> current_level = new ArrayList<Integer>();
            if(s1.size()!=0){
                while(s1.size()!=0){
                    TreeNode temp = s1.peek();
                    // temp = s1.peek();
                    if(temp.left!=null)
                        s2.push(temp.left);
                    if(temp.right!=null)
                        s2.push(temp.right);
                    current_level.add(temp.val);
                    s1.pop();
                }
                output.add(current_level);
            }
            else if(s2.size()!=0){
                while(s2.size()!=0){
                    TreeNode temp = s2.peek();
                    if(temp.right!=null)
                        s1.push(temp.right);
                    if(temp.left!=null)
                        s1.push(temp.left);
                    current_level.add(temp.val);
                    s2.pop();
                }
                output.add(current_level);
            }
        }
        return output;
        
    }
}