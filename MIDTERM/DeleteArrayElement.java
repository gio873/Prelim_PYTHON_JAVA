import java.util.Scanner;

public class DeleteArrayElement {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[] arr = new int[5];

        System.out.print("Enter Data in Array: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = input.nextInt();
        }

        System.out.print("Stored Data in Array: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        System.out.print("Enter poss. of Element to Delete: ");
        int pos = input.nextInt();

        System.out.print("New data in Array: ");
        for (int i = 0; i < arr.length; i++) {
            if (i != pos) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();

        input.close();
    }
}