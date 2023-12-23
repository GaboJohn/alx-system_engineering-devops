#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * run_infinite_loop - Execute an infinite while loop.
 *
 * Return: Always 0.
 */
int run_infinite_loop(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Create and manage five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t child_pid;
	int zombie_count = 0;

	while (zombie_count < 5)
	{
		child_pid = fork();

		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
			zombie_count++;
		}
		else
		{
			exit(0);
		}
	}

	run_infinite_loop();

	return (EXIT_SUCCESS);
}
