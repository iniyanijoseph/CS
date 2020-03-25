#pragma config(StandardModel, "RVW Mammalbot")
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//
/****************************************************
Name: Iniyan Joseph
Period: 3
Date: 3/16/2020
Assignment: Robo Slalom 1 Sensor
Program Description: Follow a line
Algorithm:
1.If Robot Sees White, Turn to the left
2.It Robot Sees Dark Turn to the right
*******************************************************/
//Variables---------------------------------------------
int speed = 70;//Set the speed of the motors
//Functions---------------------------------------------
void checklight();//Declare Function to check if there is light of dark
void straight();//Declare Function to go straight

task main()
{
	while(true)//As long as we run
	{
	checklight();//Check for each light
	}
}
//Function Glossary-------------------------------------

void checklight()
{
	while(SensorValue[lightSensor] < 2000)//As long as we see white
	{
		straight();//Go Straight
		motor[leftMotor] = -speed;//Stop Left Motor Backwards
		motor[rightMotor] = speed;//Turn Right Motor Forward
	}
	while(SensorValue[lightSensor] > 2000)//As long as we see black
	{
		straight();//Go Straight
		motor[leftMotor] = speed;//Turn Left Motor Forward
		motor[rightMotor] = -speed;//Turn Right Motor Backwards
	}
}

void straight()//Function to go straight
{
	motor[leftMotor] = speed;//Turn Left Motor
	motor[rightMotor] = speed;//Turn Right Motor
}