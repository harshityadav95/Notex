# Sorting Algos

#### [<--Back to Home](../Readme.md)

#### Bubble Sort

```c++
for(int i=0;i<n-1;i++)
    {
            for(int j=0;j<n-1-i;j++)
            {
                if(a[j]>a[j+1])
                {
                    int temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
            }

    }
```



