// 5. Write a C program to solve the tower of Hanoi using stack.

#include <stdio.h>
#include <stdlib.h>


typedef struct {
    int n;
    char from;
    char to;
    char aux;
    int state;
} Frame;

typedef struct {
    Frame items[100];
    int top;
} Stack;


void push(Stack *s, Frame f) {
    s->items[++(s->top)] = f;
}
Frame pop(Stack *s) {
return s->items[(s->top)--];
}
int isEmpty(Stack *s) {
return s->top == -1;
}
void towerOfHanoi(int n, char from, char to, char aux) {
    Stack stack;
    stack.top = -1;
    Frame f = {n, from, to, aux, 0};

    push(&stack, f);
    while (!isEmpty(&stack)) {
        f = pop(&stack);

        if (f.n == 1) {
            printf("Move disk 1 from %c ->; %c\n", f.from, f.to);
            continue;
        }
        if (f.state == 0) {
            f.state = 1;
            push(&stack, f);
            Frame f1 = {f.n - 1, f.from, f.aux, f.to, 0};
            push(&stack, f1);
        } else if (f.state == 1) {

            printf("Move disk %d from %c ->; %c\n", f.n, f.from, f.to);
            f.state = 2;
            push(&stack, f);
            Frame f2 = {f.n - 1, f.aux, f.to, f.from, 0};
            push(&stack, f2);
        }
    }
}
int main() {
int n;
printf("Enter number of disks: ");
scanf("%d", &n);
printf("\nSequence of moves:\n");
towerOfHanoi(n, 'A','C', 'B');
return 0;
}