s='color'
i=iter(s)
vow=''
cons=''
try:
    while True:
        a=i.__next__()
        if a in ['a','e','i','o','u']:
            vow+=a

        else:
            cons+=a

except StopIteration:
    print('string - '+s+'\nvowels-'+vow+'\nconsonsants-'+cons)
    raise StopIteration