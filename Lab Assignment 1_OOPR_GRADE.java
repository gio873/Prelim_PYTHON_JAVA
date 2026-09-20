import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String choice;

        do {
            System.out.print("Java Score: ");
            double javaScore = scanner.nextDouble();

            System.out.print("C Score: ");
            double cScore = scanner.nextDouble();

            System.out.print("Database Handling score: ");
            double dbScore = scanner.nextDouble();

            double average = (javaScore + cScore + dbScore) / 3.0;
            double truncatedAverage = ((int)(average * 1000)) / 1000.0;

            int range = (int) average / 10;
            char grade;

            if (average < 0 || average > 100) {
                grade = 'F';
            } else {
                switch (range) {
                    case 10:
                    case 9:
                        grade = 'A';
                        break;
                    case 8:
                        grade = 'B';
                        break;
                    case 7:
                        if (average >= 75) {
                            grade = 'C';
                        } else {
                            grade = 'F';
                        }
                        break;
                    default:
                        grade = 'F';
                        break;
                }
            }

            System.out.println("Output:");
            System.out.println(grade);
            System.out.println("Explanation:");
            System.out.printf("The average of the student is %.3f, so the student's grade is %c.\n", truncatedAverage, grade);

            System.out.print("Do you want to continue : YES / NO ");
            choice = scanner.next();

        } while (choice.equalsIgnoreCase("YES"));

        scanner.close();
    }
}
