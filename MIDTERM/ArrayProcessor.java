import java.util.Scanner;
import java.util.Arrays;

public class ArrayProcessor {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[] originalArray = new int[8];

        System.out.println("Please enter 8 integer numbers:");
        for (int i = 0; i < originalArray.length; i++) {
            System.out.print("Number " + (i + 1) + ": ");
            originalArray[i] = input.nextInt();
        }

        int[] tempUnique = new int[originalArray.length];
        int uniqueCount = 0;

        for (int i = 0; i < originalArray.length; i++) {
            boolean isDuplicate = false;
            for (int j = 0; j < uniqueCount; j++) {
                if (originalArray[i] == tempUnique[j]) {
                    isDuplicate = true;
                    break;
                }
            }
            if (!isDuplicate) {
                tempUnique[uniqueCount] = originalArray[i];
                uniqueCount++;
            }
        }

        int[] uniqueArray = new int[uniqueCount];
        for (int i = 0; i < uniqueCount; i++) {
            uniqueArray[i] = tempUnique[i];
        }

        System.out.println("\n--- Results ---");
        System.out.println("Array after removing duplicates: " + Arrays.toString(uniqueArray));


        if (uniqueCount < 2) {
            System.out.println("Cannot determine second largest or second smallest because there are fewer than 2 unique elements.");
        } else {
            Arrays.sort(uniqueArray);


            int secondSmallest = uniqueArray[1];
            int secondLargest = uniqueArray[uniqueArray.length - 2];

            System.out.println("Second smallest element: " + secondSmallest);
            System.out.println("Second largest element: " + secondLargest);
        }

        input.close();
    }
}
