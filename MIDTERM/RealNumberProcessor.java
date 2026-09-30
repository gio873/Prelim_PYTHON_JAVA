import java.util.Scanner;

public class RealNumberProcessor {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double[] numbers = new double[10];
        
        System.out.println("Please enter 10 real numbers (positive or negative):");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print("Number " + (i + 1) + ": ");
            numbers[i] = input.nextDouble();
        }
        
        double sumPositive = 0;
        int countPositive = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] > 0) {
                sumPositive += numbers[i];
                countPositive++;
            }
        }
        
        int countNegative = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] < 0) {
                countNegative++;
            }
        }
        
        double minValue = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] < minValue) {
                minValue = numbers[i];
            }
        }
        
        System.out.println("\n--- Results ---");
        if (countPositive > 0) {
            double averagePositive = sumPositive / countPositive;
            System.out.println("Sum of positive numbers: " + sumPositive);
            System.out.println("Average of positive numbers: " + averagePositive);
        } else {
            System.out.println("No positive numbers were entered.");
        }
        
        System.out.println("Count of negative numbers: " + countNegative);
        System.out.println("Minimum value in the array: " + minValue);
        
        input.close();
    }
}
