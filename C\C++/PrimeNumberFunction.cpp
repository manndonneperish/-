#include <iostream>
#include <iomanip>
using namespace std;

//判断是否为素数
bool isPrime(int number)
{
	for (int divisor = 2; divisor <= sqrt(number); divisor++) //如果一个数n可以因数分解，则必有一个小于等于sqrt(n)，另一个大于等于sqrt(n)
	{
		if (number % divisor == 0)
		{
			return false; //不是素数
		}
	}
	return true; //是素数
}

//以每行十个打印出指定数量的素数表，从2开始
void printPrimeNumbers(int numberOfPrimes)
{
	const int NUMBER_OF_PRIMES_PER_LINE = 10;
	int count = 0;
	int number = 2;

	//检测是否为素数
	while (count < numberOfPrimes)
	{
		//打印素数
		if (isPrime(number))
		{
			count++;
			if (count % NUMBER_OF_PRIMES_PER_LINE == 0)
			{
				cout << setw(4) << number << endl; //setw(n)设置输出格式，当下一个输出字段长度小于n时在前面用空格补齐，大于n时全部输出
			}
			else
			{
				cout << setw(4) << number;
			}
		}

		//更新为下一个数
		number++;
	}
}

int main()
{
	//获取素数数量
	cout << "Input the number of prime numbers.\n";
	int n;
	cin >> n;

	//打印素数
	cout << "The first " << n << " prime numbers are \n";
	printPrimeNumbers(n);

	return 0;
}