#include <stdio.h>
#include <signal.h>

void win()
{
	printf("You win!\n");
	char buf[256];
	FILE* f = fopen("./flag.txt", "r");
	if (f == NULL)
	{
		puts("flag.txt not found - ping us on discord if this is happening on the shell server\n");
	}
	else
	{
		fgets(buf, sizeof(buf), f);
		printf("flag: %s\n", buf);
	}
}

void vuln()
{
	char buf[16];
	printf("Type something>");
	gets(buf);
	printf("You typed %s!\n", buf);
}

int main()
{
	/* Disable buffering on stdout */
	setvbuf(stdout, NULL, _IONBF, 0);

	/* Call win() on SIGSEGV */
	signal(SIGSEGV, win);

	vuln();
	return 0;
}
