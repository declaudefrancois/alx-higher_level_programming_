#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 *
 * @list: A pointer to a node of the list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *initialNode = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while ((list = list->next))
	{
		if (list == initialNode)
			return (1);
	}

	return (0);
}
