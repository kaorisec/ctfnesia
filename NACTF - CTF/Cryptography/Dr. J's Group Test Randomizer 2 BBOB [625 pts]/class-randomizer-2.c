#include <stdio.h>
#include <stdint.h>
#include <sodium.h>
#include <stdbool.h>
#include <string.h>
#define NUM_CORRECT 10

uint64_t x = 0, w = 0, s = 0xb5ad4eceda1ce2a9;

uint32_t nextRand() {
  w += s;
  x = x*x + w;
  x = (x>>32) | (x<<32);
  return x % (1UL<<32);
}

void init_seed() {
  uint64_t r1 = (uint64_t) randombytes_random();
  uint64_t r2 = (uint64_t) randombytes_random();
  x = (r1 << 32) + r2;
  r1 = (uint64_t) randombytes_random();
  r2 = (uint64_t) randombytes_random();
  w = (r1 << 32) + r2;
}

void print_flag() {
  FILE *f = fopen("flag.txt", "r");
  char flag[100];
  fgets(flag, sizeof(flag), f);
  printf("%s\n", flag);
  fflush( stdout );
  return;
}

const char *messages[NUM_CORRECT] =
{ "\nHmm... lucky guess...\n",
  "\nWow, that was coincidental!\n",
  "\nWhat? How did you guess that?\n",
  "\nThat's right, but you won't be able to guess right again!\n> ",
  "\nStrangely, that's correct...\n"
};

int main() {
  setvbuf(stdout, NULL, _IONBF, 0);
  init_seed();
  printf("\nWelcome to Dr. J's Random Number Generator v3! We have received reports of "
  "a vulnerability involving repetition of output. This vulnerability has since been patched, "
  "and Dr. J's RNG is now 100%% secure. \n"
  "[r] Print a new random number \n"
  "[g] Guess the next ten random numbers and receive the flag! \n"
  "[q] Quit \n\n");
  char line[100];
  while (true) {
    printf("> ");
    fgets (line, sizeof(line), stdin);
    line[strcspn(line, "\n")] = 0;

    if (!strcmp("r", line)) {
      uint64_t r = nextRand();
      printf("%lu\n", r);
    }
    if (!strcmp("g", line)) {
      printf("\nGuess the next ten random numbers for a flag! "
      "The chance of guessing all ten numbers correctly is 1/(2*10^96). I hope you're lucky! "
      "\nEnter Guess 1:\n> ");

      for (int i = 0; i < NUM_CORRECT; i++) {
        uint64_t guess = 0;
        fgets (line, sizeof(line), stdin);
        sscanf(line, "%lu", &guess);
        if (guess == nextRand()) {
          int m = randombytes_uniform(5);
          printf("%s", messages[m]);
          if (i < NUM_CORRECT-1) {
            printf("Enter Guess %d:\n> ", i+2);
          }
          else {
            printf("What sorcery is this? That's impossible! I guess you deserve this flag:\n");
            print_flag();
            break;
          }
        }
        else {
          printf("That's incorrect. Get out of here!\n");
          break;
        }
      }
      break;
    }
    if (!strcmp("q", line)) {
      printf("\nGoodbye!\n");
      break;
    }
  }
  return 0;
}
