#include <stdio.h>
#include "Python.h"

/**
 * print_python_list - prints basic info about
 * a python list.
 *
 * @p: A pointer to a generic PyObject.
 */
void print_python_list(PyObject *p)
{
	PyListObject *plo;
	int i;
	ssize_t size;

	plo = (PyListObject *)p;
	size = plo->ob_base.ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", plo->allocated);

	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, plo->ob_item[i]->ob_type->tp_name);
	
}

/**
 * print_python_bytes -  print some basic info about
 * a Python bytes object.
 *
 * @p: A pointer to a generic PyObject.
 */
void print_python_bytes(PyObject *p)
{
	(void)p;
}
