from functools import partial

def set_page(page_list,page):
    """
    page_list   页码范围
    page  页码
    想要当前页码的前两页和后两页
    """
    if page-3<0:
        start=0
    else:
        start=page-3
    if page+2>49:
        end=49
    else:
        end=page+2
    return list(page_list[start:end])

if __name__ == '__main__':
    page_list=range(1,50)
    setPage=partial(set_page,page_list)
    while True:
        page=int(input(">>>"))
        print(setPage(page))
