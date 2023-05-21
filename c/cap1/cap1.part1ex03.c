/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>
int main(void) {
  char ch;
  int i;
  long int li;
  short s;
  unsigned int ui;
  float f;
  double d;
  long double ld;

  printf("Numero de bytes por tipo de dados:\n");
  printf("char:         %ld\n", sizeof(ch));
  printf("int:          %ld\n", sizeof(i));
  printf("long int:     %ld\n", sizeof(li));
  printf("short:        %ld\n", sizeof(s));
  printf("unsigned int: %ld\n", sizeof(ui));
  printf("float:        %ld\n", sizeof(f));
  printf("double:       %ld\n", sizeof(d));
  printf("long double:  %ld\n", sizeof(ld));
  return 0;
}