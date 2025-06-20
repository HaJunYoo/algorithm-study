def jh_buy(jh, price):
    if jh[0] >= price:
        jh[1] += jh[0] // price
        jh[0] = jh[0] % price

def sm_buy(upstream, downstream, sm, price):
    if upstream >= 3:
        sm[0] += sm[1]*price
        sm[1] = 0
    elif downstream >= 3:
        if sm[0] >= price:
            sm[1] += sm[0] // price
            sm[0] = sm[0] % price
    
def status_return(former_price, price, status):
    
    if price - former_price > 0:
        status = 'increase'
    elif price - former_price < 0:
        status = 'decrease'
    else:
        status = 'stable'
    
    return status

def stream_return(status_stack, status, upstream, downstream):
    if status_stack[-1] != status:
        upstream, downstream = 0, 0

    if status == 'increase':
        upstream += 1
    elif status == 'decrease':
        downstream += 1
        
    
    return upstream, downstream

if __name__ == '__main__':

    money = int(input())
    prices = list(map(int, input().split()))

    jh = [money, 0]
    sm = [money, 0]

    former_price = 0
    status = 'stable'
    upstream = 0
    downstream = 0
    status_stack = [status]

    for idx, price in enumerate(prices):
        if idx == 0:
            former_price = price
        else:
            former_price = prices[idx-1]

        status = status_return(former_price, price, status) 
        upstream, downstream = stream_return(status_stack, status, upstream, downstream)
        status_stack.append(status)

        jh_buy(jh = jh, price = price)  
        sm_buy(upstream=upstream, downstream=downstream, sm=sm, price=price)    
        # print(f'{idx+1}day: {sm} price:{price} status {status} \
        #       upstream: {upstream} downstream: {downstream}')

    jh_asset = jh[0] + jh[1]*prices[-1]
    sm_asset = sm[0] + sm[1]*prices[-1]

    # print(jh_asset)
    # print(sm_asset)

    res = "SAMESAME"
    if jh_asset > sm_asset:
        res = "BNP"
    elif jh_asset < sm_asset:
        res = "TIMING"
    
    print(res)
