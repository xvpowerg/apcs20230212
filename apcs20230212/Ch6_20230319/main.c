#include <stdio.h>
#include <stdlib.h>
#define LEN 10
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int add(int a,int b){
	int c;
	c = a + b;
	return c;
}

void myFor(int i){
	
	printf("%d\n",i);
	if (i  < 5){
		myFor(i + 1);
	}
}

int gcd(int m,int n){
	if (n == 0){
		return m;
	}else{
		gcd(n,m % n);	
	}
	
}

//�@�~�D�O���t�� 

int main(int argc, char *argv[]) {	

	
	//int myGcd = gcd(20,14);
	//printf("gcd:%d",myGcd)	; 
	//myFor(1);
	/*int ans = add(5,6);
	printf("ans:%d",ans);*/
	
	/*int arr[LEN] = {0};
	int i;
	for (i = 0; i< LEN;i++){
		printf("%d ",arr[i]);
	}
	printf("\n");
	for (i = 1; i<= LEN;i++){
		arr[i-1] = i;
	}
	printf("\n");
	for (i = 0; i< LEN;i++){
		printf("%d ",arr[i]);
	}*/
	
	
	//printf("��ܦr��:%c\n",'A');
	//printf("��ܦr���s�X:%d\n",'A');
	/*printf("��ܦr��:%c\n",65);
	printf("��ܦr��:%d\n",10);*/

/*	int a = 3,b = 55;
	double c1 = 3.14,c2 = 15.678;
	printf("a=%08d,\t b=%8d\n",a,b);
	printf("Test!");
	printf("c1=%-8.2f,\t c2 = %8.2f\n",c1,c2);*/
	
	
	/*printf("%d\n",sizeof(short));
	printf("%d\n",sizeof(int));
	printf("%d\n",sizeof(long));*/
	
	/*int input1;
	float input2;
	char input3[10];
	printf("��J���:");
	scanf("%d",&input1);
	printf("��J�B�I:");
	scanf("%f",&input2);
	printf("��J��r:");
	scanf("%10s",&input3);
	
	printf("�Ʀr:%d\n",input1);
	printf("�B�I:%.2f\n",input2);
	printf("��r:%s\n",input3);*/
	
/*	char c;
	printf("�п�J�r��:");
	c = getchar();
	putchar(c);*/
	
	
	/*char str[20];
	puts("�п�J�r��:");
	gets(str);
	
	puts("�п�J�r�ꬰ:");
	puts(str);*/
	
	/*int input = 0;	
	printf("�п�J���:");
	scanf("%d",&input);
	printf("���_��?%c\n",input % 2?'Y':'N');*/
	
	/*
	int score = 0;
	printf("�ǥͤ���:");
	scanf("%d",&score);
	printf("�O�_�ή�?%c\n",score >= 60?'Y':'N');*/
	
	/*int score = 0;
	printf("�ǥͤ���:");
	scanf("%d",&score);
	printf("�O�_�ݭn�ɦ�?%c\n",(score < 60 && score >= 40 ) ?'Y':'N');*/
	
	/*int input = 0;
	int remain = 0;
	
	printf("��J���:");
	scanf("%d",&input); 
	remain = input % 2;
	if (remain == 1){
		printf("%d�O�_��\n",input);
	}else{
		printf("%d�O����\n",input);
	}*/
	
/*	int score = 0;
	printf("�п�J���Z:");
	scanf("%d",&score);
	if (score >= 90){
		printf("A");
	}else if(score >= 80 && score < 90){
		printf("B");
	}else if(score >= 70 && score < 80){
		printf("C");
	}else if(score >= 60 && score < 70){
		printf("D");
	}else{
		printf("F");
	}*/	
	/*int action;
	printf("1 Play\n");
	printf("2 Stop\n");
	printf("3 Exit\n");
	scanf("%d",&action);	
	switch(action){
		case 1:
			puts("����");	
		break;
		case 2:
			puts("����");	
		break;
		case 3:
			puts("���}");	
		break;
		default:
			puts("���~");	
		break;	
	}*/
	
/*	int score = 0;
	int level = 0;
	printf("��J����:");
	scanf("%d",&score);
	level = score / 10;
	switch(level){
		case 10:
		case 9:
			puts("A");
		break;	
		case 8:
			puts("B");
		break;
		case 7:	
			puts("C");
		break;
		case 6:
			puts("D");
		break;	
		default:
			puts("F ���ή�");
		break;				
	}*/
	
/*	int i = 0;
	for (i = 0;i < 10;i++){
		printf("%d ",i);
	}*/
	
/*	int i = 0;
	for(i = 2;i<=9;i++){
		int k = 0;
		for (k = 1;k <= 9;k++){
			
			printf("%d*%d=%2d ",i,k,i*k);
		}
		printf("\n");
		
	}*/
	
	/*int score = 0;
	int sum = 0;
	int count = -1;
	
	while(score != -1){
		count++;
		sum += score;
		printf("��J����(-1���}):");
		scanf("%d",&score);
	}
	printf("����:%.2f",sum/(double)count);*/
	
	/*int i = 1;
	for(i = 1;i<10;i++){
		if (i % 7 == 0){
			break;
		}
		printf("%d\t",i);		
	}
	printf("\n");
	for (i = 1; i<10;i++){
		if (i % 7== 0){
			continue;
		}
		printf("%d\t",i);
		
	}*/
	
	
	/*int score = 0;
	int sum = 0;
	int count = 0;
	int i;
	
	for (i = 1; i <= 5;i++){
		printf("��J����:");
		scanf("%d",&score);
		if (score < 0 || score > 100){
			printf("���ƿ��~:%d\n",score);
			continue;
		}
		count++;
		sum += score;		
	}
	printf("�`��:%d\n",sum);
	printf("����:%.2f\n",(double)sum/count);*/
	


	return 0;
}
