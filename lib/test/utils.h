//
// Created by Jerry Kim on 12/8/20.
//

#ifndef LIB_UTILS_H
#define LIB_UTILS_H
#include <stdio.h>
#include <stdlib.h>

void checkNull(void *dt);

int get_size(FILE *f);

char *read_binary(const char *filepath, int *size);

#endif //LIB_UTILS_H
