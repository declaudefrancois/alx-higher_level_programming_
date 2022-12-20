#include <stdio.h>
#include "Python.h"
#include <string.h>

void print_python_bytes(PyObject *p);

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
	{
		printf("Element %d: %s\n", i, plo->ob_item[i]->ob_type->tp_name);

		if (strcmp(plo->ob_item[i]->ob_type->tp_name, "bytes") == 0)
		{
			print_python_bytes(plo->ob_item[i]);
		}
	}
}

/**
 * print_python_bytes -  print some basic info about
 * a Python bytes object.
 *
 * @p: A pointer to a generic PyObject.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *pbo;
	ssize_t size;
	int max_bytes;

	pbo = (PyBytesObject *)p;
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(pbo))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = pbo->ob_base.ob_size;
	max_bytes = size >= 10 ? 10 : size + 1;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", pbo->ob_sval);
	printf("  first %d bytes:", max_bytes);
	for (int i = 0; i < max_bytes; i++)
	{
		printf(" %02x", pbo->ob_sval[i] & 0xff);
	}
	printf("\n");
}
