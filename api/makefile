#Testing VGTP Performance Evaluation API
CC = g++
AR = ar

APP_NAME=api_test

ifdef REL
CFLAGS= -O2 -s -DNDEBUG 
TARGET=run_$(APP_NAME)_release_version 
else
CFLAGS= -g -Wall -DDEBUG -O0 -gdwarf-2 -g3 
TARGET=run_$(APP_NAME)_debug_version
endif

PG_INC=-I /usr/local/include/hiredis
PG_LIB=-L /usr/local/lib

OBJS=$(APP_NAME)_main.o log_vgtp_pe.o

$(TARGET): $(OBJS) 
	$(CC) -o $(TARGET) $(OBJS) $(PG_LIB) -lm -lhiredis

$(OBJS):%.o:%.c
	$(CC) -c $(CFLAGS) $(PG_INC) $< -o $@


.PHONY:clean
clean:
	rm -frv $(READ_LIB) $(READ_OBJS) 
	find ./ -name "*.o" |xargs rm -R -v --force
	find ./ -name "*.orig" |xargs rm -R -v --force
	find ./ -name "*.bak" |xargs rm -R -v --force
#	rm -v --force $(TARGET) 
	rm -v --force *.bak
	rm -v --force *.orig
	rm -v --force log_error.txt
	rm -v --force *.log
	rm -v --force ./log/*.*
#	rm -v --force run_*
.PHONY:release
release:
	-find ./ -name "*" -print |egrep '\.cpp$$|\.c$$|\.h$$' |xargs rm -i; 
.PHONY:pp
pp:
	-find ./ -name "*" -print |egrep '\.cpp$$|\.c$$|\.h$$' |xargs astyle --style=linux -s -n;
	 
