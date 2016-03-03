mint@mint ~ $ ls
build_lab  Documents  Music     Public     tutorial
Desktop    Downloads  Pictures  Templates  Videos
mint@mint ~ $ cd build_lab
mint@mint ~/build_lab $ ls
#PART I


CMakeLists.txt  step1  TutorialConfig.h.in  tutorial.cxx
mint@mint ~/build_lab $ rmdir step1
rmdir: failed to remove ‘step1’: Directory not empty
mint@mint ~/build_lab $ mkdir step_1
mint@mint ~/build_lab $ cd step_1
mint@mint ~/build_lab/step_1 $ cmake ..
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
-- Build files have been written to: /home/mint/build_lab/step_1
mint@mint ~/build_lab/step_1 $ make
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
mint@mint ~/build_lab/step_1 $ cd ..
mint@mint ~/build_lab $ ls
CMakeLists.txt  step1  step_1  TutorialConfig.h.in  tutorial.cxx


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
