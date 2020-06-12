# dirscan(from ctfscan)
这是一款参考CTFWSCAN开发的扫描器
对CTFWSCAN做了一些改进：
## 使用方法： python dirscan.py url
## 使用生产者-消费者模型进行线程数目控制，通过命令行输入可以自定义线程数，默认为10；
## 使用队列存储生成的字典item，解决了ctfwscan文件重复扫描的bug；
## 一切参数命令行可控，不需要再打开配置文件修改。
## TODO:批量扫描
欢迎提交issues & pr！
