#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;
struct Node {
    int data;
    Node* next;
    Node* prev;
};

Node* head = NULL;

Node* getNewNode(int data) {
    Node* newNode = malloc(sizeof(Node));
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

// O(N)
int length() {
    int i = 0;
    Node* curr = head;
    while (curr != NULL) {
        i++;
        curr = curr->next;
    }
    return i;
}

// O(n)
Node* getNode(int index) {
    if (index < 0 || index > length() - 1) return NULL;
    Node* curr = head;
    for (int i = 0; i < index; i++) curr = curr->next;
    return curr;
}

// O(1)
void deleteNode(Node* toDelete) {
    if (toDelete == head) head = toDelete->next;
    if (toDelete->next != NULL) toDelete->next->prev = toDelete->prev;
    if (toDelete->prev != NULL) toDelete->prev->next = toDelete->next;
    free(toDelete);
}

// O(1)
// Can't append at end of the list
void addNodeBefore(Node* nextNode, Node* newNode) {
    if (nextNode == NULL) printf("Can't Add there\n");
    else {
        newNode->next = nextNode;
        newNode->prev = nextNode->prev;
        nextNode->prev = newNode;
        if (newNode->prev == NULL) head = newNode; // Check if newNode was at head.
        else newNode->prev->next = newNode;
    }
}

// O(n)
// Can be made constant if we keep refrence to the tail.
void addToTail(Node* newNode) {
    if (head == NULL) head = newNode;
    else {
        Node* last = head;
        while(last->next != NULL) last = last->next;
        newNode->prev = last;
        last->next = newNode;
    }
}

// O(1)
void addNodeAfter(Node* prev, Node* newNode) {
    if (prev == NULL) printf("Can't add there!\n");
    else {
        newNode->next = prev->next;
        newNode->prev = prev;
        prev->next = newNode;
        if (prev->next != NULL) prev->next->prev = newNode;
    }
}

// O(1)
void addToHead(Node* newNode) {
    if (head == NULL) head = newNode;
    else {
        head->prev = newNode;
        newNode->next = head;
        head = newNode;
    }
}

// O(n)
void forwardPrint() {
    if (head == NULL) printf("List is Empty!");
    else {
        Node* tmp = head;
        printf("Forward: ");
        while (tmp != NULL) {
            printf("%d ", tmp->data);
            tmp = tmp->next;
        }
        printf("\n");
    }
}

// O(n)
void reversePrint(Node* tmp) {
    if (tmp == NULL){
        printf("Reverse: ");
        return;
    }
    reversePrint(tmp->next);
    printf("%d ", tmp->data);
    if (tmp == head) printf("\n");
}

int main(void) {
    addToHead(getNewNode(1));
    addToTail(getNewNode(2));
    addToTail(getNewNode(3));
    addToTail(getNewNode(5));
    forwardPrint();
    reversePrint(head);
    deleteNode(getNode(2));
    forwardPrint();
    reversePrint(head);
    addNodeBefore(getNode(2), getNewNode(3));
    forwardPrint();
    reversePrint(head);
    deleteNode(getNode(0));
    forwardPrint();
    reversePrint(head);
    addNodeBefore(getNode(0), getNewNode(1));
    forwardPrint();
    reversePrint(head);
    addNodeBefore(getNode(length() - 1), getNewNode(4));
    forwardPrint();
    reversePrint(head);
    addToTail(getNewNode(6));
    forwardPrint();
    reversePrint(head);
    addNodeAfter(getNode(length() - 1), getNewNode(7));
    forwardPrint();
    reversePrint(head);
    return 0;
}
