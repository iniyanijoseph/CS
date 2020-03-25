#pragma config(StandardModel, "RVW SWERVEBOT")
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

/****************************************************
Name: Iniyan
Period: 3
Date: 2/5/2020
Assignment:
Program Description: (Travel in a Square)
Algorithm:
1.Move Forward 8 Spaces
2.Right Turn 90 Degrees
3.Repeat Steps 1 & 2 3 More Times
*******************************************************/
//Variables---------------------------------------------
int speed = 70;//Set the speed of the motors
//Functions---------------------------------------------
void straight();//Declare the function to go straight
void turnright();//Declare the function to turn right
void clear();//Declare the function to clear the encoder values

task main() //Main
{
	for(int count=0; count<8; count++) // Set a for loop to count to 8
	{
		straight();//Go Straight
		turnright();//Turn Right
	}	//0, 1, 2, 3, 4, 5, 6, 7 stops at 8
}
//------------------------------------------------------
void straight()//Define function to go straight
{
	while(SensorValue[rightEncoder] < 1400)
	//True as long as the right encoder is less than 1400
	{
		motor[leftMotor] = speed;//Turn the leftmotor on to the vlaue of speed
		motor[rightMotor] = speed;//Turn the rightmotor ont to the value of speed
	}
	clear();//Clear the encoders to use again
}

void turnright()//Define the function to turn right
{
	while(SensorValue[leftEncoder] < 378)
	//True as long as the left encoder is less than 375
	{
		motor[leftMotor] = speed;//Turn the leftmotor on to the value of speed
		motor[rightMotor] = 0;//Make sure the rightMotor is 0
	}
	clear();//Clear the encoders to use again
}

void clear()
{
	SensorValue[rightEncoder] = 0;//Clear the rightencoder value
	SensorValue[leftEncoder] = 0;//Clear the leftencoder value
}