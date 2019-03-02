#include<stdio.h>
#include<stdlib.h>  

void bfs(int adj[][20],int ver[],int visited[],int size);
void insertqueue(int visitQ[],int ele,int rear);
void deletequeue(int visitQ[],int orderQ[],int front);

int main(void)
{
    int size,adj[20][20],ver[20],visited[20];
    printf("enter no of verteces: \n");
    scanf("%d",&size);
    printf("enter the verteces lable:\n");
    for(int i = 0; i < size; i++){
        scanf("%d",&ver[i]);
    }
    printf("enter the digraph edges for the matrix:\n");
    for(int i = 0; i < size; i++){
        for(int j = 0; j < size; j++){
            scanf("%d",&adj[i][j]);
        }
    }
    printf("matrix = \n");
    for(int i = 0; i < size; i++){
        for(int j = 0; j < size; j++){
            ("%d",adj[i][j]);
        }
    }   
    for(int i = 0; i < size; i++){
        visited[i] = 0;
    }
    visited[1] = 1;
    bfs(adj,ver,visited,size);
    return 0;
}

void insertqueue(int visitQ[],int ele,int rear){
   visitQ[rear] = ele;
}

void deletequeue(int visitQ[],int orderQ[],int front){
    orderQ[front] = visitQ[front];
}

void bfs(int adj[][20],int ver[],int visited[],int size)
{
    int visitQ[20],orderQ[20],ele;
    visitQ[1] = ver[1];
    for(int i = 0; i < size; i++){
        for(int j = 0; j < size; j++){
            if(adj[i][j] == 1 && visited[j] != 1){
                ele = ver[j];
                insertqueue(visitQ,ele,j);
                visited[j] = 1;
            } 
        }
        deletequeue(visitQ,orderQ,i);
    }
    printf("the order of traversing = \n");
    for(int i = 0; i < size; i++){
        printf("%d",orderQ[i]);
    }
}