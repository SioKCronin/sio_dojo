#include <iostream>
#include "linked_list.cpp"

using namespace std;

int main(){
  list obj;
  obj.create(10);
  obj.create(20);
  obj.create(30);
  obj.create(40);
  obj.create(50);
  obj.create(60);
  obj.create(70);
  obj.create(80);
  obj.point_values(80, 10);
  return 0;
}

