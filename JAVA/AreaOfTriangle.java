import java.util.Scanner;
public class AreaOfTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入三角形的三边长（以空格分割）：");
        String str = sc.nextLine();
        String[] strs = str.split(" ");
        double a = Double.parseDouble(strs[0]), b = Double.parseDouble(strs[1]), c = Double.parseDouble(strs[2]);
        double s = (a + b + c) / 2, area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        System.out.println("三角形的面积为"+area);
    }
}
