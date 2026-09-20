import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String choice;
        
        do {
        System.out.println("Enter value for x: ");
        int x = scanner.nextInt();

        System.out.println("Enter value for y: ");
           int y = scanner.nextInt();

        double result = 0.0;
        System.out.println("Variable values:");
        System.out.println("x = " + x);
        System.out.println("y = " + y);

        System.out.println("Arithmetic Operation:");
        
        result = x + y;
        System.out.printf("Addition: x + y = %.1f\n", result);

        result = x - y;
        System.out.printf("Subtraction: x - y = %.1f\n", result);

        result = x * y;
        System.out.printf("Multiplication: x * y = %.1f\n", result);

        result = x / y;
        System.out.printf("Division: x / y = %.1f\n", result);

        result = x % y;
        System.out.printf("Modulus: x %% y = %.1f\n", result);

        int tempX = x;
        tempX++;
        result = tempX;
        System.out.printf("Increment: x++ = %.1f\n", result);

        tempX = x;
        tempX--;
        result = tempX;
        System.out.printf("Decrement: x-- = %.1f\n", result);

        System.out.print("Do you want to continue : YES / NO ");
            choice = scanner.next();

        } while (choice.equalsIgnoreCase("YES"));

        scanner.close();
    }
}
