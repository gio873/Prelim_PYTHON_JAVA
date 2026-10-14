import javax.swing.*;
import java.awt.*;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class ProgramSelector extends JFrame {

    private JComboBox<String> cmbPrograms;
    private JTextArea txtOutput;
    private JButton btnRun;

    public ProgramSelector() {
        setTitle("Java Program Launcher");
        setSize(600, 480);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));

        JPanel topPanel = new JPanel(new GridBagLayout());
        topPanel.setBorder(BorderFactory.createEmptyBorder(15, 15, 10, 15));
        GridBagConstraints gbc = new GridBagConstraints();
        
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.insets = new Insets(5, 5, 5, 5);

        JLabel lblSelect = new JLabel("Select a program to run:");
        lblSelect.setFont(new Font("Arial", Font.BOLD, 12));
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.weightx = 0.0;
        topPanel.add(lblSelect, gbc);

        String[] programList = {
            "Display odd numbers between 1 - 100",
            "Sum of odd numbers between 1 - 100",
            "Total number of odd numbers between 1 - 100",
            "Find sum of first n numbers (n=10)",
            "Find the sum of the digits of a number (251025)",
            "Calculate electricity bill (123 units)",
            "Check Armstrong number (153)",
            "Print Armstrong numbers between 1 to 1000",
            "Print given number in words (28)",
            "Check if number is Palindrome (121)",
            "Print palindrome numbers up to 50",
            "Print prime numbers from 1 to 100",
            "Print Pyramid Pattern 1",
            "Print Pyramid Pattern 2",
            "Find largest number in an array",
            "Count number of words in a string",
            "Reverse string and check Palindrome (AMMA)",
            "Delete vowels in a given string"
        };

        cmbPrograms = new JComboBox<>(programList);
        cmbPrograms.setFont(new Font("Arial", Font.PLAIN, 12));
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.weightx = 1.0;
        topPanel.add(cmbPrograms, gbc);

        btnRun = new JButton("Execute Program");
        btnRun.setFont(new Font("Arial", Font.BOLD, 12));
        btnRun.setBackground(new Color(0, 122, 255));
        btnRun.setForeground(Color.WHITE);
        btnRun.setFocusPainted(false);
        btnRun.setPreferredSize(new Dimension(150, 30));
        
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 2;
        gbc.weightx = 1.0;
        gbc.fill = GridBagConstraints.NONE;
        gbc.anchor = GridBagConstraints.CENTER;
        gbc.insets = new Insets(15, 5, 5, 5);
        topPanel.add(btnRun, gbc);

        add(topPanel, BorderLayout.NORTH);

        txtOutput = new JTextArea();
        txtOutput.setFont(new Font("Monospaced", Font.PLAIN, 12));
        txtOutput.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(txtOutput);
        scrollPane.setBorder(BorderFactory.createTitledBorder("Console Output"));
        add(scrollPane, BorderLayout.CENTER);

        btnRun.addActionListener(e -> executeSelectedProgram());
    }

    private void executeSelectedProgram() {
        int index = cmbPrograms.getSelectedIndex();
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        PrintStream ps = new PrintStream(baos);
        PrintStream oldOut = System.out;
        System.setOut(ps);

        try {
            switch (index) {
                case 0: runOddNumbers(); break;
                case 1: runSumOfOdd(); break;
                case 2: runTotalOddCount(); break;
                case 3: runSumFirstN(); break;
                case 4: runDigitsSum(); break;
                case 5: runElectricBill(); break;
                case 6: runArmstrongCheck(); break;
                case 7: runArmstrongRange(); break;
                case 8: runNumberToWords(); break;
                case 9: runPalindromeCheck(); break;
                case 10: runPalindromeRange(); break;
                case 11: runPrimeNumbers(); break;
                case 12: runPyramid1(); break;
                case 13: runPyramid2(); break;
                case 14: runLargestInArray(); break;
                case 15: runWordCount(); break;
                case 16: runStringPalindromeCheck(); break;
                case 17: runRemoveVowels(); break;
            }
        } catch (Exception ex) {
            System.out.println("Execution Error: " + ex.getMessage());
        }

        System.out.flush();
        System.setOut(oldOut);
        txtOutput.setText(baos.toString());
    }

    private void runOddNumbers() {
        System.out.println("The Odd Numbers are:");
        for (int i = 1; i <= 100; i++) {
            if (i % 2 != 0) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }

    private void runSumOfOdd() {
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 2 != 0) {
                sum = sum + i;
            }
        }
        System.out.println("The Sum Of 100 Odd Numbers are:" + sum);
    }

    private void runTotalOddCount() {
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 2 != 0) {
                count++;
            }
        }
        System.out.println("The Count Of Odd Numbers are:" + count);
    }

    private void runSumFirstN() {
        int sum = 0;
        int n = 10;
        for (int i = 1; i <= n; i++) {
            sum = sum + i;
        }
        System.out.println("The Sum Of " + n + " Numbers are:" + sum);
    }

    private void runDigitsSum() {
        int num = 251025, rem = 0, sum = 0, temp;
        temp = num;
        while (num > 0) {
            rem = num % 10;
            sum = sum + rem;
            num = num / 10;
        }
        System.out.print("Sum of Digits of " + temp + " is " + sum);
    }

    private void runElectricBill() {
        int units = 123;
        int bill = 0;
        if (units > 100) {
            if (units >= 200) {
                if (units > 300) {
                    bill = units * 8;
                } else {
                    bill = units * 6;
                }
            } else {
                bill = units * 5;
            }
        }
        System.out.println("Units Consumed : " + units);
        System.out.println("Total Bill : " + bill);
    }

    private void runArmstrongCheck() {
        int n = 153;
        int arg = n;
        int sum = 0, r;
        int tempN = n;
        while (tempN > 0) {
            r = tempN % 10;
            sum = sum + (r * r * r);
            tempN = tempN / 10;
        }
        if (arg == sum) {
            System.out.println("Given number is armstrong number: " + arg);
        } else {
            System.out.println("Given number is not armstrong number: " + arg);
        }
    }

    private void runArmstrongRange() {
        int num, rem, limit = 1000, sum = 0;
        System.out.println("Armstrong numbers from 1 to N:");
        for (int i = 1; i <= limit; i++) {
            num = i;
            while (num > 0) {
                rem = num % 10;
                sum = sum + (rem * rem * rem);
                num = num / 10;
            }
            if (sum == i) {
                System.out.print(i + " ");
            }
            sum = 0;
        }
        System.out.println();
    }

    private void runNumberToWords() {
        int n = 28;
        System.out.println("Number: " + n);
        if (n <= 0) {
            System.out.println("Enter numbers greater than 0");
        } else {
            pw((n / 100) % 10, " hundred");
            pw(n % 100, " ");
        }
    }

    private void pw(int n, String ch) {
        String[] one = {" ", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", "Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"};
        String[] ten = {" ", " ", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", "Seventy", " Eighty", " Ninety"};
        if (n > 19) {
            System.out.print(ten[n / 10] + " " + one[n % 10]);
        } else {
            System.out.print(one[n]);
        }
        if (n > 0) {
            System.out.print(ch);
        }
    }

    private void runPalindromeCheck() {
        int n = 121, pal, r, rev = 0;
        pal = n;
        while (n > 0) {
            r = n % 10;
            rev = rev * 10 + r;
            n = n / 10;
        }
        if (rev == pal) {
            System.out.println(" The given no is palindrome " + rev);
        } else {
            System.out.println("The given no is not palindrome " + rev);
        }
    }

    private void runPalindromeRange() {
        int n, b, rev = 0;
        int limit = 50;
        System.out.println("Palindrome numbers from 1 to N:");
        for (int i = 1; i <= limit; i++) {
            n = i;
            while (n > 0) {
                b = n % 10;
                rev = rev * 10 + b;
                n = n / 10;
            }
            if (rev == i) {
                System.out.print(i + " ");
            }
            rev = 0;
        }
        System.out.println();
    }

    private void runPrimeNumbers() {
        int num = 0, i = 0;
        System.out.println("Prime numbers from 1 to 100 are :");
        for (i = 1; i <= 100; i++) {
            int counter = 0;
            for (num = i; num >= 1; num--) {
                if (i % num == 0) {
                    counter = counter + 1;
                }
            }
            if (counter == 2) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }

    private void runPyramid1() {
        int n = 4;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
System.out.print(" * ");
}
System.out.println();
}
}
private void runPyramid2() {
int i, j, k = 8;
for (i = 0; i < 5; i++) {
for (j = 0; j < k; j++) {
System.out.print(" ");
}
k = k - 2;
for (j = 0; j <= i; j++) {
System.out.print("* ");
}
System.out.println();
}
}
private void runLargestInArray() {
int[] a = new int[]{20, 30, 50, 4, 71, 100};
int max = a[0];
for (int i = 1; i < a.length; i++) {
if (a[i] > max) {
max = a[i];
}
}
System.out.println("The Given Array Element is:");
for (int i = 0; i < a.length; i++) {
System.out.println(a[i]);
}
System.out.println("From The Array Element Largest Number is:" + max);
}
private void runWordCount() {
String s = "welcome to candid java tutorial";
int count = 1;
for (int i = 0; i < s.length() - 1; i++) {
if ((s.charAt(i) == ' ') && (s.charAt(i + 1) != ' ')) {
count++;
}
}
System.out.println("Number of words in a string = " + count);
}
private void runStringPalindromeCheck() {
String inpstr = "AMMA";
char[] inpArray = inpstr.toCharArray();
char[] revArray = new char[inpArray.length];
int j = 0;
for (int i = inpArray.length - 1; i >= 0; i--) {
revArray[j] = inpArray[i];
j++;
}
String revstr = String.valueOf(revArray);
if (inpstr.equals(revstr)) {
System.out.println("The given string is a Palindrome");
} else {
System.out.println("The given string is not a Palindrome");
}
}
private void runRemoveVowels() {
String string = "Welcome to Candid Java Programming";
System.out.println("Input String : " + string);
string = string.replaceAll("[AaEeIiOoUu]", "");
System.out.println("Result: " + string);
}
public static void main(String[] args) {
SwingUtilities.invokeLater(() -> new ProgramSelector().setVisible(true));
}
}