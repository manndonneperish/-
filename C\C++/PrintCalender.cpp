#include <iostream>
#include <iomanip>
using namespace std;

//���������õ��ĺ���
void printMonth(int year, int month);
void printMonthTitle(int year, int month);
void printMonthName(int month);
void printMonthBody(int year, int month);
int getStartday(int year, int month);
int getTotalNumberOfDays(int year, int month);
int getNumberOfDaysInMonth(int year, int month);
bool isLeapYear(int year);

int main()
{
	//�û�������ݺ��·ݣ���������ɴ�ӡ1800��1���Ժ������
	cout << "Enter full year after 1800 (e.g. 2001): ";
	int year;
	cin >> year;
	cout << "Enter month in number between 1 and 12: ";
	int month;
	cin >> month;

	//��ӡ������µ�����
	printMonth(year, month);

	return 0;
}

//��ӡ��������
void printMonth(int year, int month)
{
	//��ӡ����ͷ
	printMonthTitle(year, month);

	//��ӡ������
	printMonthBody(year, month);
}

//��ӡ����ͷ������e.g. May 1999
void printMonthTitle(int year, int month)
{
	printMonthName(month);
	cout << " " << year << endl;
	cout << "-----------------------------" << endl;
	cout << " Sun Mon Tue Wed Thu Fri Sat" << endl;
}

//����·ݵ�Ӣ����
void printMonthName(int month)
{
	string months[] = { "January","February","March","April","May","June","July","August","September","October","November","December" };
	cout << months[month - 1];
}

//��ӡ�����庯��
void printMonthBody(int year, int month)
{
	//��ñ��µ�һ�������
	int startDay = getStartday(year, month);

	//��ñ�������
	int numberOfDaysInMonth = getNumberOfDaysInMonth(year, month);

	//�ڱ��µ�һ��֮ǰ��λ�����ո�
	int i = 0;
	for (i = 0; i <= startDay; i++)
		cout << "   ";

	for (i = 1; i <= numberOfDaysInMonth; i++)
	{
		cout << setw(4) << i;
		
		if ((i + startDay) % 7 == 0)
			cout << endl;
	}
}

//��ø��µĵ�һ�������
int getStartday(int year, int month)
{
	//��ô�1800��1��1�յ������·ݵ�һ���������
	int startDay1800 = 3;
	int totalNumberOfDays = getTotalNumberOfDays(year, month);

	//���ص�һ�����ֵ
	return (totalNumberOfDays + startDay1800) % 7;
}

//��ô�1800��1��1�յ������·ݵ�һ���������
int getTotalNumberOfDays(int year, int month)
{
	int total = 0;

	//��ô�1800��year-1��������
	for (int i = 1800; i < year; i++)
		if (isLeapYear(i))
			total = total + 366;
		else
			total = total + 365;

	//���ϴ�һ�µ�����֮ǰ������
	for (int i = 1; i < month; i++)
		total = total + getNumberOfDaysInMonth(year, i);

	return total;
}

//���ÿ���µ�����
int getNumberOfDaysInMonth(int year, int month)
{
	if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12)
		return 31;
	
	if (month == 4 || month == 6 || month == 9 || month == 11)
		return 30;

	if (month == 2) return isLeapYear(year) ? 29 : 28;

	return 0; //����·ݲ�����
}

//�ж�����
bool isLeapYear(int year)
{
	return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
}