#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop
 * @void: no argument
 *
 * Description: This function creates an infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 processes
 * @void: no argument
 *
 * Description: This function creates processes for the zombie
 * Return: 0
 */
int main(void)
{
	pid_t zombie;
	int i = 0;

	while (i < 5)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		i++;
		printf("Zombie process created, PID: %d\n", zombie);
	}

	infinite_while();
	return (0);
}

