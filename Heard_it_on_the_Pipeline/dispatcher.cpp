#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <iostream>

int main(){
	
	int fpipe[2];
	char** b = {NULL};
	int generator;
	int consumer;
	if(pipe(fpipe)){
		return EXIT_FAILURE;
	}
	if(!(generator == fork())){
		dup2(fpipe[1], STDOUT_FILENO);
		close(fpipe[0]);
		execve("./generator", b, NULL);
		exit(0);	
	}
	sleep(1);
	if(!kill(generator, SIGTERM)){
		waitpid(generator, NULL, 0);	
	}
	
	if(!(consumer == fork())){
		dup2(fpipe[0], STDOUT_FILENO);
		close(fpipe[1]);
		execve("./consumer", b, NULL);
		exit(0);	
	}

	return EXIT_SUCCESS;
}
