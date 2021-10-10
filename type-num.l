

%{
	int posno=0;
	int negno=0;
	int frac=0;
%}

%%

\+?[0-9]+			 posno++;
-[0-9]+				 negno++;

\+?[0-9]*\.[0-9]+ frac++;
-[0-9]*\.[0-9]+ frac++;
\n {return 0;}
%%
int yywrap(){}
// driver code
int main()
{
	yylex();
	printf("\nPositive: %d", posno);
	printf("\nNegative: %d", negno);
	printf("\nFractions: %d", frac);
	return 0;
}