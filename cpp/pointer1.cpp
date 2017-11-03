#include <iostream>

struct Node {
  int value;
  struct Node* next;
};

int main()
{

  Node* one = new Node;
  Node* two = new Node;
  Node* three = new Node;
  Node* x;

  Node y;
  x = &y;

  (*one).value = 1;
  (*two).value = 2;
  (*three).value = 3;

  one->next = two;
  two->next = three;
  three->next = one;

	return 0;
}
