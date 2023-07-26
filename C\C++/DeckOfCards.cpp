/*
该程序用于随机从一副纸牌的52张中选择4张
所有的纸牌用0~51共52个数字表示
0~12为13张黑桃，13~25为红桃，26~38为方片，39~51为梅花
每张牌对应的数字cardNumber/13决定了花色，cardNumber%13决定了纸牌的牌面
将数组内容重新随机排序后取前四张
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

	//设定牌号
	for (int i = 0; i < NUMBER_OF_CARDS; i++)
		deck[i] = i;

	//取牌
	srand(time(0));
	for (int i = 0; i < NUMBER_OF_CARDS; i++)
	{
		//随机洗牌
		int index = rand() % NUMBER_OF_CARDS;
		int temp = deck[i];
		deck[i] = deck[index];
		deck[index] = temp;
	}

	//将前四个数变为对应的牌输出
	for (int i = 0; i < 4; i++)
	{
		string suit = suits[deck[i] / 13];
		string rank = ranks[deck[i] % 13];
		cout << "Crad number " << deck[i] << ": " << rank << " of " << suit << endl;
	}

	return 0;
}