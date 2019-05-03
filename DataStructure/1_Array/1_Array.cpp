//
// Created by hon on 2019-05-03.
//

#include <iostream>
# include <vector>
using namespace std;

int main() {
    vector<int> int_vector;
    for(int i=0; i<5; i++){
        int_vector.push_back(i);
    }
    for(int i=0; i < 5; i++){
        std::cout << int_vector[i];
    }
}