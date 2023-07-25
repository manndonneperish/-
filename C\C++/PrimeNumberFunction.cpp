#include <iostream>
#include <iomanip>
using namespace std;

//�ж��Ƿ�Ϊ����
bool isPrime(int number)
{
	for (int divisor = 2; divisor <= sqrt(number); divisor++) //���һ����n���������ֽ⣬�����һ��С�ڵ���sqrt(n)����һ�����ڵ���sqrt(n)
	{
		if (number % divisor == 0)
		{
			return false; //��������
		}
	}
	return true; //������
}

//��ÿ��ʮ����ӡ��ָ����������������2��ʼ
void printPrimeNumbers(int numberOfPrimes)
{
	const int NUMBER_OF_PRIMES_PER_LINE = 10;
	int count = 0;
	int number = 2;

	//����Ƿ�Ϊ����
	while (count < numberOfPrimes)
	{
		//��ӡ����
		if (isPrime(number))
		{
			count++;
			if (count % NUMBER_OF_PRIMES_PER_LINE == 0)
			{
				cout << setw(4) << number << endl; //setw(n)���������ʽ������һ������ֶγ���С��nʱ��ǰ���ÿո��룬����nʱȫ�����
			}
			else
			{
				cout << setw(4) << number;
			}
		}

		//����Ϊ��һ����
		number++;
	}
}

int main()
{
	//��ȡ��������
	cout << "Input the number of prime numbers.\n";
	int n;
	cin >> n;

	//��ӡ����
	cout << "The first " << n << " prime numbers are \n";
	printPrimeNumbers(n);

	return 0;
}