import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter first word: ");
        String word1 = reader.readLine();

        System.out.print("Enter second word: ");
        String word2 = reader.readLine();

        System.out.print("Enter third word: ");
        String word3 = reader.readLine();

        System.out.println(word1 + " " + word2 + " " + word3);
    }
}
