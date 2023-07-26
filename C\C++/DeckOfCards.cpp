/*
�ó������������һ��ֽ�Ƶ�52����ѡ��4��
���е�ֽ����0~51��52�����ֱ�ʾ
0~12Ϊ13�ź��ң�13~25Ϊ���ң�26~38Ϊ��Ƭ��39~51Ϊ÷��
ÿ���ƶ�Ӧ������cardNumber/13�����˻�ɫ��cardNumber%13������ֽ�Ƶ�����
����������������������ȡǰ����
*/

#include <iostream>
#include <ctime>
#include <string>
using namespace std;

int main()
{
	const int NUMBER_OF_CARDS = 52;
	int deck[NUMBER_OF_CARDS];
	string suits[] = { "Spads","Hearts","Diamons","Clubs" };
	string ranks[] = { "Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King" };

	//�趨�ƺ�
	for (int i = 0; i < NUMBER_OF_CARDS; i++)
		deck[i] = i;

	//ȡ��
	srand(time(0));
	for (int i = 0; i < NUMBER_OF_CARDS; i++)
	{
		//���ϴ��
		int index = rand() % NUMBER_OF_CARDS;
		int temp = deck[i];
		deck[i] = deck[index];
		deck[index] = temp;
	}

	//��ǰ�ĸ�����Ϊ��Ӧ�������
	for (int i = 0; i < 4; i++)
	{
		string suit = suits[deck[i] / 13];
		string rank = ranks[deck[i] % 13];
		cout << "Crad number " << deck[i] << ": " << rank << " of " << suit << endl;
	}

	return 0;
}