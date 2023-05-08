#include <iostream>
#include <chrono>
#include <thread>

using namespace std;

int main() {
  int focusMinutes = 25; // 专注时间，单位为分钟
  cout << "开始专注 " << focusMinutes << " 分钟..." << endl;
  
  auto start = chrono::steady_clock::now(); // 记录当前时间
  
  this_thread::sleep_for(chrono::minutes(focusMinutes)); // 等待专注时间
  
  auto end = chrono::steady_clock::now(); // 记录结束时间
  
  cout << "恭喜！您已经专注了 " << focusMinutes << " 分钟。" << endl;
  
  auto duration = chrono::duration_cast<chrono::seconds>(end - start).count(); // 计算专注时间
  
  cout << "共计用时 " << duration / 60 << " 分钟 " << duration % 60 << " 秒。" << endl;
  
  return 0;
}
