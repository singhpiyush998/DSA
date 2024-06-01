#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct BinaryTreeNode BinaryTreeNode;
struct BinaryTreeNode {
  int data;
  BinaryTreeNode *left;
  BinaryTreeNode *right;
};

BinaryTreeNode *getNewNode(int data) {
  BinaryTreeNode *newNode = malloc(sizeof(BinaryTreeNode));
  newNode->left = newNode->right = NULL;
  newNode->data = data;
  return newNode;
}

BinaryTreeNode *insert(BinaryTreeNode *root, int data) {
  if (root == NULL) {
    // Tree is empty
    root = getNewNode(data);
  } else if (data <= root->data) {
    root->left = insert(root->left, data);
  } else {
    root->right = insert(root->right, data);
  }
  return root;
}

int max(int a, int b) { return a >= b ? a : b; }
int findHeight(BinaryTreeNode *root) {
  if (root == NULL)
    return -1;
  int leftHeight = findHeight(root->left);
  int rightHeight = findHeight(root->right);

  return max(leftHeight, rightHeight) + 1;
}

int main(void) {
  // address of the root not the root itself and setting tree as empty
  BinaryTreeNode *root = NULL;
  root = insert(root, 15);
  root = insert(root, 10);
  root = insert(root, 20);
  root = insert(root, 18);
  root = insert(root, 25);
  root = insert(root, 8);
  root = insert(root, 12);

  printf("The height of the binary tree is: %d\n", findHeight(root));

  return 0;
}
