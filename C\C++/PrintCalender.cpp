#include <iostream>
#include <iomanip>
using namespace std;

//声明所有用到的函数
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
	//用户输入年份和月份，本程序仅可打印1800年1月以后的日历
	cout << "Enter full year after 1800 (e.g. 2001): ";
	int year;
	cin >> year;
	cout << "Enter month in number between 1 and 12: ";
	int month;
	cin >> month;

	//打印该年该月的日历
	printMonth(year, month);

	return 0;
}

//打印日历函数
void printMonth(int year, int month)
{
	//打印日历头
	printMonthTitle(year, month);

	//打印日历体
	printMonthBody(year, month);
}

//打印日历头函数，e.g. May 1999
void printMonthTitle(int year, int month)
{
	printMonthName(month);
	cout << " " << year << endl;
	cout << "-----------------------------" << endl;
	cout << " Sun Mon Tue Wed Thu Fri Sat" << endl;
}

//获得月份的英文名
void printMonthName(int month)
{
	string months[] = { "January","February","March","April","May","June","July","August","September","October","November","December" };
	cout << months[month - 1];
}

//打印日历体函数
void printMonthBody(int year, int month)
{
	//获得本月第一天的星期
	int startDay = getStartday(year, month);

	//获得本月天数
	int numberOfDaysInMonth = getNumberOfDaysInMonth(year, month);

	//在本月第一天之前的位置填充空格
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

//获得该月的第一天的星期
int getStartday(int year, int month)
{
	//获得从1800年1月1日到输入月份第一天的总天数
	int startDay1800 = 3;
	int totalNumberOfDays = getTotalNumberOfDays(year, month);

	//返回第一天的数值
	return (totalNumberOfDays + startDay1800) % 7;
}

//获得从1800年1月1日到输入月份第一天的总天数
int getTotalNumberOfDays(int year, int month)
{
	int total = 0;

	//获得从1800到year-1的总天数
	for (int i = 1800; i < year; i++)
		if (isLeapYear(i))
			total = total + 366;
		else
			total = total + 365;

	//加上从一月到该月之前的天数
	for (int i = 1; i < month; i++)
		total = total + getNumberOfDaysInMonth(year, i);

	return total;
}

//获得每个月的天数
int getNumberOfDaysInMonth(int year, int month)
{
	if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12)
		return 31;
	
	if (month == 4 || month == 6 || month == 9 || month == 11)
		return 30;

	if (month == 2) return isLeapYear(year) ? 29 : 28;

	return 0; //如果月份不合理
}

//判断闰年
bool isLeapYear(int year)
{
	return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
}