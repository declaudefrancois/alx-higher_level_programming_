#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;
	listint_t *head1;
	listint_t *head2;
	listint_t *head3;
	
	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");

	free_listint(head);

	head1 = NULL;
	add_nodeint_end(&head1, 1);
	add_nodeint_end(&head1, 2);
	print_listint(head1);
	if (is_palindrome(&head1) == 1)
                printf("Linked list is a palindrome\n");
        else
                printf("Linked list is not a palindrome\n");
	free_listint(head1);

	head2 = NULL;
        print_listint(head2);
        if (is_palindrome(&head2) == 1)
                printf("Linked list is a palindrome\n");
        else
                printf("Linked list is not a palindrome\n");
        free_listint(head2);

	head3 = NULL;
        add_nodeint_end(&head3, 1);
        add_nodeint_end(&head3, 2);
        add_nodeint_end(&head3, 1);
        print_listint(head3);
        if (is_palindrome(&head3) == 1)
                printf("Linked list is a palindrome\n");
        else
                printf("Linked list is not a palindrome\n");
        free_listint(head3);
	return (0);
}
