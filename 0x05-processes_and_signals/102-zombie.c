#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop to keep the program running
 *
 * Return: Always 0.
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
 * main - Creates 5 zombie processes
 *
 * Return: Always 0.
 */
int main(void)
{
    pid_t zombie_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        zombie_pid = fork(); /* Create a child process */

        if (zombie_pid == -1)
        {
            perror("fork");
            exit(EXIT_FAILURE);
        }

        if (zombie_pid > 0)
        {
            /* Parent process: display Zombie process created, PID: ZOMBIE_PID */
            printf("Zombie process created, PID: %d\n", zombie_pid);
            sleep(1); /* Give some time for the parent to display the message */
        }
        else
        {
            /* Child process: exit immediately to become a zombie */
            exit(EXIT_SUCCESS);
        }
    }

    /* Parent process: infinite loop to keep the program running */
    return infinite_while();
}

