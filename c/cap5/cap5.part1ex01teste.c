/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>
#include <string.h>

int main() {
  char s[40];
  printf("digite algo:\n");
  fgets(s, 40, stdin);
  printf("saida: \"%s\" tamanho: %ld\n", s, strlen(s));
  s[strlen(s) - 1] = '\0'; // substituir \n por \0
  printf("saida: \"%s\" tamanho: %ld\n", s, strlen(s));
  return 0;
}