
#PART I \n
mint@mint ~ $ mkdir build-lab \n
mint@mint ~ $ cd build-lab
mint@mint ~/build-lab $ cat > tutorial.cxx
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
    }
  double inputValue = atof(argv[1]);
  double outputValue = sqrt(inputValue);
  fprintf(stdout,"The square root of %g is %g\n",
          inputValue, outputValue);
  return 0;
}
mint@mint ~/build-lab $ cat > CMakeLists.txt
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
mint@mint ~/build-lab $ cat > TutorialConfig.h.in
// the configured options and settings for Tutorial
define Tutorial_VERSION_MAJOR @Tutorial_VERSION_MAJOR@
define Tutorial_VERSION_MINOR @Tutorial_VERSION_MINOR@
mint@mint ~/build-lab $ ls
CMakeLists.txt  TutorialConfig.h.in  tutorial.cxx
mint@mint ~/build-lab $ mkdir step1
mint@mint ~/build-lab $ cd step1
mint@mint ~/build-lab/step1 $ cmake ..
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
mint@mint ~/build-lab/step1 $ make
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial



#Part5
mint@mint ~/build_lab/step_4_5 $ cd ..
mint@mint ~/build_lab $ ls
CMakeLists.txt   step1   step_3    step_infinity
MathFunctions    step_1  step_4_5  TutorialConfig.h.in
MathFunctions.h  step_2  step4_5   tutorial.cxx
mint@mint ~/build_lab $ mkdir step--4--5
mint@mint ~/build_lab $ cd step--4--5
mint@mint ~/build_lab/step--4--5 $ cmake ..
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
-- Build files have been written to: /home/mint/build_lab/step--4--5
mint@mint ~/build_lab/step--4--5 $ make
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
mint@mint ~/build_lab/step--4--5 $ ctest
Test project /home/mint/build_lab/step--4--5
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
