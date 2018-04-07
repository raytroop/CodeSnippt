#include <stdio.h>
#include <malloc.h>

// typedef struct network{
//     int n;
//     int batch;
//     size_t *seen;
//     int *t;
//     float epoch;
//     int subdivisions;
//     layer *layers;
//     float *output;
//     learning_rate_policy policy;
//     ...
// } network;

// network **nets = calloc(ngpus, sizeof(network));     // L type: `network*`, R type: `network*`

int main()
{
    int row=3,column=4;
    //申请空间    
    int **a = (int**)malloc(sizeof(int*)*row);//为二维数组分配3行
    for (int i = 0; i < row; ++i){//为每列分配4个大小空间
        a[i] = (int*)malloc(sizeof(int)*column);
    }
    //初始化
    for (int i = 0; i < row; ++i){
        for (int j = 0; j < column; ++j){
            a[i][j] = i+j;
        }
    }
    //输出测试
    for (int i = 0; i < row; ++i){
        for (int j = 0; j < column; ++j){
            printf ("%d ", a[i][j]);
        }
        printf ("\n");
    }
    //释放动态开辟的空间
    for (int i = 0; i < row; ++i){
        free(a[i]);
    }
    free(a);

    return 0;
}

// raytroop@MyServer:~/CodeSnippt/CXX/array$ gcc 2dDynamic.c
// raytroop@MyServer:~/CodeSnippt/CXX/array$ ./a.out 
// 0 1 2 3 
// 1 2 3 4 
// 2 3 4 5



// darnet YOLOv3
// char *copy_string(char *s)
// {
//     char *copy = malloc(strlen(s)+1);       // allocate
//     strncpy(copy, s, strlen(s)+1);
//     return copy;
// }


// char **find_replace_paths(char **paths, int n, char *find, char *replace)
// {
//     char **replace_paths = calloc(n, sizeof(char*));        // allocate
//     int i;
//     for(i = 0; i < n; ++i){
//         char replaced[4096];
//         find_replace(paths[i], find, replace, replaced);
//         replace_paths[i] = copy_string(replaced);
//     }
//     return replace_paths;
// }


// data load_data_writing(char **paths, int n, int m, int w, int h, int out_w, int out_h)
// {
//     if(m) paths = get_random_paths(paths, n, m);
//     char **replace_paths = find_replace_paths(paths, n, ".png", "-label.png");
//     data d = {0};
//     d.shallow = 0;
//     d.X = load_image_paths(paths, n, w, h);
//     d.y = load_image_paths_gray(replace_paths, n, out_w, out_h);
//     if(m) free(paths);
//     int i;
//     for(i = 0; i < n; ++i) 
//         free(replace_paths[i]);  // clear, destroy sub cstring
//     free(replace_paths);    // clear, destory ptr array
//     return d;
// }