package com.google.challenges; 

public class Answer {   
    public static int answer(int[] numbers) { 
    
        int first_pirate = 0;
        int current_pirate = numbers[first_pirate];
        
        // boolean array keeps track of traversal
        // int array count keeps track of the amount of iterations before a loop is established
        // Max size is 5000 as stated in readme
        int max_size = 5000;
        int[] count = new int[max_size];
        boolean[] array = new boolean[max_size];
        
        // A first traversal has already been done above
        array[first_pirate] = true;
        increment(array, count);

        // Start traversals
        while(array[current_pirate] != true) {
            if(array[current_pirate] != true){
                array[current_pirate] = true;
                current_pirate = numbers[current_pirate];
                increment(array, count);
            }
        }
        return count[current_pirate];
    }
    
    // Increment the counts
    private static void increment(boolean[] arr, int[] count){
        for(int i = 0; i < arr.length; i++){
            if(arr[i] == true){
                count[i] += 1;
            }
        }
    }
}
