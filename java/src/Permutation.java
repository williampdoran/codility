import java.util.HashMap;
import java.util.Map;

public class Permutation {
    public static boolean permutation(String w1, String w2) {
        return counts(w2).equals(counts(w1));
    }
    private static Map<Character, Integer> counts(String word){
        Map<Character, Integer> counts = new HashMap<Character, Integer>();
        for(Character c : word.toCharArray()){
            if(counts.containsKey(c)){
                counts.put(c, counts.get(c) + 1);
            }
            else {
                counts.put(c, 1);
            }
        }
        return counts;
    }
    public static void main(String[] args) {
        String[][] pairs = {{"apple", "papel"}, {"carrot", "tarroc"}, {"hello", "llloh"}};
        for (String[] pair : pairs) {
            String word1 = pair[0];
            String word2 = pair[1];
            boolean anagram = permutation(word1, word2);
            System.out.println(word1 + ", " + word2 + ": " + anagram);
        }
    }
}
