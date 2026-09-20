import java.util.Scanner;

public class WordPhraseScanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first word: ");
        String word1 = scanner.next();

        System.out.print("Enter second word: ");
        String word2 = scanner.next();

        System.out.print("Enter third word: ");
        String word3 = scanner.next();

        System.out.println(word1 + " " + word2 + " " + word3);

        scanner.close();
    }
}