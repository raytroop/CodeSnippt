#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main ()
{
	const char *anchors = "1.08,1.19,  3.42,4.41,  6.63,11.38,  9.42,5.11,  16.62,10.52"; // same with above
  	printf("anchors:%s\n", anchors);
  	const char ch = ',';
  	char *ret;

  	// atof()会扫描参数nptr字符串，跳过前面的空格字符，
  	// 直到遇上数字或正负符号才开始做转换，而再遇到非数字或字符串结束时('\0')才结束转换，并将结果返回
  	float tx = atof(anchors);  
  	printf("The first coord: %f\n", tx);

  	ret = strchr(anchors, ch);
  	printf("|%c| 之后的字符串是 - |%s|\n", ch, ret);
   
  	return(0);
}