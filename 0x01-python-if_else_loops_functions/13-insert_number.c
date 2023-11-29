#include "lists.h"

/**
 * insert_node - The Function Inserts a number into a sorted singly-linked list.
 * @head: pointer the head of the linked list.
 * @number: Number to insert.
 *
 * Return: Returns if the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *tope;

        tope = malloc(sizeof(listint_t));
        if (tope == NULL)
                return (NULL);
        tope->n = number;

        if (node == NULL || node->n >= number)
        {
                tope->next = node;
                *head = tope;
                return (tope);
        }

        while (node && node->next && node->next->n < number)
                node = node->next;

        tope->next = node->next;
        node->next = tope;

        return (tope);
}
