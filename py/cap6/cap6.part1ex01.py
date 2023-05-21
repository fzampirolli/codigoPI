"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

#include <stdio.h>
#include <stdlib.h>  // malloc e free

int** leiaMatriz(int L, int C) {
  int** m = (int**)malloc(L * sizeof(int*));
  for (int i = 0; i < L; i++) {
    m[i] = (int*)malloc(C * sizeof(int)); // for each row allocate C ints
    for (int j = 0; j < C; j++) {
      scanf("%d", &m[i][j]);
    }
  }
  return m;
}

// you must supply the number of rows
void free_matrix(int** m, int L) {
  // first free each row
  for (int i = 0; i < L; i++) {
    free(m[i]);
  }

  // Eventually free the memory of the pointers to the rows
  free(m);
}

void escrevaMatriz(int** m, int L, int C) {
  for (int i = 0; i < L; i++) {
    for (int j = 0; j < C; j++) {
      printf("%d\t", m[i][j]);
    }
    printf("\n");
  }
}
int main(void) {
  // ENTRADA DE DADOS
  int L, C, ** m;   // variaveis de referência m
  printf("Digite o número de alunos: ");
  scanf("%d", &L);

  printf("Digite o número de avaliações: ");
  scanf("%d", &C);

  C = C + 1; // a primeira coluna é o RA do aluno

  printf("Digite os elementos da matriz");
  m = leiaMatriz(L, C);

  // PROCESSAMENTO ?

  // SAÍDA DE DADOS
  printf("\nLISTA DE ALUNOS vs Avaliações:\n");
  printf("RA ");
  for (int i = 0; i < C - 1; i++) {
    printf("\t%d", (i + 1));
  }
  printf("\n");
  escrevaMatriz(m, L, C);
  free_matrix(m, L); // liberar memória alocado com malloc
  return 0;
}