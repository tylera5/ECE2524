//Tyler Adams
#include "Process.h"
#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <iostream>
#include <string.h>
#include <algorithm>

Process::Process(const std::vector<std::string> &args){/* Initialize the process, create input/output pipes */
   	pipe(readpipe);
   	pipe(writepipe);
   	m_pread = fdopen(readpipe[0], "r");\

	std::vector<const char *> cargs;
	std::transform(args.begin(), args.end(), std::back_inserter(cargs), []( const std::string s) { return s.c_str(); /*what would you return here?*/ } );
	cargs.push_back(NULL); // exec expects a NULL terminated array

	m_pid = fork();
	m_name = cargs[0];

	if(m_pid == 0){//child
		dup2(writepipe[0], 0);
		close(writepipe[1]);

		dup2(readpipe[1], 1);
		close(readpipe[0]);

		execve(m_name.c_str(), const_cast<char**>(&cargs[0]), NULL);
		exit(0);
	}

	else{//parent
		m_pread = fdopen(readpipe[0], "r");
		close(writepipe[0]);
		close(readpipe[1]);
		std::cout << "Parent[" <<  getpid() << "] Process constructor" << std::endl;
	}
}

Process::~Process(){ /* Close any open file streams or file descriptors, insure that the child has terminated */
	int stat;
	close(readpipe[1]);
    	close(writepipe[0]);
	fclose(m_pread);
        kill(m_pid, SIGTERM);
        waitpid(m_pid, &stat, 0);
}

void Process::write(const std::string& val){/* write a string to the child process */
	::write(writepipe[1], val.c_str(), strlen(val.c_str()));
}

std::string Process::readline(){ /* read a full line from child process, if no line is available, block until one becomes available */
	char* l = NULL;
    	size_t len = 0;
    	getline(&l, &len, m_pread);
    	return l;
}
