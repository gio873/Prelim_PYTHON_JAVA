import java.util.Date;
import java.text.SimpleDateFormat;

public class Student {
    private String studentNo;
    private String studentName;
    private Date dateOfBirth;
    private int tariffPoints;
    
    private static int noOfStudents = 0;

    public Student() {
        this.studentNo = "not known";
        this.studentName = "not known";
        try {
            this.dateOfBirth = new SimpleDateFormat("dd/MM/yyyy").parse("01/01/1995");
        } catch (Exception e) {
            this.dateOfBirth = null;
        }
        this.tariffPoints = 20;
        noOfStudents++;
    }

    public Student(String studentNo, String studentName, Date dateOfBirth, int tariffPoints) {
        setStudentNo(studentNo);
        setStudentName(studentName);
        setDateOfBirth(dateOfBirth);
        setTariffPoints(tariffPoints);
        noOfStudents++;
    }

    public String getStudentNo() {
        return studentNo;
    }

    public void setStudentNo(String studentNo) {
        if (studentNo == null || studentNo.trim().isEmpty()) {
            this.studentNo = "not known";
        } else {
            this.studentNo = studentNo;
        }
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        if (studentName == null || studentName.trim().isEmpty()) {
            this.studentName = "not known";
        } else {
            this.studentName = studentName;
        }
    }

    public Date getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(Date dateOfBirth) {
        if (dateOfBirth == null || dateOfBirth.after(new Date())) {
            throw new IllegalArgumentException("Invalid date of birth.");
        }
        this.dateOfBirth = dateOfBirth;
    }

    public int getTariffPoints() {
        return tariffPoints;
    }

    public void setTariffPoints(int tariffPoints) {
        if (tariffPoints < 20 || tariffPoints > 280) {
            throw new IllegalArgumentException("Tariff points must be between 20 and 280.");
        }
        this.tariffPoints = tariffPoints;
    }

    public static int getNoOfStudents() {
        return noOfStudents;
    }

    @Override
    public String toString() {
        SimpleDateFormat fmt = new SimpleDateFormat("dd/MM/yyyy");
        String dobStr = (dateOfBirth != null) ? fmt.format(dateOfBirth) : "not known";
        return "Student Details:\n" +
               "---------------------\n" +
               "Student No   : " + studentNo + "\n" +
               "Name         : " + studentName + "\n" +
               "Date of Birth: " + dobStr + "\n" +
               "Tariff Points: " + tariffPoints + "\n";
    }

    public static void main(String[] args) {
        Student student1 = new Student();

        Date specificDate;
        try {
            specificDate = new SimpleDateFormat("dd/MM/yyyy").parse("15/08/2004");
        } catch (Exception e) {
            specificDate = new Date();
        }
        Student student2 = new Student("S12345", "Alex Smith", specificDate, 180);

        System.out.println(student1);
        System.out.println(student2);
        System.out.println("Total Students Registered: " + Student.getNoOfStudents());
    }
}
