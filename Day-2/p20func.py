def prod(pid,pname,pcost=0.0):
    print(f'{pid}\t{pname}\t{pcost}')
prod(11,"nike",4000)


def display(**karg):
    if(karg):
        for var in karg:
            print(var,karg[var])
    else:
        print('empty args')
display(pid = 'p90',pname ='Nike' )