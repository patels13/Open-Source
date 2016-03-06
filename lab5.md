
#PART I 
####mint@mint ~ $ cd build-lab

####mint@mint ~/build-lab $ cat > tutorial.cxx

// A simple program that computes the square root of a number

include <stdio.h>
include <stdlib.h>
include <math.h>
include "TutorialConfig.h"
int main (int argc, char *argv[])
{
  if (argc < 2)
    {
    fprintf(stdout,"%s Version %d.%d\n",
            argv[0],
            Tutorial_VERSION_MAJOR,
            Tutorial_VERSION_MINOR);
    fprintf(stdout,"Usage: %s number\n",argv[0]);
    return 1;

####mint@mint ~/build-lab $ cat > CMakeLists.txt

cmake_minimum_required (VERSION 2.6)
project (Tutorial)
The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)
 
 configure a header file to pass some of the CMake settings
 to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )
 
 add the binary tree to the search path for include files
 so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")
 
 add the executable
add_executable(Tutorial tutorial.cxx)

####mint@mint ~/build-lab $ cat > TutorialConfig.h.in

// the configured options and settings for Tutorial
define Tutorial_VERSION_MAJOR @Tutorial_VERSION_MAJOR@
define Tutorial_VERSION_MINOR @Tutorial_VERSION_MINOR@

####mint@mint ~/build-lab $ ls

CMakeLists.txt  TutorialConfig.h.in  tutorial.cxx

####mint@mint ~/build-lab $ mkdir step1

####mint@mint ~/build-lab $ cd step1

####mint@mint ~/build-lab/step1 $ cmake ..

-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/mint/build-lab/step1

####mint@mint ~/build-lab/step1 $ make

Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial

#Part2

####mint@mint ~ $ cd build-lab

####mint@mint ~/build-lab $ ls

CMakeLists.txt  step1  TutorialConfig.h.in  tutorial.cxx

####mint@mint ~/build-lab $ mkdir MathFunctions

####mint@mint ~/build-lab $ cd MathFunctions

####mint@mint ~/build-lab/MathFunctions $ cat > CMakeLists.txt

add_library(MathFunctions mysqrt.cxx)

####mint@mint ~/build-lab/MathFunctions $ cd ..

####mint@mint ~/build-lab $ ls

CMakeLists.txt  MathFunctions  step1  TutorialConfig.h.in  tutorial.cxx

####mint@mint ~/build-lab $ cat > CMakeLists.txt

cmake_minimum_required (VERSION 2.6)
project (Tutorial)
The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)
 
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )
include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
add_subdirectory (MathFunctions) 

add_executable (Tutorial tutorial.cxx)
target_link_libraries (Tutorial MathFunctions)

option (USE_MYMATH 
        "Use tutorial provided math implementation" ON) 
mint@mint ~/build-lab $ cat > CMakeLists.txt
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )

option (USE_MYMATH 
        "Use tutorial provided math implementation" ON) 


if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
  add_subdirectory (MathFunctions)
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)
 
add_executable (Tutorial tutorial.cxx)
target_link_libraries (Tutorial  ${EXTRA_LIBS})

####mint@mint ~/build-lab $ cat > tutorial.cxx

// A simple program that computes the square root of a number

 
int main (int argc, char *argv[])
{
  if (argc < 2)
    {
    fprintf(stdout,"%s Version %d.%d\n", argv[0],
            Tutorial_VERSION_MAJOR,
            Tutorial_VERSION_MINOR);
    fprintf(stdout,"Usage: %s number\n",argv[0]);
    return 1;
    }
 
  double inputValue = atof(argv[1]);
 
ifdef USE_MYMATH
  double outputValue = mysqrt(inputValue);
else
  double outputValue = sqrt(inputValue);
endif
 
  fprintf(stdout,"The square root of %g is %g\n",
          inputValue, outputValue);
  return 0;
}

####mint@mint ~/build-lab $ cat >> TutorialConfig.h.in

####mint@mint ~/build-lab $ cd MathFunctions

####mint@mint ~/build-lab/MathFunctions $ cat > mysqrt.cxx

double absolute(double a)
{
  if (a >= 0) return a;
  else return -a;
}
  
double mysqrt(double x)
{
  double guess;
  if (x < 0) 
    {
      //fprintf(stdout, " The number has to be nonnegative %g \n", 0);
      return 0;
    }
  if (x == 0)
    {
      //fprintf(stdout,"The square root of 0 is 0 \n");
      return 0;
    }
  guess = x/2.0;
  while ( absolute((guess*guess)/x - 1.0 ) >= 0.000001)
    guess  = ((x/guess)+guess)/2;
  return guess;
}

####mint@mint ~/build-lab/MathFunctions $ cd ..

####mint@mint ~/build-lab $ ls

CMakeLists.txt  MathFunctions  step1  step2  TutorialConfig.h.in  tutorial.cxx

