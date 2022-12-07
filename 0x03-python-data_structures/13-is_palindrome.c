#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a pointer to the head of the list.
 *
 * Return:0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int *arr = malloc(sizeof(int *));
	int i = 0, size, j;
	listint_t *h = *head;

	if (arr == NULL)
		return (1);

	while (h)
	{
		arr[i++] = h->n;
		h = h->next;
	}

	size = i;
	--i;
	for (j = 0; j < size; j++)
	{
		if (arr[j] != arr[i--])
		{
			free(arr);
			return (0);
		}
	}

	free(arr);
	return (1);
}
