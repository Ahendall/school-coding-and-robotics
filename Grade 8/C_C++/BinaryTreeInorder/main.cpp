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

// Print nodes iteratively
void printTreeNodesIterative(treeNode *node) {
	stack<treeNode *> s;
	treeNode *temp = node;
	while (temp != NULL || !s.empty()) {
		while (temp != NULL) {
			s.push(temp);
			temp = temp->leftChild;
		}
		temp = s.top();
		s.pop();
		cout << temp->value << endl;
		temp = temp->rightChild;
	}

	// Time complexity: O(n)
	// Space complexity: O(n)
}
