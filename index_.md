在currency_exchange的测试文件中，是从输出流中提取同学们的print语句print出来的字符串打印的，下列两种不同的格式化方法，在输出流中会不一样
![3365F305A095136802E60E0FFF0C35F7](https://pkun.oss-cn-beijing.aliyuncs.com/uPic/3365F305A095136802E60E0FFF0C35F7.jpg)
第一种会通过，但是第二种会显示out of range，如果同学们打断点调试的话，很容易就会发现这两种输出的方式输出流有很大的不同。
![A69253BEF3CE6ED1FD1383B20234C1B8](https://pkun.oss-cn-beijing.aliyuncs.com/uPic/A69253BEF3CE6ED1FD1383B20234C1B8.jpg) 
![87330C24866537A4D731D2BA5FD80078](https://pkun.oss-cn-beijing.aliyuncs.com/uPic/87330C24866537A4D731D2BA5FD80078.jpg) 
至于具体原因，大家可以自行查询python的文档。