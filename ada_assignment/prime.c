#include<stdio.h>
#include<stdlib.h>
void generateArray(int point);
int main()
{
    int endPoint;
    printf("enter the end point for the prime numbers : \n");
    scanf("%d",&endPoint);
    if(endPoint < 2)
    {
        printf("the prime numbers below 2 doesnot exist: \n");
        return 0;
    }
    else{
        generateArray(endPoint);
    }
    return 0;
}

void generateArray(int point)
{
    int a[100],b[100],count=0,n;
    for(int i = 2,j = 0; i <= point; i++,j++)
    {
      a[j] = i;
    }
    for(int i = 0; i < point-1; i++)
    {
      if(a[i] == 0)
      {
          continue;
      }
      else
      {
        for(int j = i,n = a[i]; j < point - 1; j++)
        {
          if(a[j] == 0) 
          {
            continue;
          }
          else if((a[j] % n) == 0)
          {
            a[j] = 0; 
            continue;
          }
          else
          {
            b[count] = a[j];
            count++;
          }
        }
      }
    }
    printf("the array elements are:\n");
    printf("count = %d \n",count);
    // for(int i = 0; i < count; i++)
    // {
    //   printf("%d \n",b[i]);
    // }
}