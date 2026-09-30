import java.util.Scanner;

public class EvenOddElements {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Size of Array : ");
        int size = input.nextInt();

        int[] arr = new int[size];

        System.out.println("Enter any " + size + " elements in Array:");
        for (int i = 0; i < size; i++) {
            arr[i] = input.nextInt();
        }

        System.out.print("Even Elements: ");
        for (int i = 0; i < size; i++) {
            if (arr[i] % 2 == 0) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();

        System.out.print("Odd Elements: ");
        for (int i = 0; i < size; i++) {
            if (arr[i] % 2 != 0) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();

        input.close();
    }
}