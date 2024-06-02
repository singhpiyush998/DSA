#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int capacity;
  int size;
  int *items;
} MinHeap;

MinHeap minheap;

int getLeftChildIndex(int parentIndex) { return 2 * parentIndex + 1; }
int getRightChildIndex(int parentIndex) { return 2 * parentIndex + 2; }
int getParentIndex(int childIndex) { return (childIndex - 1) / 2; }

int leftChild(int parentIndex) {
  return minheap.items[getLeftChildIndex(parentIndex)];
}
int rightChild(int parentIndex) {
  return minheap.items[getRightChildIndex(parentIndex)];
}
int parent(int index) { return minheap.items[getParentIndex(index)]; }

bool hasLeftChild(int index) { return getLeftChildIndex(index) < minheap.size; }
bool hasRightChild(int index) {
  return getRightChildIndex(index) < minheap.size;
}
bool hasParent(int index) { return getParentIndex(index) >= 0; }

void swap(int indexOne, int indexTwo) {
  int temp = minheap.items[indexOne];
  minheap.items[indexOne] = minheap.items[indexTwo];
  minheap.items[indexTwo] = temp;
}

void ensureExtraCapacity() {
  if (minheap.size == minheap.capacity) {
    int *newArray = malloc(sizeof(int) * minheap.capacity * 2);
    for (int i = 0; i <= minheap.size; i++)
      newArray[i] = minheap.items[i];
    minheap.capacity *= 2;
    minheap.items = newArray;
  }
}

int peek() {
  if (minheap.size == 0)
    return -1;
  return minheap.items[0];
}

void heapifyDown() {
  int index = 0;
  // We only have to check for left child because if there is no left child,
  // there certaily is no right child
  while (hasLeftChild(index)) {
    int smallerChildIndex = getLeftChildIndex(index);
    if (hasLeftChild(index) && rightChild(index) < leftChild(index))
      smallerChildIndex = getRightChildIndex(index);

    if (minheap.items[index] < minheap.items[smallerChildIndex]) {
      break;
    } else {
      swap(index, smallerChildIndex);
    }
    index = smallerChildIndex;
  }
}

int poll() {
  if (minheap.size == 0)
    return -1;
  int item = minheap.items[0];
  minheap.items[0] = minheap.items[minheap.size - 1];
  minheap.size--;
  heapifyDown();
  return item;
}

void heapifyUp() {
  int index = minheap.size - 1;
  while (hasParent(index) && parent(index) > minheap.items[index]) {
    swap(getParentIndex(index), index);
    index = getParentIndex(index);
  }
}

void add(int item) {
  ensureExtraCapacity();
  minheap.items[minheap.size] = item;
  minheap.size++;
  heapifyUp();
}

void printHeap() {
  printf("The Heap values are:\n");
  for (int i = 0; i < minheap.size; i++) {
    printf("%d ", minheap.items[i]);
  }
  printf("\n");
}

int main(void) {
  minheap.capacity = 10;
  minheap.size = 0;
  minheap.items = malloc(sizeof(int) * minheap.capacity);

  int arr[] = {10, 15, 20, 17, 25};
  for (int i = 0; i < sizeof(arr) / sizeof(int); i++) {
    minheap.items[i] = arr[i];
    minheap.size++;
  }
  printHeap();

  printf("The minimum value in array is: %d\n", poll());
  printHeap();

  add(10);
  printHeap();

  return 0;
}
