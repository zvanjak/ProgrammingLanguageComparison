// Zad 01 - Reading log.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using std::ifstream;
using std::cout;
using std::string;
using std::vector;
using std::map;

enum MessageType
{
	WARNING,
	INFO,
	DEBUG,
	ERROR
};

string getMessageType(MessageType type)
{
	if (type == MessageType::DEBUG) return "DEBUG";
	else if (type == MessageType::WARNING) return "WARNING";
	else if (type == MessageType::INFO) return "INFO";
	else if (type == MessageType::ERROR) return "ERROR";
	else return "UNKNOWN";
}

class LogLine
{
public:
	LogLine(string date, string time, string file, string line, string type, string message): _date(date), _time(time), _file(file), _line(line), _message(message)
	{
		if (type == "WARNING") _type = MessageType::WARNING;
		else if (type == "DEBUG") _type = MessageType::DEBUG;
		else if (type == "INFO") _type = MessageType::INFO;
		else if (type == "ERROR") _type = MessageType::ERROR;
	}

public:
	string _time;
	string _date;
	string _file;
	string _line;
	MessageType _type;
	string _message;
};

void countAndPrintTypeStat(vector<LogLine>& lines)
{
	map<MessageType, int> countTypes;

	for (auto it = lines.begin(); it != lines.end(); it++)
	{
		MessageType t = it->_type;
		if (countTypes.find(t) != countTypes.end())
			countTypes[t] += 1;
		else
			countTypes[t] = 1;
	}

	for (auto it2 = countTypes.begin(); it2 != countTypes.end(); it2++)
		cout << getMessageType(it2->first) << " - " << it2->second << std::endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream file("Log.txt");
	vector<LogLine> lines;

	if (file.is_open())
	{
		string strDate, strTime, strFile, strLine, strType, strMessage;
		while (std::getline(file, strDate, ' '))
		{
			std::getline(file, strTime, ' ');
			std::getline(file, strFile, ' ');
			std::getline(file, strLine, ' ');
			std::getline(file, strType, ' ');
			std::getline(file, strMessage);

			LogLine read(strDate, strTime, strFile, strLine, strType, strMessage);

			lines.push_back(read);
		}

		countAndPrintTypeStat(lines);
	}
	else
		cout << "Error opening file";
	return 0;
}
