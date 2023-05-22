/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>

int main(void) {

  // ENTRADA DE DADOS e PROCESSAMENTO
  float acumulador = 0, nota, media;
  int contador = 0;

  printf("Entre com 10 notas válidas\n");
  while (contador < 10) {
    do {
      scanf("%f", &nota);
    } while (nota < 0.0 || nota > 10.0);
    acumulador = acumulador + nota;
    contador++;
  }
  media = acumulador / contador;

  // SAÍDA
  printf("A média das %d notas é %.1f\n", contador, media);

  return 0;
}