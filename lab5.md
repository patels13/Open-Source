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