####mint@mint ~/build-lab $ ls

CMakeLists.txt  MathFunctions  step1  TutorialConfig.h.in  tutorial.cxx

####mint@mint ~/build-lab $ mkdir step2

####mint@mint ~/build-lab $ cd step2

####mint@mint ~/build-lab/step2 $ cmake ..

-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/mint/build-lab/step2

#Part 3
####mint@mint ~/build-lab $ cat >> CMakeLists.txt

install (TARGETS Tutorial DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"        
         DESTINATION include)
####mint@mint ~/build-lab $ cat >> CMakeLists.txt
include(CTest)


add_test (TutorialRuns Tutorial 25)
 
add_test (TutorialComp25 Tutorial 25)
 
set_tests_properties (TutorialComp25 
  PROPERTIES PASS_REGULAR_EXPRESSION "25 is 5")
 

add_test (TutorialNegative Tutorial -25)
set_tests_properties (TutorialNegative
  PROPERTIES PASS_REGULAR_EXPRESSION "-25 is 0")

add_test (TutorialSmall Tutorial 0.0001)
set_tests_properties (TutorialSmall
  PROPERTIES PASS_REGULAR_EXPRESSION "0.0001 is 0.01")
 
add_test (TutorialUsage Tutorial)
set_tests_properties (TutorialUsage
  PROPERTIES 
  PASS_REGULAR_EXPRESSION "Usage:.*number")
