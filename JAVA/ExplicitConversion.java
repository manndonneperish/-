public class ExplicitConversion {
    public static void main(String[] args) {
        int a = (int) 45.23; // double 类型强制转换为 int 类型
        long b = (long) 456.6f; // float 类型强制转换为 long 类型
        char c = (char) 97.14; // double 类型强制转化为 char 类型
        System.out.println("45.23 强制转换为 int 的结果：" + a);
        System.out.println("456.6f 强制转换为 long 的结果：" + b);
        System.out.println("97.14 强制转换为 char 的结果：" + c);
    }
}
