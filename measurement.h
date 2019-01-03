#include<pthread.h>
#include <stdbool.h>

typedef struct {
  pthread_t tid;
  bool set;
  double call_count;
  double last_active;
  double first_active;
  double wall_time;
} MEASURE_t;

#define _MEASURE_MAX_THREADS 100
#define _MEASURE
//#define _SYNCTHREAD
#define _SYNC_NUM 1