####mint@mint ~/build-lab $ ls
CMakeLists.txt   step1             TutorialConfig.h.in  whatever2
MathFunctions    step2             tutorial.cxx         whatever3
MathFunctions.h  TutorialConfig.h  whatever             whatever4
####mint@mint ~/build-lab $ mkdir step3
####mint@mint ~/build-lab $ cd step3
####mint@mint ~/build-lab/step3 $ cmake ..
-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/mint/build-lab/step3
####mint@mint ~/build-lab/step3 $ make
Scanning dependencies of target MathFunctions
[ 50%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
####mint@mint ~/build-lab/step3 $ ctest
Test project /home/mint/build-lab/step3
    Start 1: TutorialRuns
1/5 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialComp25
2/5 Test #2: TutorialComp25 ...................   Passed    0.00 sec
    Start 3: TutorialNegative
3/5 Test #3: TutorialNegative .................   Passed    0.00 sec
    Start 4: TutorialSmall
4/5 Test #4: TutorialSmall ....................   Passed    0.00 sec
    Start 5: TutorialUsage
5/5 Test #5: TutorialUsage ....................   Passed    0.00 sec

100% tests passed, 0 tests failed out of 5

Total Test time (real) =   0.01 sec

![image](https://cloud.githubusercontent.com/assets/16493078/13551645/214c2386-e30f-11e5-82f6-a0177b0c63d3.png)

#Part 4
####mint@mint ~/build-lab $ cat >> CMakeLists.txt
does this system provide the log and exp functions?
include (CheckFunctionExists)
check_function_exists (log HAVE_LOG)
check_function_exists (exp HAVE_EXP)
####mint@mint ~/build-lab $ cat >> TutorialConfig.h.in
// does the platform provide exp and log functions?
cmakedefine HAVE_LOG
cmakedefine HAVE_EXP
####mint@mint ~/build-lab $ mkdir step4
####mint@mint ~/build-lab $ cd step4
####mint@mint ~/build-lab/test $ cmake ..
-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/mint/build-lab/test
####mint@mint ~/build-lab/test $ make
Scanning dependencies of target MathFunctions
[ 50%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial


#Part 5
####mint@mint ~/build-lab $ cd MathFunctions
####mint@mint ~/build-lab/MathFunctions $ cat > MakeTable.cxx
// A simple program that builds a sqrt table 

 
int main (int argc, char *argv[])
{
  int i;
  double result;
 
  // make sure we have enough arguments
  if (argc < 2)
    {
    return 1;
    }
  
  // open the output file
  FILE *fout = fopen(argv[1],"w");
  if (!fout)
    {
    return 1;
    }
  
  // create a source file with a table of square roots
  fprintf(fout,"double sqrtTable[] = {\n");
  for (i = 0; i < 10; ++i)
    {
    result = sqrt(static_cast<double>(i));
    fprintf(fout,"%g,\n",result);
    }
 
  // close the table with a zero
  fprintf(fout,"0};\n");
  fclose(fout);
  return 0;
}
####mint@mint ~/build-lab/MathFunctions $ cd ..
####mint@mint ~/build-lab $ ls
CMakeLists.txt   step1  step4                tutorial.cxx  whatever3
MathFunctions    step2  TutorialConfig.h     whatever      whatever4
MathFunctions.h  step3  TutorialConfig.h.in  whatever2
####mint@mint ~/build-lab $ cat > CMakeLists.txt
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
include(CTest)
 
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

include (${CMAKE_ROOT}/Modules/CheckFunctionExists.cmake)
 
check_function_exists (log HAVE_LOG)
check_function_exists (exp HAVE_EXP)
 

option(USE_MYMATH 
  "Use tutorial provided math implementation" ON)
 

configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )

include_directories ("${PROJECT_BINARY_DIR}")
 
if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
  add_subdirectory (MathFunctions)
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)
 

add_executable (Tutorial tutorial.cxx)
target_link_libraries (Tutorial  ${EXTRA_LIBS})

install (TARGETS Tutorial DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"        
         DESTINATION include)
 

add_test (TutorialRuns Tutorial 25)
 

add_test (TutorialUsage Tutorial)
set_tests_properties (TutorialUsage
  PROPERTIES 
  PASS_REGULAR_EXPRESSION "Usage:.*number"
  )
 

macro (do_test arg result)
  add_test (TutorialComp${arg} Tutorial ${arg})
  set_tests_properties (TutorialComp${arg}
    PROPERTIES PASS_REGULAR_EXPRESSION ${result}
    )
endmacro (do_test)
 

do_test (4 "4 is 2")
do_test (9 "9 is 3")
do_test (5 "5 is 2.236")
do_test (7 "7 is 2.645")
do_test (25 "25 is 5")
do_test (-25 "-25 is 0")
do_test (0.0001 "0.0001 is 0.01")
####mint@mint ~/build-lab $ cat > TutorialConfig.h.in
// the configured options and settings for Tutorial
define Tutorial_VERSION_MAJOR @Tutorial_VERSION_MAJOR@
define Tutorial_VERSION_MINOR @Tutorial_VERSION_MINOR@
cmakedefine USE_MYMATH
 
// does the platform provide exp and log functions?
cmakedefine HAVE_LOG
cmakedefine HAVE_EXP
####mint@mint ~/build-lab $ cd MathFunctions
####mint@mint ~/build-lab/MathFunctions $ ls
CMakeLists.txt  MakeTable.cxx  mysqrt.cxx
####mint@mint ~/build-lab/MathFunctions $ cat > CMakeLists.txt
 first we add the executable that generates the table
add_executable(MakeTable MakeTable.cxx)
 add the command to generate the source code
add_custom_command (
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Table.h
  DEPENDS MakeTable
  COMMAND MakeTable ${CMAKE_CURRENT_BINARY_DIR}/Table.h
  )
 add the binary tree directory to the search path 
 for include files
include_directories( ${CMAKE_CURRENT_BINARY_DIR} )
 
 add the main library
add_library(MathFunctions mysqrt.cxx ${CMAKE_CURRENT_BINARY_DIR}/Table.h)
 
install (TARGETS MathFunctions DESTINATION bin)
install (FILES MathFunctions.h DESTINATION include)
####mint@mint ~/build-lab/MathFunctions $ cd ..
####mint@mint ~/build-lab $ ls
CMakeLists.txt   step1  step4             TutorialConfig.h.in  whatever2
MathFunctions    step2  test              tutorial.cxx         whatever3
MathFunctions.h  step3  TutorialConfig.h  whatever             whatever4
####mint@mint ~/build-lab $ mkdir step5
####mint@mint ~/build-lab $ cd step5
####mint@mint ~/build-lab/step5 $ cmake ..
-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/mint/build-lab/step5
####mint@mint ~/build-lab/step5 $ make
Scanning dependencies of target MakeTable
[ 25%] Building CXX object MathFunctions/CMakeFiles/MakeTable.dir/MakeTable.cxx.o
Linking CXX executable MakeTable
[ 25%] Built target MakeTable
[ 50%] Generating Table.h
Scanning dependencies of target MathFunctions
[ 75%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
Linking CXX static library libMathFunctions.a
[ 75%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
####mint@mint ~/build-lab/step5 $ ctest
Test project /home/mint/build-lab/step5
    Start 1: TutorialRuns
1/9 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialUsage
2/9 Test #2: TutorialUsage ....................   Passed    0.00 sec
    Start 3: TutorialComp4
3/9 Test #3: TutorialComp4 ....................   Passed    0.00 sec
    Start 4: TutorialComp9
4/9 Test #4: TutorialComp9 ....................   Passed    0.00 sec
    Start 5: TutorialComp5
5/9 Test #5: TutorialComp5 ....................   Passed    0.00 sec
    Start 6: TutorialComp7
6/9 Test #6: TutorialComp7 ....................   Passed    0.00 sec
    Start 7: TutorialComp25
7/9 Test #7: TutorialComp25 ...................   Passed    0.00 sec
    Start 8: TutorialComp-25
8/9 Test #8: TutorialComp-25 ..................   Passed    0.00 sec
    Start 9: TutorialComp0.0001
9/9 Test #9: TutorialComp0.0001 ...............   Passed    0.00 sec

100% tests passed, 0 tests failed out of 9

Total Test time (real) =   0.02 sec

