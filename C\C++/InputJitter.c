#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 模拟获取键盘输入的函数
char getKeyboardInput() {
    // 模拟随机生成键盘输入
    char inputs[] = {'A', 'B', 'C', 'D', 'E'};
    int index = rand() % 5;
    return inputs[index];
}

// 检测键盘输入是否抖动
int isInputJitter(char input) {
    // 模拟抖动检测条件
    if (input == 'A' || input == 'B') {
        return 1;
    }
    return 0;
}

int main() {
    srand(time(NULL));  // 初始化随机数生成器

    char previousInput = '\0';  // 保存上一次有效的键盘输入

    while (1) {
        char input = getKeyboardInput();

        // 检测键盘输入是否抖动
        if (!isInputJitter(input)) {
            previousInput = input;
        }

        // 使用有效的键盘输入进行处理
        if (previousInput != '\0') {
            printf("有效输入：%c\n", previousInput);
            // 在这里执行你的逻辑处理
        }
    }

    return 0;
}
