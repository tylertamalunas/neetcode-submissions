class Solution {
    public boolean isValid(String s) {
        // make a deque/stack
        // if opener, push
        // else if closer, check if top is open of same


        Deque<Character> stack = new LinkedList<>();

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else if (stack.isEmpty()) return false;
            else {
                if (c == ')' && stack.peek() != '(') return false;
                else if (c == ']' && stack.peek() != '[') return false;
                else if (c == '}' && stack.peek() != '{') return false;
                stack.pop();
            } 
        }
        return stack.isEmpty();
    }
}
