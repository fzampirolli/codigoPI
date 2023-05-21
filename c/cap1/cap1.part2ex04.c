/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>
int main(void) {
  double d = 3.14;
  int i = (int)d; // AQUI ESTA O CAST
  printf("double = %f\n", d);
  printf("int = %d\n", i);
  return 0;
}