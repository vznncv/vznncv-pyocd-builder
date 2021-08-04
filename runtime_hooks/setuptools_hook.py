import functools

import pkg_resources


@functools.wraps(pkg_resources.EntryPoint.require)
def requires(self, *args, **kwargs):
    pass


# mock require to use pkg_resources.iter_entry_points
pkg_resources.EntryPoint.require = requires
