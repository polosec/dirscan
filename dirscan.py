import argparse
from libs.init import Init
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('url',type=str)
    parser.add_argument('-k','--keys',dest='keywords',nargs='+',type=str,default="")
    parser.add_argument('-d',dest='delay',type=float,default=0)
    args=parser.parse_args()
    scan=Init(args)
    scan.start()
if __name__=='__main__':
    main()