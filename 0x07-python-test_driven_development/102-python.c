#include "Python.h"

/**
 * print_python_string - prints Python strings.
 * @p: A pointer to a generic PyObject
 * representing a PyBytesObject which stores
 * a python string.
 */
void print_python_string(PyObject *p)
{
	PyBytesObject *pso;
	Py_ssize_t size;

	printf("[.] string object info\n");	
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	pso = (PyBytesObject *) PyUnicode_AsUTF8String(p);
	size =  pso->ob_base.ob_size;

	printf("  type: ");
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("compact ascii\n");
	else if (PyUnicode_IS_COMPACT(p))
		printf("compact unicode object\n");
	else if (PyUnicode_KIND(p) == PyUnicode_WCHAR_KIND)
		printf("legacy string, not ready\n");
	else
		printf("legacy string, ready\n");

	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %s\n", pso->ob_sval);
}
