import argparse
from libs.init import Init
import  time
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('-k','--keys',dest='keywords',nargs='+',type=str,default="")
    parser.add_argument('-d',dest='delay',type=float,default=0)
    parser.add_argument('-m',dest='method',type=str,default="")
    parser.add_argument('-t',dest='thread',type=str,default="")
    args=parser.parse_args()
    scan=Init(args)
    scan.start()
if __name__=='__main__':
    s=time.time()
    main()
    e=time.time()
    print("扫描执行完毕，总耗时%.2f秒"%(e-s))
