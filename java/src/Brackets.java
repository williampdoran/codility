import java.util.Map;
import java.util.Stack;

public class Brackets{
    public static boolean solution(String s){
        Stack<Character> chars = new Stack<>();
        Map<Character, Character> brackets = Map.of('{','}','(',')', '[',']');
        for(Character c : s.toCharArray()){
            if(brackets.keySet().contains(c)){
                chars.push(c);
            }
            else if(!chars.empty() && brackets.containsValue(c)){
                Character popped = chars.pop();
                if(c != brackets.get(popped)){
                    return false;
                }
            }
        }
        return chars.size() == 0;
    }
    public static void main(String[] args) {
        System.out.println(solution("{[()()]}"));
        System.out.println(solution("([)()]"));

    }
}
