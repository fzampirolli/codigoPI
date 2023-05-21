/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>

 // MÉTODOS
float delta(float a, float b, float c) {
  float d = b * b - 4 * a * c;
  return d;
}

float leia() {
  float valor;
  printf("Entre com um valor: ");
  scanf("%f", &valor);
  return valor;
}

// PROGRAMA PRINCIPAL
int main(void) {
  // ENTRADAS
  float a, b, c, d;
  a = leia();
  b = leia();
  c = leia();

  // PROCESSAMENTO
  d = delta(a, b, c);

  //SAÍDA
  printf("Delta = %.1f\n", d);
  return 0;
}