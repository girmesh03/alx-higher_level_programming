#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *previous, *current;

	previous = list;
	current = list;

	while (list && current && current->next)
	{
		previous = previous->next;
		current = current->next->next;

		if (previous == current)
		{
			list = previous;
			previous = current;
			while (1)
			{
				current = list;
				while (current->next != previous && current->next != list)
				{
					current = current->next;
				}
				if (current->next == list)
					break;
				previous = current;
			}
			return (1);
		}
	}

	return (0);
}
