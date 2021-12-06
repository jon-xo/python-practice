# kwargs.py

# The syntax used for keyword arguments (kwargs) is **,
# **kwargs ...




def arbitrary_keywords_args(**kwargs):
    print(type(kwargs))
    print(kwargs)
   
    print(kwargs.get('anything_goes'))

arbitrary_keywords_args(this_arg='wowzers', anything_goes=101)
