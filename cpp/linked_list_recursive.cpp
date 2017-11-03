// Linked List Set

#include <iostream>
#include <cassert>

using namespace std;

struct node {
  int value;
  node* next;
};

class list {
  private:
    node* head;

    bool findNode(node* i, int value) {
      if (i == NULL) return false;
      if (i->value == value) return true;
      return findNode(i->next, value);
    }

    node* find_pointer (node* pointer, int value) {
      if (pointer == NULL) return NULL;
      if (pointer->value == value) return pointer;
      return find_pointer(pointer->next, value);
    }

    void set_values(node* head, int value1, int value2) {
      if (head == NULL) return;
      if (head->value == value1) head->next = pointer(value2);
      return set_values(head->next, value1, value2);
    }

    void remove_node(node* previous, int key_value) {
      if (previous->next == NULL) return;

      if (previous->next->value == key_value){
        node* next = previous->next->next;
        delete previous->next;
        previous->next = next;
        --size;
        return;
      }

      return remove_node(previous->next, key_value);
    }

  public:
    list() {
      head = NULL;
      size = 0;
    }

    int size;

    void create(int value) {
      if(exists(value)) return;

      node* new_node = new node;
      new_node->value = value;
      new_node->next = head;
      head = new_node;
      // what's the diference between ++size and size++?
      ++size;
    }

    bool exists(int value){
      return findNode(head, value);
    }

    void remove(int value){
      if (!exists(value)) return;
      if (size == 0) return;
      if (head->value == value) {
        node* temp = head->next;
        delete head;
        head = temp;
        return;
      }
      return remove_node(head, value);
    }

    node* pointer(int value){
      if (!exists(value)) return NULL;
      if (head->value == value){
        return head;
      }
      return find_pointer(head, value);
    }

    void point_values(int value1, int value2){
      if (!exists(value1)) return;
      if (!exists(value2)) return;
      if (head->value == value1) {
        head->next = pointer(value2);
      }
      return set_values(head, value1, value2);
    }

    node* find_pointer_by_position(node* head, int value){
      while (value != 0){
        head = head->next;
        value -= 1;
      }
      return head;
    }

    bool floyds_check(int value){
      int slow = 0;
      int fast_even = 0;
      int fast_odd = 1;

      while (slow < size){
        if (head == find_pointer_by_position(head, fast_even)) return true;
        if (head == find_pointer_by_position(head, fast_odd)) return true;
        slow += 1;
        fast_even += 2;
        fast_odd += 1;
      }
      return false;
    }
};

//int main() {
//  list obj;
//  assert(obj.exists(50) == false);
//  obj.create(50);
//  obj.create(100);
//  obj.create(101);
//  obj.create(102);
//  assert(obj.exists(50) == true);
//  assert(obj.exists(100) == true);
//  assert(obj.exists(150) == false);
//  obj.remove(100);
//  obj.remove(51);
//  obj.remove(50);
//  assert(obj.exists(50) == false);
//  obj.remove(100);
//  assert(obj.exists(100) == false);
//  return 0;
//}

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
  assert(obj.floyds_check(head));
  return 0;
}
