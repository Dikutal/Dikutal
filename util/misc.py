from django.core.cache import cache

def cached(cache_key='', timeout_seconds=1800):
    """Django cache decorator

    Example 1:
    class MenuItem(models.Model):
        @classmethod
        @cached('menu_root', 3600*24)
        def get_root(self):
            return MenuItem.objects.get(pk=1)

    Example 2:
    @cached(lambda u: 'user_privileges_%s' % u.username, 3600)
    def get_user_privileges(user):
        #...
    """
    def _cached(func):
        def do_cache(*args, **kws):
            if isinstance(cache_key, str):
                key = cache_key % locals()
            elif callable(cache_key):
                key = cache_key(*args, **kws)
            data = cache.get(key)
            if data: return data
            data = func(*args, **kws)
            cache.set(key, data, timeout_seconds)
            return data
        return do_cache
    return _cached
