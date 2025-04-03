cmake_minimum_required(VERSION 3.16)

project(cpu_scheduler_simulator VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Avoid warning about DOWNLOAD_EXTRACT_TIMESTAMP in CMake 3.24:
if (CMAKE_VERSION VERSION_GREATER_EQUAL "3.24.0")
    cmake_policy(SET CMP0135 NEW)
endif()

# Fetch Google Test
include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# Collect all core source files
file(GLOB_RECURSE CORE_SRC src/core/*.cpp)

# Define the core library to avoid recompiling it for each target
add_library(core STATIC ${CORE_SRC})
target_include_directories(core PUBLIC src/core)

# Console executable (main application)
#file(GLOB_RECURSE CONSOLE_SRC src/console/*.cpp)
#add_executable(console ${CONSOLE_SRC})
#target_include_directories(console PRIVATE src/console)
#target_link_libraries(console PRIVATE core)

# Enable testing
#include(CTest) # This is alternative to Google Test
include(GoogleTest)
enable_testing()

# Collect all test files
file(GLOB TEST_FILES test/*.cpp)

# Function to add a test executable and register it with CTest
function(add_simulator_test TEST_FILE)
    get_filename_component(TEST_NAME ${TEST_FILE} NAME_WE) # Extract filename without extension
    add_executable(${TEST_NAME} ${TEST_FILE})
    target_link_libraries(${TEST_NAME} PRIVATE core GTest::gtest_main)
#    add_test(NAME ${TEST_NAME} COMMAND ${TEST_NAME}) # This is alternative to Google Test
endfunction()

# Automatically add all test files
foreach(TEST_FILE ${TEST_FILES})
    add_simulator_test(${TEST_FILE})
endforeach()

if (${COMPILE_GUI})
    # Add QMake commands as per a new clean Qt project
endif()