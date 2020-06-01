#pragma config(StandardModel, "RVW Buggybot")
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

/****************************************************
Name: Iniyan Joseph
Period: 3
Date: 5/11/2020
Assignment: Palm Islands
Program Description: Robot picks up trash bins, coconuts, and pushes lobster pots
Algorithm:
1.
*******************************************************/
//Variables---------------------------------------------
int speed = 50;
//Functions---------------------------------------------
void sec1();
void sec2();
void sec3p1();
void sec3p2();
void sec4p1();
void sec4p2();
void sec5();
void sec6();
void sec7();
void sec8();

task main()
{
	sec8();
}
//------------------------------------------------------

void sec1()
{
	forward(4, rotations, speed);
}

void sec2()
{
	forward(4.6, rotations, speed);
	turnRight(138, degrees, speed);
	forward(11, rotations, speed);
}

void sec3p1()
{
	forward(2.5, rotations, speed);
	turnRight(138, degrees, speed);
	forward(2, rotations, speed);
}

void sec3p2()
{
	forward(2.5, rotations, speed);
	turnLeft(138, degrees, speed);
	forward(5.5, rotations, speed);
}

void sec4p1()
{
	forward(2, rotations, speed);
	turnRight(138, degrees, speed);
	forward(3, rotations, speed);
	turnRight(65, degrees, speed);
	forward(6.5, rotations, speed);
}

void sec4p2()
{
	forward(2, rotations, speed);
	turnRight(138, degrees, speed);
	forward(2.58, rotations, speed);
	turnLeft(65, degrees, speed);
	forward(7.8, rotations, speed);
}
void sec5()
{
	forward(1, rotations, speed);
	turnRight(80, degrees, speed);
	forward(4.8, rotations, speed);
}
void sec6()
{
	setMultipleMotors(speed, leftMotor, rightMotor);
	waitUntil(SensorValue[touchSensor] == 1);
	stopAllMotors();
	backward(0.2, rotations, speed);
	turnLeft(138, degrees, speed);
	setMultipleMotors(speed, leftMotor, rightMotor);
	waitUntil(SensorValue[sonarSensor] < 45);
	turnRight(138, degrees, speed);
	backward(0.8, rotations, speed);
}
void sec7()
{
	forward(3, rotations, speed);
	turnRight(110, degrees, speed);
	forward(4.5, rotations, speed);
}

void sec8()
{
	while(true)
	{
		while(SensorValue[lightSensor] < 2000)//As long as we see white
		{
			forward(0.1, degrees, speed);//Go Straight
			motor[leftMotor] = -speed;//Stop Left Motor Backwards
			motor[rightMotor] = speed;//Turn Right Motor Forward
		}
		while(SensorValue[lightSensor] > 2000)//As long as we see black
		{
			forward(0.1, degrees, speed);
			motor[leftMotor] = speed;//Turn Left Motor Forward
			motor[rightMotor] = -speed;//Turn Right Motor Backwards
		}
	}
}
