import inspect
import logging
import functools

logger = logging.getLogger(__name__)
fh = logging.FileHandler('running.log', 'w', 'utf-8')
fh.setFormatter(logging.Formatter('%(asctime)s %(name)s %(message)s'))
logger.addHandler(fh)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


def debug(*attrs):
    def wrap(f):
        attrs_set = set(attrs)
        functools.wraps(f)
        def decr(*args, **kwargs):
            result = f(*args, **kwargs)
            #logger.debug('{} {}'.format(f.__name__, [(k, v) for k, v in inspect.getclosurevars(f).nonlocals.items()]))
            logger.debug('{} {}'.format(f.__name__, locals()))
            return result
        return decr

    return wrap