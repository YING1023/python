try:
    inpath='G:\Python\scrapytext/scrapy.txt'
    outpath='G:\Python\scrapytext/Tscrapy.txt'
    inlist=[]
    outlist=[]
    with open(inpath,'r') as f:
        for line in f.readlines():
            inlist.append(line.strip('\n'))
    for date in inlist:
        a=str(date).split('|')[1]
        print(a)
        outlist.append(a)

    print(outlist)

    with open(outpath,'a',encoding='utf-8') as f:
        for i in outlist:
            f.write(str(i)+'\n')


except:
    print('错误')

