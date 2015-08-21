package com.google.challenges; 
import java.util.*;

public class Answer {   
    public static String[] answer(String[] names) { 

        // Your code goes here.
        Arrays.sort(names, new scoreComparator());
        return names;
        
    } 
    
    // Gets the score value of the letter
    private static int getLetterVal(char c) {
        return Character.getNumericValue(c) - 9;
    }
    
    // Gets the score value of the name
    private static int getNameScore(String name) {
        int score = 0;
        for(int i = 0; i < name.length(); i++){
            char c = name.charAt(i);
            score += getLetterVal(c);
        }
        return score;
    }
    
    // A comparator to sort the names in descending oder by score
    private static class scoreComparator implements java.util.Comparator<String> {
        @Override
        public int compare(String s1, String s2) {
            int val1 = getNameScore(s1);
            int val2 = getNameScore(s2);
            if(val1 > val2)
                return -1;

            if(val2 > val1)
                return 1;

            // Handles the same score case and compares for the lexicographically larger name.
            if(val1 == val2){
                int ls1 = s1.length();
                int ls2 = s2.length();
                int len = ls1 > ls2 ? ls2 : ls1;
                for(int i = 0; i < len; i++){
                    int lexcompare1 = getLetterVal(s1.charAt(i));
                    int lexcompare2 = getLetterVal(s2.charAt(i));
                    if(lexcompare2 > lexcompare1) {
                        return 1;
                    } else if (lexcompare1 > lexcompare2) {
                        return -1;
                    }
                }
            }

            return 0;
        }
    }
    
}