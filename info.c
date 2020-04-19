#include "types.h"
#include "stat.h"
#include "user.h"
#include "fcntl.h"
// #include "defs.h"

int
main(int argc, char *argv[])
{
    // printf(1, "info main \n");
    if(argc == 2){
        // yes
        if(atoi(argv[1]) == 1){
            info((int)1);
        } else if (atoi(argv[1]) == 2) {
            info((int)2);
        } else if (atoi(argv[1]) == 3) {
            info((int)3);
        }
    }else {
        // no
        printf(1, "Usage: info [option 1 or 2 or 3] \n");
        exit();
    }
    exit();
}