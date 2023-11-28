#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - This function checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: Returns 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *sloppy = list;
	listint_t *quick = list;

	if (!list)
		return (0);

	while (sloppy && quick && quick->next)
	{
		sloppy = sloppy->next;
		quick = quick->next->next;
		if (sloppy == quick)
			return (1);
	}
	return (0);
}

