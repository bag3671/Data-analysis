import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
# %matplotlib inline
# mpl.rc('font', family='Malgun Gothic')
# mpl.rc('axes', unicode_minus=False)

BORDER_LINES = [[(5, 1), (5, 2), (7, 2), (7, 3), (11,3), (11, 0)],
    [(5, 4), (5, 5), (2, 5), (2, 7), (4, 7), (4, 9), (7, 9), (7, 7), (9, 7), (9, 5), (10, 5), (10, 4), (5, 4)], 
    [(1, 7), (1, 8), (3, 8), (3, 10), (10, 10), (10, 7), (12, 7), (12, 6), (11, 6), (11, 5), (12, 5), (12, 4), (11, 4),(11, 3)], 
    [(8, 10), (8, 11), (6, 11), (6, 12)], 
    [(12, 5), (13, 5), (13, 4), (14, 4), (14, 5), (15, 5), (15, 4), (16, 4), (16, 2)], 
    [(16, 4), (17, 4), (17, 5), (16, 5), (16, 6), (19, 6), (19, 5), (20, 5), (20, 4), (21, 4), (21, 3), (19, 3), (19, 1)],
    [(13, 5), (13, 6), (16, 6)],
    [(13, 5), (14, 5)],
    [(21, 2), (21, 3), (22, 3), (22, 4), (24, 4),(24,2), (21, 2)],
    [(20, 5), (21, 5), (21, 6), (23, 6)],
    [(10, 8), (12, 8), (12, 9), (14, 9), (14, 8), (16, 8), (16, 6)],
    [(14, 9), (14, 11), (14, 12), (13, 12), (13, 13)],
    [(15, 8), (17, 8), (17, 10), (16, 10), (16, 11), (14, 11)],
    [(17, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10), (21, 10)],
    [(16, 11), (16, 13)],
    [(27, 5), (27, 6), (25, 6)],
]
tmp_gu_dict = {
    '수원':['장안구','권선구','팔달구','영통구'],
    '성남':['수정구','중원구','분당구'],
    '안양':['만안구','동안구'],
    '안산':['상록구','단원구'],
    '고양':['덕양구','일산동구','일산서구'],
    '용인':['처인구','기흥구','수지구'],
    '청주':['상당구','서원구','흥덕구','청원구'],
    '천안':['동남구','서북구'],
    '전주':['완산구','덕진구'],
    '포항':['남구','북구'],
    '창원':['의창구','성산구','진해구','마산합포구','마산회원구']
}
def carto(draw_korea):
    plt.figure(figsize=(8,11))
    for idx, row in draw_korea.iterrows():
        if len(row['ID'].split()) == 2:
            dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
        elif row['ID'][:2]=='고성':
            dispname = '고성'
        else:
            dispname = row['ID']
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 9.5,1.5
        else:
            fontsize, linespacing = 9.5,1.5
        plt.annotate(dispname,(row['x']+0.5, row['y']+0.5),weight='bold',
                    fontsize=fontsize,ha='center',va='center',
                    linespacing=linespacing)
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        # print(ys, xs)
        plt.plot(xs,ys,c='black',lw=1.5)

    plt.gca().invert_yaxis()
    plt.axis('off')

    plt.tight_layout()
    plt.show()

def drawKorea(targetData, blockedMap, cmapname):
    gamma = .75
    whitelabelmin = (max(blockedMap[targetData]) - min(blockedMap[targetData]))*0.25 + min(blockedMap[targetData])
    datalabel = targetData
    
    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])
    
    mapdata = blockedMap.pivot_table(index='y', columns = 'x', values = targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
    
    plt.figure(figsize = (6, 8))
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor='#aaaaaa', linewidth=0.5)
    
    for idx, row in blockedMap.iterrows():
        if len(row['ID'].split())==2:
            dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
        elif row['ID'][:2] =='고성':
            dispname = '고성'
        else:
            dispname = row['ID']

        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 8, 1.1
        else:
            fontsize, linespacing = 9, 0.9
            
        annocolor = 'white' if row[targetData] > whitelabelmin else 'black'
        plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold', fontsize= fontsize, ha='center', va='center', linespacing=linespacing)
        
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=2)
    
    plt.gca().invert_yaxis()
    plt.axis('off')
    cb =plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)
    
    plt.tight_layout()
    plt.show()


def mk_si_name(coffee_shop):
    si = [None] * len(coffee_shop)
    for n in coffee_shop.index:
        # [-3:] 끝 3글자
        if coffee_shop['광역시도'][n][-3:] not in ['광역시', '특별시', '자치시']:
            # [:-1] 끝 1글자 빼고 나머지
            if coffee_shop['시군구'][n][:-1] =='고성' and coffee_shop['광역시도'][n] =='강원도':
                si[n] = '고성(강원)'
            elif coffee_shop['시군구'][n][:-1]=='고성' and coffee_shop['광역시도'][n] =='경상남도':
                si[n] = '고성(경남)'
            else:
                try:
                    si[n] = coffee_shop['시군구'][n][:-1]
                except:
                    pass
                
            for keys, values in tmp_gu_dict.items():
                if coffee_shop['행정구'][n] in values:
                    if len(coffee_shop['행정구'][n])==2:
                        si[n] = keys + ' '+coffee_shop['행정구'][n]
                        
                    elif coffee_shop['행정구'][n] in ['마산합포구', '마산회원구']:
                        si[n] = keys + ' '+coffee_shop['행정구'][n][2:-1]
                    else:
                        si[n]  = keys + ' '+coffee_shop['행정구'][n][:-1]
                        
        elif coffee_shop['광역시도'][n] == '세종특별자치시':
            si[n]= '세종'
        else:
            if len(coffee_shop['시군구'][n]) == 2:
                si[n] = coffee_shop['광역시도'][n][:2]+ ' '+coffee_shop['시군구'][n]
            else:
                si[n] = coffee_shop['광역시도'][n][:2]+ ' '+ coffee_shop['시군구'][n][:-1]
    return si

def insert_ID(a):
    a['ID'] = mk_si_name(a)

def pivot_cafes(a):
    return a.pivot_table('도로명주소',index=['ID'],aggfunc='count')