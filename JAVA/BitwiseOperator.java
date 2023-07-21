public class BitwiseOperator {
    public static void main(String[] args) {
        int password = 751248; // 原密码
        int key = 7; // 加密参数
        System.out.println("原密码：" + password);
        password = password << key; // 将原密码左移，生成新数字
        System.out.println("左移加密后的结果：" + password);
        password = password >> key; // 将新数字右移还原
        System.out.println("右移还原后的结果：" + password);
    }
}