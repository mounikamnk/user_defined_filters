from django import template
register=template.Library()
@register.filter('swapping') #filter name
def swap(data):
    return data.swapcase()

@register.filter() # automaticaly filter name as function name
def remove(data,arg):
    return data.replace(arg,'')

# register.filter('swap',swap)
# register.filter('remove',remove)
@register.filter()
def change(s):
    l=s.split()
    res=[]
    for i in range(len(l)):
        if i==0 or i==len(l)-1:
            res.append(l[i])
        else:
            res.append(l[i].lower())
    return ' '.join(res)
@register.filter()
def count(s,sub):
    c=0
    for i in range(len(s)):
        if s[i:i+len(sub):]==sub:
            c+=1
    return c