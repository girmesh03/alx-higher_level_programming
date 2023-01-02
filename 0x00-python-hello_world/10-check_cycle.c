#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *temp;

	current = list;
	while (current != NULL)
	{
		temp = current->next;
		while (temp != NULL)
		{
			if (temp == current)
				return (1);
			temp = temp->next;
		}
		current = current->next;
	}
	return (0);
}
