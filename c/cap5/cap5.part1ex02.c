/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>

int main(void) {

  // ENTRADA DE DADOS
  int max = 100; // número máximo de alunos
  int n, ras[max], notas[max];   // variaveis de referência ras e notas

  printf("Digite o numero de alunos: \n");
  scanf("%d", &n);

  printf("RAs: \n");
  for (int i = 0; i < n; i++) {
    printf("RA %d: \n", i + 1);
    scanf("%d", &ras[i]);
  }

  printf("Notas: \n");
  for (int i = 0; i < n; i++) {
    printf("Nota %d: \n", i + 1);
    scanf("%d", &notas[i]);
  }

  // PROCESSAMENTO ?
  // SAÍDA
  printf("LISTA DE ALUNOS\nNúmero\t RA\t Nota\n");
  for (int i = 0; i < n; i++) {
    printf("%d\t %d\t %d\n", i + 1, ras[i], notas[i]);
  }
  //free(ras);   // liberar memória alocado com malloc
  //free(notas);
  return 0;
}