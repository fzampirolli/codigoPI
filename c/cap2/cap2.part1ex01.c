/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>
 // MÉTODO
float delta(float a, float b, float c) {
  float d = b * b - 4 * a * c;
  return d;
}
// PROGRAMA PRINCIPAL
int main(void) {
  float a = 5.0, b = -2.0, c = 4.0;
  printf("O delta de ax^2 + bx + c e %.1f\n", delta(a, b, c));
  return 0;
}