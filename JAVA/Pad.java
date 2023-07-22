class Computer { //父类
    String screen = "液晶显示屏"; //父类属性
    String sayHello() { //父类方法 1
        return "欢迎使用";
    }
    void startup() { //父类方法 2
        System.out.println("电脑正在开机，请等待…");
    }
    void showPicture() { //父类方法 3
        System.out.println("鼠标点击");
    }
}

public class Pad extends Computer { //子类
    String battery = "5000 毫安电池"; //子类属性
    String sayHello() { //重写父类方法 1
        return super.sayHello() + "iPad"; //调用父类方法 1 并添加字符串
    }
    void showPicture() { //重写父类方法 3
        System.out.println("手指点击触摸屏");
    }
    public static void main(String[] args) {
        Computer pc = new Computer(); //创建父类对象
        System.out.println("computer 的屏幕是：" + pc.screen); //父类对象调用父类属性
        pc.startup(); //父类对象调用父类方法 2
        System.out.println(pc.sayHello()); //父类对象调用父类方法 1
        System.out.println("pc 打开图片：");
        pc.showPicture(); //父类对象调用父类方法 3

        Pad iPad = new Pad(); //创建子类对象
        System.out.println("pad 的屏幕是：" + iPad.screen); //子类对象调用父类属性
        System.out.println("pad 的电池是：" + iPad.battery); //子类对象调用子类属性
        iPad.startup(); //子类对象调用父类方法 2
        System.out.println(iPad.sayHello()); //子类对象调用重写的父类方法 1
        System.out.println("pad 打开图片：");
        iPad.showPicture(); //子类对象调用重写的父类方法 3
    }
}
