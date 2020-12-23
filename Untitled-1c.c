#include <stdio.h>

int main()
{
    printf("__Difference Operation in Set__\n");
    int n,m,x,y;
    int i = 0;
    
    printf("Enter the Number of Element in 1st Array : ");
    scanf("%d",&n);
    
    int a[n];
    printf("\nEnter the Elements of an Array : \n");
    for (x=0; x<n; x++)
    {
        scanf("%d",&a[x]);
        
    }
    
    printf("\nEnter the Number of Element in 2nd Array : ");
    scanf("%d",&m);
    int b[m];
    printf("\nEnter the Elements of an Array : \n");
    for (y=0; y<m; y++)
    {
        scanf("%d",&b[y]);
    }
    
    //x = 0;
    
    // print the element in both Array
    printf("\nElements of 1st Array : ");
    for (y=0; y<n; y++)
    {
        printf(" %d" , a[y]);
    }
    //x = 0;
    
    printf("\nElements of 2nd Array : ");
    for (y=0; y<m; y++)
    {
        printf(" %d" , b[y]);
    }
    //x=0
    //Difference Operation
    printf("Enter the Operation You want to perform\n\tPress1 for a-b \n\tPress 2 for b-a \n \tChoice : ");
    int choice , c[n]; 
    scanf("%d",&choice);
    if (choice == 1)
    {
        for(x=0; x<n;x++)
        {
            for(y=0;y=m;y++)
            {
                if (a[x] != b[y])
                {
                    c[i] = a[x];
                    i++;
                }
                
            }
        }
    }
    
    else
    {
        printf("\n\t_Please Check the Choice press 1 or 2_\t\n");
    }
    //print intersection outuput
    printf("\nOutput is : ");
    for(x = 0 ; x<i ; x++)
    {
        printf(" %d" , c[x]);
    }
    
}



