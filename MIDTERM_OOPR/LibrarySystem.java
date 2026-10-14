import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.time.LocalDate;
import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class LibrarySystem extends JFrame {

    private JTextField txtTotalPages;
    private JTextField txtPagesRead;
    private JTextField txtIssueDate;
    private JTextField txtDueDate;
    private JButton btnCalculate;

    static class CalendarIcon implements Icon {
        @Override
        public void paintIcon(Component c, Graphics g, int x, int y) {
            Graphics2D g2 = (Graphics2D) g.create();
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            
            g2.setColor(Color.WHITE);
            g2.fillRect(x + 2, y + 2, 14, 14);
            
            g2.setColor(Color.BLACK);
            g2.drawRect(x + 2, y + 2, 14, 14);
            
            g2.setColor(new Color(200, 0, 0));
            g2.fillRect(x + 3, y + 3, 13, 4);
            
            g2.setColor(Color.LIGHT_GRAY);
            g2.drawLine(x + 6, y + 10, x + 6, y + 13);
            g2.drawLine(x + 9, y + 10, x + 9, y + 13);
            g2.drawLine(x + 12, y + 10, x + 12, y + 13);
            g2.drawLine(x + 5, y + 11, x + 13, y + 11);
            
            g2.dispose();
        }

        @Override
        public int getIconWidth() {
            return 18;
        }

        @Override
        public int getIconHeight() {
            return 18;
        }
    }

    public LibrarySystem() {
        setTitle("Library System - OOP Lab Activity #2");
        setSize(550, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(null);

        JLabel lblHeader = new JLabel("Welcome Angelo Austero", SwingConstants.CENTER);
        lblHeader.setFont(new Font("Arial", Font.BOLD, 14));
        lblHeader.setBounds(10, 20, 510, 25);
        add(lblHeader);

        JLabel lblTotalPages = new JLabel("How many pages does the book have?");
        lblTotalPages.setBounds(40, 65, 250, 20);
        add(lblTotalPages);

        txtTotalPages = new JTextField("100");
        txtTotalPages.setBounds(40, 90, 150, 25);
        add(txtTotalPages);
        preventNegativeInput(txtTotalPages);

        JLabel lblPagesRead = new JLabel("How many pages have you read?");
        lblPagesRead.setBounds(40, 140, 250, 20);
        add(lblPagesRead);

        txtPagesRead = new JTextField("50");
        txtPagesRead.setBounds(40, 165, 150, 25);
        add(txtPagesRead);
        preventNegativeInput(txtPagesRead);

        JLabel lblIssueDate = new JLabel("Issue Date");
        lblIssueDate.setBounds(330, 65, 100, 20);
        add(lblIssueDate);

        txtIssueDate = new JTextField("08 01, 21");
        txtIssueDate.setBounds(330, 90, 100, 25);
        add(txtIssueDate);

        JButton btnCal1 = new JButton(new CalendarIcon());
        btnCal1.setBounds(435, 90, 45, 25);
        add(btnCal1);
        btnCal1.addActionListener(e -> showCalendarPopup(txtIssueDate));

        JLabel lblDueDate = new JLabel("Due Date");
        lblDueDate.setBounds(330, 140, 100, 20);
        add(lblDueDate);

        txtDueDate = new JTextField("08 15, 21");
        txtDueDate.setBounds(330, 165, 100, 25);
        add(txtDueDate);

        JButton btnCal2 = new JButton(new CalendarIcon());
        btnCal2.setBounds(435, 165, 45, 25);
        add(btnCal2);
        btnCal2.addActionListener(e -> showCalendarPopup(txtDueDate));

        btnCalculate = new JButton("Calculate");
        btnCalculate.setBounds(180, 220, 150, 30);
        add(btnCalculate);

        btnCalculate.addActionListener(e -> calculateLibraryMetrics());
    }

    private void preventNegativeInput(JTextField textField) {
        textField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyTyped(KeyEvent e) {
                char c = e.getKeyChar();
                if (c == '-') {
                    e.consume();
                }
            }
        });
    }

    private void showCalendarPopup(JTextField targetTextField) {
        JDialog calendarDialog = new JDialog(this, "Select Date", true);
        calendarDialog.setSize(320, 260);
        calendarDialog.setLocationRelativeTo(targetTextField);
        calendarDialog.setLayout(new BorderLayout());

        int currentYear = 2021;
        int currentMonth = 8;

        try {
            DateTimeFormatter initFormatter = DateTimeFormatter.ofPattern("MM dd, yy");
            LocalDate currentFieldDate = LocalDate.parse(targetTextField.getText().trim(), initFormatter);
            currentYear = currentFieldDate.getYear();
            currentMonth = currentFieldDate.getMonthValue();
        } catch (Exception ignored) {}

        JPanel controlPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 5, 5));
        
        String[] months = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
        JComboBox<String> monthCombo = new JComboBox<>(months);
        monthCombo.setSelectedIndex(currentMonth - 1);
        
        Integer[] years = new Integer[101];
        for (int i = 0; i <= 100; i++) {
            years[i] = 2000 + i;
        }
        JComboBox<Integer> yearCombo = new JComboBox<>(years);
        yearCombo.setSelectedItem(currentYear);

        controlPanel.add(monthCombo);
        controlPanel.add(yearCombo);
        calendarDialog.add(controlPanel, BorderLayout.NORTH);

        JPanel daysContainer = new JPanel(new BorderLayout());
        calendarDialog.add(daysContainer, BorderLayout.CENTER);

        Runnable updateDaysGrid = new Runnable() {
            @Override
            public void run() {
                daysContainer.removeAll();
                
                int selMonth = monthCombo.getSelectedIndex() + 1;
                int selYear = (Integer) yearCombo.getSelectedItem();
                YearMonth yearMonth = YearMonth.of(selYear, selMonth);

                JPanel daysPanel = new JPanel(new GridLayout(0, 7, 2, 2));
                String[] headers = {"Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"};
                for (String header : headers) {
                    JLabel lbl = new JLabel(header, SwingConstants.CENTER);
                    lbl.setFont(new Font("Arial", Font.BOLD, 11));
                    daysPanel.add(lbl);
                }

                int startDayOfWeek = yearMonth.atDay(1).getDayOfWeek().getValue() % 7;
                for (int i = 0; i < startDayOfWeek; i++) {
                    daysPanel.add(new JLabel(""));
                }

                int totalDays = yearMonth.lengthOfMonth();
                for (int day = 1; day <= totalDays; day++) {
                    final int selectedDay = day;
                    JButton btnDay = new JButton(String.valueOf(day));
                    btnDay.setMargin(new Insets(2, 2, 2, 2));
                    btnDay.setFont(new Font("Arial", Font.PLAIN, 11));

                    btnDay.addActionListener(e -> {
                        int shortYear = selYear % 100;
                        String formattedDate = String.format("%02d %02d, %02d", selMonth, selectedDay, shortYear);
                        targetTextField.setText(formattedDate);
                        calendarDialog.dispose();
                    });
                    daysPanel.add(btnDay);
                }

                daysContainer.add(daysPanel, BorderLayout.CENTER);
                daysContainer.revalidate();
                daysContainer.repaint();
            }
        };

        monthCombo.addActionListener(e -> updateDaysGrid.run());
        yearCombo.addActionListener(e -> updateDaysGrid.run());

        updateDaysGrid.run();
        calendarDialog.setVisible(true);
    }

    private void calculateLibraryMetrics() {
        try {
            int totalPages = Integer.parseInt(txtTotalPages.getText().trim());
            int pagesRead = Integer.parseInt(txtPagesRead.getText().trim());

            if (totalPages <= 0 || pagesRead < 0) {
                JOptionPane.showMessageDialog(this, "Page counts cannot be zero or negative numbers.", "Input Error", JOptionPane.ERROR_MESSAGE);
                return;
            }

            if (pagesRead > totalPages) {
                JOptionPane.showMessageDialog(this, "Pages read cannot exceed the total pages of the book.", "Input Error", JOptionPane.ERROR_MESSAGE);
                return;
            }

            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM dd, yy");
            LocalDate issueDate = LocalDate.parse(txtIssueDate.getText().trim(), formatter);
            LocalDate dueDate = LocalDate.parse(txtDueDate.getText().trim(), formatter);

            int percentageRead = (int) (((double) pagesRead / totalPages) * 100);

            long daysRemaining = ChronoUnit.DAYS.between(issueDate, dueDate);
            if (daysRemaining < 0) daysRemaining = 0;

            int pagesLeft = totalPages - pagesRead;
            int pagesPerDay = (daysRemaining > 0) ? (int) Math.ceil((double) pagesLeft / daysRemaining) : pagesLeft;

            String message = String.format(
                    "You have read %d%% of the book.\n" +
                    "You have %d day(s) remaining to return the book.\n" +
                    "You still have %d page(s) left and you should read %d pages a day",
                    percentageRead, daysRemaining, pagesLeft, pagesPerDay
                );

            JOptionPane.showMessageDialog(this, message, "Message", JOptionPane.INFORMATION_MESSAGE);

        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Invalid input format! Double check numeric values and date layout strings (MM dd, yy).",
"Input Error", JOptionPane.ERROR_MESSAGE);
}
}
public static void main(String[] args) {
SwingUtilities.invokeLater(() -> new LibrarySystem().setVisible(true));
}
}
    