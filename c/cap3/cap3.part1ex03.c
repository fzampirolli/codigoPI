/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>
int main() {
  float area;
  int num;
  char escolha;
  printf("1. Circulo\n");
  printf("2. Quadrado\n");
  printf("Escolha:\n");

  scanf("%c", &escolha);

  switch (escolha) {
  case '1':
    printf("Raio:\n");
    scanf("%d", &num);
    area = 3.14 * num * num;
    printf("Area do circulo: ");
    printf("%.2f\n", area);
    break;

  case '2':
    printf("Lado:\n");
    scanf("%d", &num);
    area = num * num;
    printf("Area do quadrado: ");
    printf("%.2f\n", area);
    break;

  default:
    printf("Escolha Incorreta!\n");
  }
  return 0;
}