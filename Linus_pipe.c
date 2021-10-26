#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
int main() 
{ 
 int pid; 
 int fd[2]; 
 pipe(fd); 
 pid = fork(); 
 if (pid < 0) 
 { 
 perror("fork"); 
 exit(-1); 
 } 
 if (pid == 0) 
 { 
 close(1); 
 dup(fd[1]); 
 close(fd[0]); 
 close(fd[1]); 
 execl("/bin/ls", "ls", "-l", (char *)0); 
 } 
 else 
 { 
 close(0); 
 dup(fd[0]); 
 close(fd[0]); 
 close(fd[1]); 
 execl("/usr/bin/grep", "grep", ".c$", (char *)0); 
 } 
