#include <bits/stdc++.h>
using namespace std;

struct treeNode {
	int value;
	treeNode *leftChild, *rightChild = NULL;

	treeNode(int val) {
		value = val;
	}
};

void createTree(treeNode *rootnode) {
	treeNode *right = new treeNode(6);
	treeNode *left = new treeNode(2);

	right->rightChild = new treeNode(7);
	right->leftChild = new treeNode(5);

	left->rightChild = new treeNode(3);
	left->leftChild = new treeNode(1);

	rootnode->leftChild = left;
	rootnode->rightChild = left;
}