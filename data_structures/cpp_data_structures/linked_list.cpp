// Linked List Set

#include<iostream>

using namespace std;

struct node {
  int data;
  node* next;
};

class list {
  private:
    node* head;
  public:
    list() {
      head = NULL;
      size = 0;
    }

    int size;

    void create_node(int value) {
      node* new_node = new node;
      new_node->data = value;
      new_node->next = NULL;

      if(head == NULL){
        head = new_node;
      } else {
        node* current = head;
        if (!exists(value)) {
          while (current->next != NULL) {
            current = current->next;
          }
          current->next = new_node;
        }
      }
      ++size;
    }

    bool exists(int value) {
      node* current = head;
      while (current != NULL){
        if (current->data == value) return true;
        current = current->next;
      }
      return false;
    }

    void delete_node(int key_value) {
      node* current = head;
      node* previous = NULL;

      if (head == NULL) return;

      if (head->data == key_value){
        current = head->next;
        delete head;
        head = current;
        --size;
        return;
      }

      if (exists(key_value)){
        while (current != NULL){
          if (current->data == key_value){
            previous->next = current->next;
            delete current;
            --size;
            return;
          } else {
            previous = current;
            current = current->next;
          }
        }
      }
    }

    void display(void) {
      node* current = head;
      while (current != NULL){
        cout << current->data << " -> ";
        current = current->next;
      }
      cout << "You've reached the tail\n";
    }
};

int main() {
  list obj;
  obj.create_node(25);
  obj.display();
  obj.create_node(50);
  obj.display();
  obj.create_node(100);
  obj.display();
  obj.delete_node(100);
  obj.display();
  obj.delete_node(25);
  obj.display();
  obj.delete_node(50);
  obj.display();
  obj.delete_node(100);
  cout << "Size: " << obj.size << endl;
  return 0;
}
