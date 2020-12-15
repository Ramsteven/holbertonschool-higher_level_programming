#include "lists.h"

/**
 * check_cycle - Checks if a Linked List has a loop
 *
 * @list: The linked to be checked
 *
 * Return: 0 if there is no loop, 1 if there is a loop
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = NULL, *slow = NULL;

	fast = list;
	slow = list;

	if ((!fast) || (!slow))
		return (0);

	do {
		if ((fast->next == NULL) || (fast->next->next == NULL))
			return (0);

		fast = fast->next->next;
		slow = slow->next;
	} while (fast != slow);

	return (1);
}
