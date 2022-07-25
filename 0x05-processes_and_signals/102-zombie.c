#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
*infinite_while - infinite while loop
*Return: 0 always
*/
int infinite_while(void)
{
while (1)
{
;  
}
return (0);
}
/**
* main - Creates 5 zombie processes
* Return: 0
*/
int main(void)
{
int n;
pid_t pid;
for (n = 0; n < 5; n++)
{
pid = fork();
if (pid > 0)
{
printf("Zombie process created, PID: %d\n", pid);
}
else
{
return (0);
}
}
infinite_while();
return (0);
}
