


- Parameter 1: Output the count of processes 
- Parameter 2: Using a global counter countsysproc in defs.h which also accomodate the declaration of system calls. Then I increase the counter in each function of sysproc.c.
- Parameter 3: The process structure proc already have the memory size. Use it to divide by the page size to obtain the page numbers. 



Detains of changes made in code:

Changes for info:

in syscall.h adding
```
#define SYS_info   22
```
in syscall.c adding 
```
extern int sys_info(void);
[SYS_info]    sys_info,
```
in defs.h adding 
```
int             info(int);
```

in user.h adding 
```
int info(int);
```

in sysproc.c adding 
```
int 
sys_info( int param)
{
  return info(param);
}
```

in usys.S adding 
```
SYSCALL(info)
```

in proc.c adding definition of 
```
int
info(int param)
```

adding the file info.c

in Makefine adding declaration of info.c
