import java.util.Scanner;
public class LonginService {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // 创建扫描器，获取控制台输入的值
        System.out.println("请输入 6 位数字密码：");
        int password = sc.nextInt(); // 将用户在控制台输入的整数赋值给整型变量
        boolean result = (password == 924867);
        System.out.println("用户密码是否正确：" + result);
        sc.close(); // 关闭扫描器
    }
}
