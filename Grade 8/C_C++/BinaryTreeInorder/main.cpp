/*
Given a binary tree, print out the nodes of the tree in an in-order fashion
*/

#include <bits/stdc++.h>
#include "binarytree.h"
using namespace std;

void printTreeNodes(treeNode *node);

int main(void) {
	treeNode *root = new treeNode(4);
	createTree(root);
	printTreeNodes(root);
}

void printTreeNodes(treeNode *node) {
	if (node->leftChild != NULL)
		printTreeNodes(node->leftChild);
	
	cout << node->value << endl;

	if (node->rightChild != NULL)
		printTreeNodes(node->rightChild);
}