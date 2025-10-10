#include <iostream>
#include <string.h>
using namespace std;

int main(int argc, char* argv[]) {
    int nextArgType = 0;
    std::string fileToOpen;
    std::string fileToOutput;
    std::string stringToAdd;
    for (int i = 1;i<argc;i++) {
        if (nextArgType == 0) {
            if (strcmp(argv[i],"-i") == 0) {
                nextArgType = 1;
            }
            if (strcmp(argv[i],"--input") == 0) {
                nextArgType = 1;
            }
            if (strcmp(argv[i],"-a") == 0) {
                nextArgType = 2;
            }
            if (strcmp(argv[i],"-o") == 0) {
                nextArgType = 3;
            }
        } else if (nextArgType == 1) {
            fileToOpen = argv[i];
            nextArgType = 0;
        } else if (nextArgType == 2) {
            stringToAdd = argv[i];
            nextArgType = 0;
        } else if (nextArgType == 3) {
            fileToOutput = argv[i];
            nextArgType = 0;
        }
    }
    cout << fileToOpen << endl;
    cout << nextArgType << endl;
    cout << stringToAdd << endl;
    cout << fileToOutput << endl;
    return 0;
}