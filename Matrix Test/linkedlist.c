#include <stdio.h>
#include <stdlib.h>

typedef struct _node{
    int value;
    struct _node *next;
} node;

node *newnode(int value){
    node *newnode = malloc(sizeof(node *));
    newnode->value = value;
    newnode->next = NULL;
    return newnode;
}

int main(){
    return 0;
}