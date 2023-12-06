#include "lists.h"

/**
 * listint_size - This function gets the length of the singly linked list
 * @h: the head node of the linked list
 *
 * Return: returns the length of the singly linked list
 */

int listint_size(const listint_t *h)
{
	const listint_t *curr;
	int counter = 0;

	curr = h;

	while (curr != NULL)
	{
		curr = curr->next;
		counter++;
	}
	return (counter);
}

/**
 * compare_arr - thid functin compares 2 arrays of int to check if the same
 * @arr1: the first array
 * @arr2: the second array
 * @len: length of arr1
 *
 * Return: returns 0 if not the same and 1 if the same
 */

int compare_arr(int *arr1, int *arr2, int len)
{
	int x, same;

	same = 1;

	for (x = 0; x < len; x++)
	{
		if (arr1[x] != arr2[x])
		{
			same = 0;
			break;
		}
	}
	return (same);
}

/**
 * is_palindrome - check if linked list is palidrome
 * @head: head node of the linked list
 *
 * Return: 0 if not a palindrome and 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr;
	int g, b, arr1[10240], arr2[10240], len;

	/* if linked list is empty */
	if (*head == NULL)
		return (1);
	/* if linked list does not exist */
	if (head == NULL)
		return (0);

	len = listint_size(*head);
	curr = *head;

	/* loop through the linked list and save each value of n in an array */
	g = 0;
	while (curr != NULL)
	{
		arr1[g] = curr->n;
		current = curr->next;
		g++;
	}
	/* loop through the arr1 from the end and save in arr2 */
	for (b = 0; b < len; b++)
		arr2[b] = arr1[len - 1 - b];
	return (compare_arr(arr1, arr2, len));
}
