SOURCE_FILE=add.cpp
# main.cpp include `add.h` whose implementation is `add.cpp`
MAIN_FILE=main.cpp
SONAME=libadd.so.1
REAL_NAME=libadd.so.1.1
LINKER_NAME=libadd.so
OUTPUT_FILE=a.out

all:
	g++ -shared -fPIC -Wl,-soname,${SONAME} -o ${REAL_NAME} ${SOURCE_FILE}
	ln -s ${REAL_NAME} ${LINKER_NAME}
	g++ main.cpp -I. -L. -ladd -o ${OUTPUT_FILE}	
	# same with `ldconfig -n .` create a soft symbolic link
	ln -s ${REAL_NAME} ${SONAME}
	#./a.out: error while loading shared libraries: libadd.so.1: cannot open shared object file: No such file or directory
	LD_LIBRARY_PATH=. ./${OUTPUT_FILE}
clean:
	rm ${SONAME} ${REAL_NAME} ${LINKER_NAME} ${OUTPUT_FILE}
