#include <stdio.h>  /* defines FILENAME_MAX */
#include <unistd.h>
#define GetCurrentDir getcwd
#include<iostream>
std::string GetCurrentWorkingDir( void ) {
  char buff[FILENAME_MAX];
  GetCurrentDir( buff, FILENAME_MAX );
  std::string current_working_dir(buff);
  return current_working_dir;
  }
int main(){
	std::string path=GetCurrentWorkingDir();
	std::string res;
	res=path+"/python-run.sh";
	const char * script = res.c_str();
	std::cout<<script<<std::endl;
	system(script);
	return 0;
        }
//////////////
//////
