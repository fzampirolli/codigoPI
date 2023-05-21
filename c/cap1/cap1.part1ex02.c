/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>
int main(void) {
  int C;
  scanf("%d", &C);
  float F = C * 9 / 5 + 32;
  printf("%d graus Celsius corresponde a %.1f graus Fahrenheit", C, F);
  return 0;
}