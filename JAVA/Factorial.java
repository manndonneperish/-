import java.util.Scanner;
public class Factorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个自然数：");
        int n = sc.nextInt(), ans = 1;
        if (n == 0) {
            System.out.println(n+"的阶乘为"+ans);
        }
        else if (n > 0) {
            for (int i = 1; i <= n; i++) {
                ans = ans * i;
            }
            System.out.println(n+"的阶乘为"+ans);
        }
        else {
            System.out.println("输入有误！");
        }
    }
}
