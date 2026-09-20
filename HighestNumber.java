import java.util.Scanner;

public class HighestNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();

        System.out.print("Enter third number: ");
        double num3 = scanner.nextDouble();

        double highest = Math.max(num1, Math.max(num2, num3));

        if (highest == (long) highest) {
            System.out.println("The highest number is " + (long) highest);
        } else {
            System.out.println("The highest number is " + highest);
        }

        scanner.close();
    }
}