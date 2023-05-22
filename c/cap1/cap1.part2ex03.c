/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>
#include <math.h>
int main(void) {
  int a = 2, b = 3, c = -5;
  float delta = b * b - 4 * a * c;
  float raiz1 = (-b + sqrt(delta)) / (2 * a);
  float raiz2 = (-b - sqrt(delta)) / (2 * a);
  printf("raiz1 = %.2f\n", raiz1);
  printf("raiz2 = %.2f\n", raiz2);
  return 0;
}