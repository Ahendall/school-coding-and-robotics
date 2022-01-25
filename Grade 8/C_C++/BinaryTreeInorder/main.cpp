/*
Given a binary tree, print out the nodes of the tree in an in-order fashion
*/

#include <bits/stdc++.h>
#include "binarytree.h"
using namespace std;

void printTreeNodesRecusivly(treeNode *node);
void printTreeNodesIterative(treeNode *node);

int main(void) {
	treeNode *root = new treeNode(4);
	createTree(root);
	printTreeNodesRecusivly(root);
	printTreeNodesIterative(root);
}

void printTreeNodesRecusivly(treeNode *node) {
	if (node->leftChild != NULL)
		printTreeNodesRecusivly(node->leftChild);
	
	cout << node->value << endl;

	if (node->rightChild != NULL)
		printTreeNodesRecusivly(node->rightChild);
}

void printTreeNodesIterative(treeNode *node) {

}