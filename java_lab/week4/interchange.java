import java.util.Scanner;
class interchange
{
	public static void main(String[] args)
	{
		Scanner s=new Scanner(System.in);
		int i,j,m=2;
		int A[][]=new int[3][3];
		int B[][]=new int[3][3];
		System.out.println("Enter the elements for array:\n");
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				A[i][j]=s.nextInt();

			}
		}
		for(i=0;i<3;i++)
		{
			for(j=0,m=2;j<3;j++,m--)
			{
				B[i][j]=A[i][m];
			}
		}
		System.out.println("Reverse rows elements:\n");
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				System.out.print(B[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println("Interchanging rows and columns:\n");
			for(i=0;i<3;i++)
			{
				for(j=0;j<3;j++)
				{
					A[j][i]=B[i][j];
				}
			}
		    for(i=0;i<3;i++)
		    {
			   for(j=0;j<3;j++)
			   {
				  System.out.print(A[i][j]+" ");
			   }
			   System.out.println();
		    }
		

	}
}