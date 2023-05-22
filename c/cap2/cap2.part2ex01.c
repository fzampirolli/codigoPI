/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>

 // MÉTODOS
int ParImpar(int n) {
  return n % 2;
}

float leia() {
  int valor;
  printf("Entre com um valor inteiro: ");
  scanf("%d", &valor);
  return valor;
}

// PROGRAMA PRINCIPAL
int main(void) {
  // ENTRADAS
  int n;
  n = leia();

  // PROCESSAMENTO
  int r = ParImpar(n);

  //SAÍDA
  printf("0=Par e 1=Impar : %d\n", r);
  return 0;
}