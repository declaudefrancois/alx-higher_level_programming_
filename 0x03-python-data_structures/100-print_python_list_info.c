#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info -  function that prints some basic
 * info about Python lists.
 *
 * @p: a pointer to a generic PyObject.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *plo;
	int i;
	ssize_t size;

	plo = (PyListObject *)p;
	size = plo->ob_base.ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", plo->allocated);

	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, plo->ob_item[i]->ob_type->tp_name);
}
